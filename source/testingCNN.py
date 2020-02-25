"""
AUTHOR: Samantha Muellner, Keenan Swanson

DESCRIPTION: script that will test our unknown videos against the saved CNN model

VERSION: 2.0.1v
"""

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

originalPath = os.getcwd()
import videoToFrames

model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
#test_path = './dataset/test2/single_prediction'
test_path = './dataset/predictions'

model = load_model(model_path)
model.load_weights(model_weights_path)

img_width, img_height = 50, 50

EXCELLENT = 0
EXTREMELY_OBSTRUCTED = 1
GOOD = 2
POOR = 3




def predict(file):
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)

    array = model.predict(x)

    result = array[0]
    answer = np.argmax(result)

    score = 0

    if answer == EXCELLENT:
        print("Excellent")
        score += 4

    elif answer == EXTREMELY_OBSTRUCTED:
        print("Extremely Obstructed")
        score += 0

    elif answer == GOOD:
        print("Good")
        score += 3

    elif answer == POOR:
        print("Poor")
        score += 1

    return score

def somethingForPrediction():
    print("\n\n Moving excellent test files to training images pic directory\n\n")

    videoArr = os.listdir(originalPath+"./dataset/testing_set")
    currentDir = originalPath+"./dataset/testing_set/"
    videoToFrames.changeDir(originalPath)

    arrayLen = len( videoArr )

    score = 0

    if (arrayLen > 0):

        for video in range(arrayLen):

            videoToFrames.dumpArr()
            videoFile = videoArr[ video ]

            print("\n\n Working on: \n\n")
            print("\t"+videoFile+"\n")

            videoToFrames.changeDir(currentDir)

            frameRate = videoToFrames.getFrameRate(videoFile, 18)
            videoToFrames.getFrame(currentDir+videoFile, 0, frameRate, 1)

            imageArr = videoToFrames.getFrameArray()
            videoToFrames.changeDir(originalPath)
            imageArrLen = len( imageArr )

            for frame in range(imageArrLen):
                #path = str(pathlib.Path().absolute())
                imageOnlyArr = imageArr[frame]
                print(imageOnlyArr)

                os.chdir(originalPath)
                score += predict(imageOnlyArr)
                os.chdir(originalPath)


            if(round(score/18) == 4):
                print(round(score/18))
                score = 0

                os.replace(currentDir+videoFile, originalPath + "/output/Excellent/" + videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as excellent\n\n\n")

            elif(round(score/18) == 3 or round(score/18) == 2 ):
                print(round(score/18))
                score = 0

                os.replace(currentDir+videoFile, originalPath + "/output/Good_to_Fair/" + videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as good\n\n\n")

            elif(round(score/18) == 1 ):
                print(round(score/18))
                score = 0

                os.replace(currentDir+videoFile, originalPath + "/output/Poor/" + videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as poor\n\n\n")
                
            else:
                score = 0

                os.replace(currentDir+videoFile, originalPath + "/output/Extremely_Obstructed/" + videoFile)
                print("\n\n\nThe video," + videoFile + ", has been classified as extremely obstructed\n\n\n")

    #videoToFrames.getAllImagesNotDeleted(videoArr, currentDir)
    videoToFrames.deleteFiles(currentDir)
    return 0