# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:37:05 2020

@author: keena
"""

import os
import pathlib

originalPath = os.getcwd()
"""
print(originalPath)
print(os.path.basename(originalPath))
"""
os.chdir(originalPath)
import VideoToFrames
from os import path

TRAINING_SET = "/dataset/training_set/"

def toImageTrainingFolder( string ):
    print("\n\n Moving" + string +" training files to training images pic directory\n\n")
    
    #Creates an array of the files in the directory prior to any changes
    videoArr = os.listdir(originalPath+TRAINING_SET+string)
    
    #Gets the amount of files in the directory
    arrayLen = len( videoArr )
    
    #changes directory to main working directory
    VideoToFrames.changeDir(originalPath)
    
    #the directory we will be working in and grabbing files
    currentDir = "/dataset/training_set/" + string + "/"
    
    #the directory we will be sending files
    destinationDir = "/dataset/training_set_frames/"+string+"/"
    
    #this is a check if there are any files to break into images
    if (arrayLen > 0):
        
        #loops through all the videos in the array
        for video in range(arrayLen):
            
            #makes sure array is empty when breaking a video down to images
            VideoToFrames.dumpArr()
            
            #gets the video at the index
            videoFile = videoArr[ video ]
            
            #prints out a check to know what video is being worked on
            print("\n\n Working on: \n\n")
            print("\t"+videoFile+"\n")
            
            #change the working directory to where the videos are located
            VideoToFrames.changeDir(originalPath+currentDir)
            
            #gets the framerate needed to get x frames
            frameRate = VideoToFrames.getFrameRate(originalPath+currentDir+videoFile, 18)
            
            #breaks the video into frames
            VideoToFrames.getFrame(originalPath+currentDir+videoFile, 0, frameRate, 1)
            
            #gets the newly created image files
            imageArr = VideoToFrames.getFrameArray()
            
            print(imageArr)
            
            #change working directory back to main directory
            VideoToFrames.changeDir(originalPath)
            
            #gets the number of images
            imageArrLen = len( imageArr )
            
            #loops through each image
            for frame in range(imageArrLen):
                
                #the path is a variable for the working directory
                #path = str(pathlib.Path().absolute())
                
                #gets the filename onlhy
                imageOnlyArr = imageArr[frame].split('/')[-1]
                
                #moves the file over to the destination directory
                os.replace(str(originalPath)+str(currentDir)+str(imageOnlyArr),
                           str(originalPath)+str(destinationDir)+str(imageOnlyArr))
                
                #move back to the main directory
                os.chdir(originalPath)
       
    #return 0 if there are no videos         
    else:
        os.chdir(originalPath)
        return 0



def toImageValidationFolder( folderName ):
    print("\n\n Moving "+folderName+" test files to test images pic directory\n\n")
    
    #Creates an array of the files in the directory prior to any changes    
    videoArr = os.listdir(originalPath+"/dataset/validation_set/"+folderName)
    
    #Gets the amount of files in the directory    
    arrayLen = len( videoArr )

    #changes directory to main working directory
    VideoToFrames.changeDir(originalPath)
    
    
    currentDir = "/dataset/validation_set/"+folderName+"/"
    
    
    destinationDir = "/dataset/validation_set_frames/"+folderName+"/"
    
    
    if (arrayLen > 0):    
        
        
        for video in range(arrayLen):
            
            
            VideoToFrames.dumpArr()
            
            
            videoFile = videoArr[ video ]
            
            
            print("\n\n Working on: \n\n")
            print("\t"+videoFile+"\n")
            
            
            VideoToFrames.changeDir(originalPath+currentDir)
            
            
            frameRate = VideoToFrames.getFrameRate(originalPath+currentDir+videoFile, 18)
            
            
            VideoToFrames.getFrame(originalPath+currentDir+videoFile, 0, frameRate, 1)
            
            
            imageArr = VideoToFrames.getFrameArray()
            
            
            VideoToFrames.changeDir(originalPath)
            
            
            imageArrLen = len( imageArr )
            
            
            for frame in range(imageArrLen):
                
                
                #path = str(pathlib.Path().absolute())
                
                
                imageOnlyArr = imageArr[frame].split('/')[-1]
                
                
                os.replace(str(originalPath)+str(currentDir)+str(imageOnlyArr),
                           str(originalPath)+str(destinationDir)+str(imageOnlyArr))
                
                
                os.chdir(originalPath)
                
    else:
        os.chdir(originalPath)
        return 0
    


toImageTrainingFolder("excellent")
toImageValidationFolder("excellent")

toImageTrainingFolder("good")
toImageValidationFolder("good")

toImageTrainingFolder("fair")
toImageValidationFolder("fair")

toImageTrainingFolder("poor")
toImageValidationFolder("poor")

toImageTrainingFolder("extremelyObstructed")
toImageValidationFolder("extremelyObstructed")
