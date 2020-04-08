# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:37:03 2020

@author: Keenan
"""
import cv2,os
count = 0
sec = 0
vidLen = 0
expectedFrames = 18;
originalDir = os.getcwd()

def changeDir( directory ):
    os.chdir( directory )

def getVidName( videoFile ):
    string = videoFile
    strArr = string.split('.')
    string = strArr[0]
    return string

def getVidDuration( videoFile ):
    video = cv2.VideoCapture( videoFile )
    fps = video.get(cv2.CAP_PROP_FPS)
    framesCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
    length = 0
    if(fps == 0):
        length = 0
    else:
        length = int(framesCount/fps)
    return length

#vidLen = getVidDuration( '1179_20180822_155018.mp4' )

def getFrame(videoFile, seconds, fr, counts):
     count = 0#, vidLen
     sec = 0
     count += counts
     sec += seconds
     vid = cv2.VideoCapture( videoFile )
     vidName = getVidName( videoFile )
    
     if sec > getVidDuration(videoFile):
         return print("The video has been divided into frames\n\n")
    
     if fr == 0:
         fr = getVidDuration(videoFile)/vid.get(cv2.CAP_PROP_FPS)#30
         fr = round(fr,2)
         print("The frame rate is %d\n", fr)
    
     vid.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
     success,image = vid.read()
    
     if success:
         cv2.imwrite(vidName + "_frame_"+str(count)+".jpg", image) # save frame as JPG file
         frameArr.append(vidName+ "_frame_"+str(count)+".jpg")
         #print(sec)
         sec += fr
         sec = round(sec,2)
         count += 1
     return getFrame( videoFile, sec, fr, count)


frameArr = []
def getFrameArray():
    return frameArr

def dumpArr():
    global frameArr
    while len(frameArr) > 0:
        frameArr.pop()
        
def deleteFiles( directory ):
    os.chdir( directory )
    #global frameArr
    arrayOfImages = os.listdir( directory )
    for file in range(len(arrayOfImages)):
        fileName = arrayOfImages[file]
        os.remove(fileName)
    os.chdir(originalDir)
    dumpArr()
    
    
def getAllImagesNotDeleted( array, directory ):
    files = os.listdir( directory )
    #for videos in range(len(array)):
        #files.pop( files.index(array[ videos ] ))
    #os.chdir( directory )
    print(files)
    for file in range(len(files)):
        fileName = files[file]
        os.remove(fileName)
    os.chdir(originalDir)

def getFrameRate( videoFile, expectedFrames):
    if(expectedFrames > 0):
        return getVidDuration(videoFile)/expectedFrames
    else:
        return getVidDuration(videoFile)/9 #WE WILL MAKE 9 DEFAULT
#frameRate = vidLen/expectedFrames

#getFrame( '1179_20180822_155018.mp4' , sec, getFrameRate("1179_20180822_155018.mp4",18))
#print(frameArr)

