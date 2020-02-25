###############################################################################
# AUTHOR: Samantha Muellner, Keenan Swanson

# DESCRIPTION: will organize our training and validation videos into 
#         the appropriate folders

# VERSION: 2.0.0v
###############################################################################

import os, pathlib
import variables

# declare variables
EXCELLENT_INPUT_PATH = (variables.SORTING_VIDEOS_INPUT_PATH 
                                                + variables.EXCELLENT_FOLDER)

EXTREMELY_OBSTRUCTED_INPUT_PATH = (variables.SORTING_VIDEOS_INPUT_PATH 
                                    + variables.EXTREMELY_OBSTRUCTED_FOLDER)

GOOD_INPUT_PATH = (variables.SORTING_VIDEOS_INPUT_PATH 
                                                    + variables.GOOD_FOLDER)

POOR_INPUT_PATH = (variables.SORTING_VIDEOS_INPUT_PATH 
                                                    + variables.POOR_FOLDER)


EXCELLENT_OUTPUT_PATH = (variables.SORTING_VIDEOS_OUTPUT_PATH 
                                                + variables.EXCELLENT_FOLDER)

EXTREMELY_OBSTRUCTED_OUTPUT_PATH = (variables.SORTING_VIDEOS_OUTPUT_PATH 
                                    + variables.EXTREMELY_OBSTRUCTED_FOLDER)

GOOD_OUTPUT_PATH = (variables.SORTING_VIDEOS_OUTPUT_PATH 
                                                    + variables.GOOD_FOLDER)
                                                    
POOR_OUTPUT_PATH = (variables.SORTING_VIDEOS_OUTPUT_PATH 
                                                    + variables.POOR_FOLDER)


originalPath = os.getcwd()

###############################################################################
# FUNCTION NAME: getFileNumberOfFiles
# WHAT IT DOES: will get the amount of files in the given directory
# RETURN: amount of files in directory
###############################################################################

def getFileNumberOfFiles(filePath):
    filesNum = len(os.listdir(originalPath + filePath))
    return filesNum


###############################################################################
# FUNCTION NAME: moveRemainingOfToTraining
# WHAT IT DOES: will move the videos that have not been moved into the 
#           validation folder into the training folder
# RETURN: 0 if there are no videos remaining
###############################################################################

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

###############################################################################
# FUNCTION NAME: get20PercentOfVideos
# WHAT IT DOES: will calculate what 20% of the videos in the folder is
# RETURN: the number of videos that equates to 20% of the total amount or 0 if 
#       there are less than 5 videos in the folder (as this will mean we need
#       to transfer .3 videos or such)
###############################################################################

def get20PercentOfVideos(filePath):
    total = getFileNumberOfFiles(filePath)

    if(total * .2 > 0 and total * .2 < 1):
        return 0

    validationSet = int(total * .2)
    return validationSet

###############################################################################
# FUNCTION NAME: moveToValidation
# WHAT IT DOES: will move the files from the inputFilePath to the outputFilePath
#           - specifically will move 20% of the videos in that folder
# RETURN: 0 if there are no videos to move
###############################################################################

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

###############################################################################
# FUNCTION NAME: main
# WHAT IT DOES: main file that will allow us to sort all our videos into 
#           train and validation sets for all categories
# RETURN: none
###############################################################################

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


# main()