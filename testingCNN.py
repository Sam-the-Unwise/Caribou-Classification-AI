import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import xlrd

originalPath = os.getcwd()
import VideoToFrames

model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
#test_path = './dataset/test2/single_prediction'
test_path = './dataset/predictions'

model = load_model(model_path)
model.load_weights(model_weights_path)

img_width, img_height = 50, 50

direc = originalPath+"\ExcelSheet\CaribouVideoProcessing_10899Responses_20191210.xlsx"
workbook = xlrd.open_workbook(direc)
sheet = workbook.sheet_by_index(0)

excellentCount = 0
goodCount = 0
poorCount = 0
extremelyObsCount = 0

EXCELLENT_CONST = "EXCELLENT"
GOOD_CONST = "FAIR to GOOD"
POOR_CONST = "POOR"
EXTREMELY_OBS_CONST = "EXTREMELY OBSTRUCTED"
incorrectArr = []


def resetCounts():
    global excellentCount, goodCount, poorCount, extremelyObsCount
    excellentCount = 0
    goodCount = 0
    poorCount = 0
    extremelyObsCount = 0

def predict(file):
    global excellentCount, goodCount, poorCount, extremelyObsCount
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    answer = np.argmax(result)
    score = 0
    
    if answer == 0:
        #print("Predicted Dog Eating")
        score += 4
        excellentCount = excellentCount + 1
        print("Excellent\n\n")
    elif answer == 1:
        #print("Predicted dog running")
        score += 0
        extremelyObsCount = extremelyObsCount + 1
        print("Extremely Obstructed\n\n")
    elif answer == 2:
        #print("Predicted dog sitting")
        score +=2
        goodCount = goodCount + 1
        print("Fair\n\n")
    elif answer == 3:
        #print("Predicted dog sleeping")
        score+=3
        goodCount = goodCount + 1
        print("Good\n\n")
            
    elif answer == 4:
        print("Poor\n\n")
        poorCount = poorCount + 1
        score+=1
    else:
        print("Unable to predict specimen. Need further training")
        
    return score

def getRowOfExcel( videoName ):
    vidNameArr = videoName.split(".")
    newVidName = vidNameArr[0]
    row = 0
    while( newVidName != sheet.cell_value( row, 0 )):
        row += 1
    return row

def getQuality( row ):
    global sheet
    vidQual = sheet.cell_value( row, 7 )
    return vidQual

def printWeights( numberOfImages ):
    print("\nWeight of excellent is ",(excellentCount/numberOfImages),"\n")
    print("Weight of extremely obstructed is ",(extremelyObsCount/numberOfImages),"\n")
    print("Weight of good is ",(goodCount/numberOfImages),"\n")
    print("Weight of poor is ",(poorCount/numberOfImages),"\n")
    
    
def getLargestWeight():
    weightArr=[excellentCount/18,extremelyObsCount/18,goodCount/18,poorCount/18]
    maxNum = max(weightArr)
    weightDict = {excellentCount/18:"excellentWeight", 
                  extremelyObsCount/18:"extremelyObsWeight", 
                  goodCount/18:"goodWeight", 
                  poorCount/18:"poorWeight"}
    return weightDict[maxNum]
        
    

def somethingForPrediction():
    print("\n\n Moving excellent test files to training images pic directory\n\n")
    videoArr = os.listdir(originalPath+"/dataset/testing_set")
    arrayLen = len( videoArr )
    score = 0
    VideoToFrames.changeDir(originalPath)
    currentDir = originalPath+"/dataset/testing_set/"
    if (arrayLen > 0):    
        for video in range(arrayLen):
            VideoToFrames.dumpArr()
            videoFile = videoArr[ video ]
            print("\n\n Working on: \n\n")
            print("\t"+videoFile+"\n")
            VideoToFrames.changeDir(currentDir)
            frameRate = VideoToFrames.getFrameRate(videoFile, 18)
            VideoToFrames.getFrame(currentDir+videoFile, frameRate, frameRate, 1)
            imageArr = VideoToFrames.getFrameArray()
            VideoToFrames.changeDir(originalPath)
            imageArrLen = len( imageArr )
            for frame in range(imageArrLen):
                #path = str(pathlib.Path().absolute())
                imageOnlyArr = imageArr[frame]
                #print(imageOnlyArr)
                print("frame "+str(frame)+":\n\r")
                os.chdir(originalPath)
                score += predict(imageOnlyArr)
                os.chdir(originalPath)
                
            try:   
                expectedQuality = getQuality(getRowOfExcel(videoFile))
                print("The expected quality is: "+ expectedQuality + "\n")
            except:
                print("The video is not in the excel sheet.\n")

                
      
            if(round(score/18 == 4)):#getLargestWeight() == "excellentWeight"):
                print(round(score/18))
                printWeights(18)
                resetCounts()
                score = 0
                if( expectedQuality != EXCELLENT_CONST ):
                    incorrectArr.append(videoFile)
                os.replace(currentDir+videoFile, originalPath+"/output/Excellent/"+videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as excellent\n\n\n")
            elif(round(score/18) == 3 or round(score/18) == 2):#getLargestWeight() == "goodWeight"):
                printWeights(18)
                resetCounts()
                score = 0
                if( expectedQuality != GOOD_CONST ):
                    incorrectArr.append(videoFile)
                os.replace(currentDir+videoFile, originalPath+"/output/Good_to_Fair/"+videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as good\n\n\n")
           
            elif(round(score/18) == 1):#getLargestWeight() == "poorWeight"):
                print(round(score/18))
                printWeights(18)
                resetCounts()
                score = 0
                if( expectedQuality != POOR_CONST ):
                    incorrectArr.append(videoFile)
                os.replace(currentDir+videoFile, originalPath+"/output/Poor/"+videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as poor\n\n\n")
            else:
                printWeights(18)
                resetCounts()
                score = 0
                if( expectedQuality != EXTREMELY_OBS_CONST ):
                    incorrectArr.append(videoFile)
                os.replace(currentDir+videoFile, originalPath+"/output/Extremely_Obstructed/"+videoFile)
                print("\n\n\nThe video,"+videoFile+", has been classified as extremely obstructed\n\n\n")
            
            
    #VideoToFrames.getAllImagesNotDeleted(videoArr, currentDir)
    print("The files that were incorrect are \n\n", incorrectArr)
    VideoToFrames.deleteFiles(currentDir)
    return 0
            
somethingForPrediction() 