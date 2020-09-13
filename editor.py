try:
    from moviepy.editor import *
    import moviepy.editor as mp
except:
    print("MoviePy not installed, please run the following command in your terminal")
    print(">>> pip install moviepy")
import os
from os import path
import random

print("Automated Python Video Editor, Created By Jerry He 2020 with Python 3. Created with MoviePy")
print("This program can cut multiple clips at once in CSV form. It can also cut single clips. It can also concatenate clips together and add audio over a video")
print("\n")
print("Type \'quit\' to end the program")
print("Note: Times must be entered in the following forms : 1-31, 1:31, 1;31, 91 - Representing 91 seconds")
print("Enter one of the following to tell the program what to do: [single-clip, multi-clip, concatenate-video, concatenate-audio]")
print("It is strongly recommended that you read the documentation prior to using this application")
print("________________________________________________________________________________________________________")
print("\n")

def getPath():
    folderPath = input("Enter the path of the folder that you want the output files to be stored : ")
    try:
        if(path.exists(folderPath) == False):
            os.mkdir(folderPath)
        os.chdir(folderPath)
        print("Output files will go to " + folderPath)
    except:
        print("Invalid Path")
        getPath()


def isInt(currTime):
    try:
        intNum = float(currTime)
    except:
        return False
    return True

def time2Second(currTime):
    time = str(currTime)
    if(isInt(time)):
        time = float(time)
        return time
    elif(':' in time):
        time = time.split(":")
    elif('-' in time):
        time = time.splti("-")
    elif(';' in time):
        time = time.split(';')
    return 60 * float(time[0]) + float(time[1])

def cutInterval(start, stop, source, name):

    clip = VideoFileClip(source)
    subclip = clip.subclip(t_start = time2Second(start), t_end = time2Second(stop))
    subclip.write_videofile(str(name) + ".mp4")


#cutInterval('1:15', '1:20', "D:/finalKrunker/k9.mp4","kYeet.mp4")
def equals(str1, str2):
    if(str1.strip().lower() == str2.strip().lower()):
        return True
    return False

def isVid(str1):
    ext = str1.split('.')[1]
    if(ext in ['mp4','m4v','f4v','m4b','m4r','mov']):
        return True
    return False
def isAudio(str1):
    ext = str1.split('.')[1]
    if(ext in ['mp3','waptt','3ga','wav','m4a']):
        return True
    return False
def getExt(str1):
    ext = str1.split('.')[1]
    return '.' + ext
def singleClip():
    print("You have selected single-clip! A video clip source, start time, end time, and clip name must be provided")
    source = input("Enter the FULL file path of the video you want to clip : ")
    start = input("Enter start time of the clip: ")
    stop = input("Enter stop time of the clip: ")
    name = input("Enter the name you want your clip to be naned (don't include the file extension) : ")
    if(name == ""):
        name = "noname"
    try:
        print("Clipping Procedure Started!...")
        cutInterval(time2Second(start), time2Second(stop), source, name)
        print("\n")
    except:
        print("Ending.....")
        print("An Error Occured :(")
        print("\n")

def multiClip():
    print("You have selected multi-clip! A CSV file and a folder of videos must be provided. (CSV formatting on documentation)")
    source = input("Enter full path to your folder of videos : ")
    ext = input("Enter extension of your files (.mp4, .wav): ")
    csvFile = input("Enter full path to your csv file : ")
    count = 1
    try:
        csv = open(csvFile)
        try:
            for line in csv.readlines():
                _line = line.split(',')
                t1 = time2Second(_line[1])
                t2 = time2Second(_line[2])
                cutInterval(t1,t2, source + '/' + _line[0] + ext, str(count))
                count += 1

        except:
            pass
    except:
        print("An error Occured :(")
        print("\n")


def concat_video():
    print("You have selected concatenate-video! A folder of videos must be provided. Videos will be concatenated alphabetically or randomly if specified!")
    print("Make sure you only have videos in folder!")
    random1 = input("Videos concatenated randomly? (yes || no) : ")
    randomly = False
    if(equals(random1, 'yes')):
        randomly = True
    name = input("Enter the name you want your file to be named (Do not include file ext): ")
    if(name == ""):
        print("No name was given so the file will be named default")
        name = "default"
    folderPath = input("Enter path to your folder of videos : ")
    if(path.exists(folderPath) == False):
        print("Invalid Path")
        return -1
    folderPath += '/'
    try:
        files = os.listdir(folderPath)
        for i in range(len(files)):
            files[i] = folderPath + files[i]
        proc_files = []
        currExt = ''
        for i in files:
            if(isVid(i)):
                currExt = getExt(i)
                proc_files.append(VideoFileClip(i))
            else:
                print(i + " was dropped as it was not a video file")
        concat_vid = mp.concatenate_videoclips(proc_files)
        concat_vid.write_videofile(name + currExt, codec = 'libx264')
    except:
        print("An error Occured :(")

def concat_audio():
    print("You have selected concatenate-audio! A folder of audio files must be provided. Audio files will be concatenated alphabetically or randomly if specified!")
    print("Make sure you only have audio-files in folder!")
    random1 = input("Audio concatenated randomly? (yes || no) : ")
    randomly = False
    if(equals(random1, 'yes')):
        randomly = True
    name = input("Enter the name you want your file to be named (Do not include file ext): ")
    if(name == ""):
        print("No name was given so the file will be named default")
        name = "default"
    folderPath = input("Enter path to your folder of audio files : ")
    if(path.exists(folderPath) == False):
        print("Invalid Path")
        return -1
    folderPath += '/'
    try:
        files = os.listdir(folderPath)
        for i in range(len(files)):
            files[i] = folderPath + files[i]
        proc_files = []
        currExt = ''
        for i in files:
            if(isAudio(i)):
                currExt = getExt(i)
                proc_files.append(AudioFileClip(i))
            else:
                print(i + " was dropped as it was not a audio file")
        concat_audio = mp.concatenate_audioclips(proc_files)
        concat_audio.write_audiofile(name + currExt)
    except:
        print("An error Occured :(")

getPath()
while (True):
    command = input("Enter Command : ")
    if(equals(command, 'quit')):
        exit()
    elif(equals(command, 'single-clip')):
        singleClip()
    elif(equals(command, 'multi-clip')):
        multiClip()
    elif(equals(command, 'concatenate-video')):
        concat_video()
    elif(equals(command, 'concatenate-audio')):
        concat_audio()
    else:
        print("command not recognized")
