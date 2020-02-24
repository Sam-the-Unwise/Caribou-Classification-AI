# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:48:27 2020

@author: keena
"""
import os
import pathlib

originalPath = os.getcwd()



#This program splits each category into 80% training and 20% validation

def getFileNumberOfExcellent():
    files = len(os.listdir(originalPath+"/VideosBeforeSort/Excellent"))
    return files

def getFileNumberOfGood():
    files = len(os.listdir(originalPath+"/VideosBeforeSort/Good"))
    return files

def getFileNumberOfFair():
    files = len(os.listdir(originalPath+"/VideosBeforeSort/Fair"))
    return files

def getFileNumberOfPoor():
    files = len(os.listdir(originalPath+"/VideosBeforeSort/Poor"))
    return files

def getFileNumberOfObstructed():
    files = len(os.listdir(originalPath+"/VideosBeforeSort/ExtremelyObstructed"))
    return files


def moveExcellentToValidation( amount ):
    currentDir = originalPath+"/VideosBeforeSort/Excellent/"
    destinationDir = originalPath+"/dataset/validation_set/excellent/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Excellent")
    if( amount > 0 ):
        for index in range( amount ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0
        
def moveRemainingOfExcellentToTraining():
    total = getFileNumberOfExcellent()
    currentDir = originalPath+"/VideosBeforeSort/Excellent/"
    destinationDir = originalPath+"/dataset/training_set/excellent/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Excellent")
    if(total > 0):
        for index in range( total ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0
    
## GOOD
def moveGoodToValidation( amount ):
    currentDir = originalPath+"/VideosBeforeSort/Good/"
    destinationDir = originalPath+"/dataset/validation_set/good/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Good")
    if( amount > 0 ):
        for index in range( amount ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0
        
def moveRemainingOfGoodToTraining():
    total = getFileNumberOfGood()
    currentDir = originalPath+"/VideosBeforeSort/Good/"
    destinationDir = originalPath+"/dataset/training_set/good/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Good")
    if(total > 0):
        for index in range( total ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0

## FAIR
def moveFairToValidation( amount ):
    currentDir = originalPath+"/VideosBeforeSort/Fair/"
    destinationDir = originalPath+"/dataset/validation_set/fair/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Fair")
    if( amount > 0 ):
        for index in range( amount ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0
        
def moveRemainingOfFairToTraining():
    total = getFileNumberOfFair()
    currentDir = originalPath+"/VideosBeforeSort/Fair/"
    destinationDir = originalPath+"/dataset/training_set/fair/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Fair")
    if(total > 0):
        for index in range( total ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])

## POOR          
def movePoorToValidation( amount ):
    currentDir = originalPath+"/VideosBeforeSort/Poor/"
    destinationDir = originalPath+"/dataset/validation_set/poor/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Poor")
    if( amount > 0 ):
        for index in range( amount ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0
        
def moveRemainingOfPoorToTraining():
    print("WORKING ON POOR TRAINING")
    total = getFileNumberOfPoor()
    currentDir = originalPath+"/VideosBeforeSort/Poor/"
    destinationDir = originalPath+"/dataset/training_set/poor/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/Poor")
    if(total > 0):
        for index in range( total ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
## Obstructed
def moveObstructedToValidation( amount ):
    currentDir = originalPath+"/VideosBeforeSort/ExtremelyObstructed/"
    destinationDir = originalPath+"/dataset/validation_set/extremelyObstructed/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/ExtremelyObstructed")
    if( amount > 0 ):
        for index in range( amount ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
    else:
        return 0
        
def moveRemainingOfObstructedToTraining():
    total = getFileNumberOfObstructed()
    currentDir = originalPath+"/VideosBeforeSort/ExtremelyObstructed/"
    destinationDir = originalPath+"/dataset/training_set/extremelyObstructed/"
    #path = str(pathlib.Path().absolute())
    fileArr = os.listdir(originalPath+"/VideosBeforeSort/ExtremelyObstructed")
    if(total > 0):
        for index in range( total ):
            os.replace(currentDir+fileArr[index],
                       destinationDir+fileArr[index])
            


def get20PercentOfExcellentVideos():
    total = getFileNumberOfExcellent()
    if(total * .2 > 0 and total * .2 < 1):
        return 1
    validationSet = int(total * .2)
    return validationSet

def get20PercentOfGoodVideos():
    total = getFileNumberOfGood()
    if(total * .2 > 0 and total * .2 < 1):
        return 1
    validationSet = int(total * .2)
    return validationSet

def get20PercentOfFairVideos():
    total = getFileNumberOfFair()
    if(total * .2 > 0 and total * .2 < 1):
        return 1
    validationSet = int(total * .2)
    return validationSet

def get20PercentOfPoorVideos():
    total = getFileNumberOfPoor()
    if(total * .2 > 0 and total * .2 < 1):
        return 1
    validationSet = int(total * .2)
    return validationSet

def get20PercentOfObstructedVideos():
    total = getFileNumberOfObstructed()
    if(total * .2 > 0 and total * .2 < 1):
        return 1
    validationSet = int(total * .2)
    return validationSet


moveExcellentToValidation(get20PercentOfExcellentVideos())
moveRemainingOfExcellentToTraining()

moveGoodToValidation(get20PercentOfGoodVideos())
moveRemainingOfGoodToTraining()

moveFairToValidation(get20PercentOfFairVideos())
moveRemainingOfFairToTraining()

movePoorToValidation(get20PercentOfPoorVideos())
moveRemainingOfPoorToTraining()

moveObstructedToValidation(get20PercentOfObstructedVideos())
moveRemainingOfObstructedToTraining()