"""
AUTHOR: Samantha Muellner, Keenan Swanson

DESCRIPTION: script that will test our unknown videos against the saved CNN MODEL

VERSION: 2.0.1v
"""

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import testingVideosToFrames, variables # import necessary files

# define variables
ORIGINAL_PATH = os.getcwd()

EXCELLENT_OUTPUT_PATH = variables.VIDEO_OUTPUT_PATH + variables.EXCELLENT_FOLDER
EXTREMELY_OBSTRUCTED_OUTPUT_PATH = variables.VIDEO_OUTPUT_PATH + variables.EXTREMELY_OBSTRUCTED_FOLDER
GOOD_OUTPUT_PATH = variables.VIDEO_OUTPUT_PATH + variables.GOOD_FOLDER
POOR_OUTPUT_PATH = variables.VIDEO_OUTPUT_PATH + variables.POOR_FOLDER


MODEL = load_model(variables.MODEL_PATH).load_weights(variables.MODEL_WEIGHTS_PATH) # load our model

img_width, img_height = 50, 50

###############################################################################
# FUNCTION NAME: predict
# WHAT IT DOES: will provide the prediction for the provided video by splitting
#           it into frames, analyzing each frame, and then averaging the results
# RETURN: none
###############################################################################
def predict(file):
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)

    array = MODEL.predict(x)

    result = array[0]
    answer = np.argmax(result)

    score = 0

    if answer == variables.EXCELLENT_CAT_NUMBER:
        print("Excellent")
        score += 4

    elif answer == variables.EXTREMELY_OBSTRUCTED_CAT_NUMBER:
        print("Extremely Obstructed")
        score += 3

    elif answer == variables.GOOD_CAT_NUMBER:
        print("Good")
        score += 2

    elif answer == variables.POOR_CAT_NUMBER:
        print("Poor")
        score += 1

    return score

###############################################################################
# FUNCTION NAME: testCNN
# WHAT IT DOES: will test our CNN with the images in the provide file paths
# RETURN: none
###############################################################################
def testCNN():
    print("\n\n Moving excellent test files to training images pic directory\n\n")
    
    currentDir = ORIGINAL_PATH + variables.TEST_PATH
    videoArr = os.listdir(currentDir)
    testingVideosToFrames.changeDir(ORIGINAL_PATH)

    arrayLen = len( videoArr )

    score = 0

    if (arrayLen > 0):

        ################### ANALYZE EACH VIDEO FOR A SCORE ####################
        for video in range(arrayLen):

            testingVideosToFrames.dumpArr()
            videoFile = videoArr[ video ]

            print("\n\n Working on: \n\n")
            print("\t" + videoFile + "\n")

            testingVideosToFrames.changeDir(currentDir)

            frameRate = testingVideosToFrames.getFrameRate(videoFile, 18)
            testingVideosToFrames.getFrame(currentDir + videoFile, 0, frameRate, 1)

            imageArr = testingVideosToFrames.getFrameArray()
            testingVideosToFrames.changeDir(ORIGINAL_PATH)
            imageArrLen = len( imageArr )

            for frame in range(imageArrLen):
                imageOnlyArr = imageArr[frame]
                print(imageOnlyArr)

                os.chdir(ORIGINAL_PATH)
                score += predict(imageOnlyArr)
                os.chdir(ORIGINAL_PATH)
            
            video_dir_location = currentDir + videoFile


            ###################### AVERAGE VIDEO RESULTS ######################

            # GOOD #
            if(round(score/18) == 4):
                print(round(score/18))
                score = 0

                os.replace(video_dir_location, ORIGINAL_PATH + EXCELLENT_OUTPUT_PATH + videoFile)
                print("\n\n\nThe video," +videoFile +", has been classified as excellent\n\n\n")

            # EXTREMELY OBSTRUCTED #
            elif(round(score/18) == 3 or round(score/18) == 2 ):
                print(round(score/18))
                score = 0

                os.replace(video_dir_location, ORIGINAL_PATH + EXTREMELY_OBSTRUCTED_OUTPUT_PATH + videoFile)
                print("\n\n\nThe video," + videoFile + ", has been classified as extremely obstructed\n\n\n")
                
            # GOOD #
            elif(round(score/18) == 1 ):
                print(round(score/18))
                score = 0

                os.replace(video_dir_location, ORIGINAL_PATH + GOOD_OUTPUT_PATH + videoFile)
                print("\n\n\nThe video," + videoFile + ", has been classified as good\n\n\n")
            
            # POOR #
            else:
                score = 0

                os.replace(video_dir_location, ORIGINAL_PATH + POOR_OUTPUT_PATH + videoFile)
                print("\n\n\nThe video," + videoFile + ", has been classified as poor\n\n\n")

    #testingVideosToFrames.getAllImagesNotDeleted(videoArr, currentDir)
    testingVideosToFrames.deleteFiles(currentDir)
    return 0

# testCNN()