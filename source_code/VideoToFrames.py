# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:37:03 2020

@author: Keenan
"""
import cv2
count = 0
sec = 0
vidLen = 0
expectedFrames = 18

def getVidDuration( videoFile ):
    video = cv2.VideoCapture( videoFile )
    fps = video.get(cv2.CAP_PROP_FPS)
    framesCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
    length = int(framesCount/fps)
    return length

vidLen = getVidDuration( '1179_20180822_155018.mp4' )

def getFrame(videoFile, seconds, fr):
    global count, sec, vidLen
    vid = cv2.VideoCapture( videoFile )
    
    if sec > vidLen:
        return print("The video has been divided into frames")
    
    if fr == 0:
        fr = vidLen/vid.get(cv2.CAP_PROP_FPS)
        fr = round(fr,2)
        print("The frame rate is %d\n", fr)
    
    vid.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    success,image = vid.read()
    
    if success:
        cv2.imwrite("image"+str(count)+".jpg", image) # save frame as JPG file
        frameArr.append("image"+str(count)+".jpg")
        print(sec)
        sec += fr
        sec = round(sec,2)
        count += 1
    return getFrame( videoFile, sec, fr)

#TODO: dumpArray
    

frameArr = []

frameRate = vidLen/expectedFrames

getFrame( '1179_20180822_155018.mp4' , sec, frameRate)
getFrame
print(frameArr)
