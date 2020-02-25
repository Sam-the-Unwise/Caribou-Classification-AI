"""
AUTHOR: Samantha Muellner, Keenan Swanson

DESCRIPTION: script that will test our unknown videos against the saved CNN MODEL

VERSION: 2.0.1v
"""

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import testingVideosToFrames

# define variables
ORIGINAL_PATH = os.getcwd()

MODEL_PATH = './models/model.h5'
MODEL_WEIGHTS_PATH = './models/weights.h5'
TEST_PATH = "./dataset/testing_set"


EXCELLENT_OUTPUT_PATH = "./dataset/output/Excellent"
EXTREMELY_OBSTRUCTED_OUTPUT_PATH = "./dataset/output/Extremely_Obstructed"
GOOD_OUTPUT_PATH = "./dataset/output/Good_to_Fair"
POOR_OUTPUT_PATH = "./dataset/output/Poor"




MODEL = load_model(MODEL_PATH).load_weights(MODEL_WEIGHTS_PATH) # load our model


img_width, img_height = 50, 50

EXCELLENT = 0
EXTREMELY_OBSTRUCTED = 1
GOOD = 2
POOR = 3


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

    if answer == EXCELLENT:
        print("Excellent")
        score += 4

    elif answer == EXTREMELY_OBSTRUCTED:
        print("Extremely Obstructed")
        score += 3

    elif answer == GOOD:
        print("Good")
        score += 2

    elif answer == POOR:
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
    
    currentDir = ORIGINAL_PATH + TEST_PATH
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