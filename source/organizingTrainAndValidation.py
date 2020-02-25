###############################################################################
# AUTHOR: Samantha Muellner, Keenan Swanson

# DESCRIPTION: will organize our training and validation videos into 
#         the appropriate folders

# VERSION: 2.0.0v
###############################################################################

import os
import pathlib

# declare variables
EXCELLENT_INPUT_PATH = "/VideosBeforeSort/Excellent/"
EXTREMELY_OBSTRUCTED_INPUT_PATH = "/VideosBeforeSort/Extremely_Obstructed/"
GOOD_INPUT_PATH = "/VideosBeforeSort/Good_to_Poor/"
POOR_INPUT_PATH = "/VideosBeforeSort/Poor/"

EXCELLENT_OUTPUT_PATH = "/dataset/training_set/Excellent/"
EXTREMELY_OBSTRUCTED_OUTPUT_PATH = "/dataset/training_set/Extremely_Obstructed/"
GOOD_OUTPUT_PATH = "/dataset/training_set/Good_to_Poor/"
POOR_OUTPUT_PATH = "/dataset/training_set/Poor/"



originalPath = os.getcwd()

def getFileNumberOfFiles(filePath):
    files = len(os.listdir(originalPath + filePath))
    return files



def moveRemainingOfToTraining(inputFilePath, outputFilePath):
    total = getFileNumberOfFiles(inputFilePath)
    currentDir = originalPath + inputFilePath
    destinationDir = originalPath + outputFilePath

    fileArr = os.listdir(currentDir)

    if(total > 0):
        for index in range( total ):
            os.replace(currentDir + fileArr[index],
                       destinationDir + fileArr[index])
    else:
        return 0


def get20PercentOfVideos(filePath):
    total = getFileNumberOfFiles(filePath)

    if(total * .2 > 0 and total * .2 < 1):
        return 1

    validationSet = int(total * .2)
    return validationSet


def moveToValidation(inputFilePath, outputFilePath ):
    # get number of videos currently in the directory
    amount = get20PercentOfVideos(inputFilePath)

    currentDir = originalPath + inputFilePath
    destinationDir = originalPath + outputFilePath

    #path = str(pathlib.Path().absolute())

    fileArr = os.listdir(currentDir)

    if( amount > 0 ):
        for index in range( amount ):
            os.replace(currentDir + fileArr[index],
                       destinationDir + fileArr[index])
    else:
        return 0


def organizeVideos():
    # sort all excellent videos
    moveToValidation(EXCELLENT_INPUT_PATH, EXCELLENT_OUTPUT_PATH)
    moveRemainingOfToTraining(EXCELLENT_INPUT_PATH, EXCELLENT_OUTPUT_PATH)

    # sort all EO videos
    moveToValidation(EXTREMELY_OBSTRUCTED_INPUT_PATH, EXTREMELY_OBSTRUCTED_OUTPUT_PATH)
    moveRemainingOfToTraining(EXTREMELY_OBSTRUCTED_INPUT_PATH, EXTREMELY_OBSTRUCTED_OUTPUT_PATH)

    # sort all good videos
    moveToValidation(GOOD_INPUT_PATH, GOOD_OUTPUT_PATH)
    moveRemainingOfToTraining(GOOD_INPUT_PATH, GOOD_OUTPUT_PATH)

    # sort all poor videos
    moveToValidation(POOR_INPUT_PATH, POOR_OUTPUT_PATH)
    moveRemainingOfToTraining(POOR_INPUT_PATH, POOR_OUTPUT_PATH)