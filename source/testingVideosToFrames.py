###############################################################################
# AUTHOR: Keenan Swanson
#
# EDITOR: Samantha Muellner
#
# DESCRIPTION: file that will split videos into frames, save them in an array
#           for easy access, and delete the array when necessary
#
# VERSION: 1.0.0
###############################################################################
import cv2, os
import variables

# declare variables
COUNT = 0
SEC = 0
vidLen = 0
EXPECTED_FRAMES = variables.EXPECTED_FRAMES
FRAME_ARRAY = []

originalDir = os.getcwd()


###############################################################################
# FUNCTION NAME: changeDir
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def changeDir( directory ):
    os.chdir( directory )


###############################################################################
# FUNCTION NAME: getVidName
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def getVidName( videoFile ):
    string = videoFile
    strArr = string.split('.')
    string = strArr[0]
    return string


###############################################################################
# FUNCTION NAME: getVidDuration
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def getVidDuration( videoFile ):
    video = cv2.VideoCapture( videoFile )
    fps = video.get(cv2.CAP_PROP_FPS)
    framesCOUNT = video.get(cv2.CAP_PROP_FRAME_COUNT)
    length = 0
    if(fps == 0):
        length = 0
    else:
        length = int(framesCOUNT/fps)
    return length

#vidLen = getVidDuration( '1179_20180822_155018.mp4' )


###############################################################################
# FUNCTION NAME: getFrame
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def getFrame(videoFile, seconds, fr, counts):
     COUNT = 0#, vidLen
     SEC = 0
     COUNT += counts
     SEC += seconds
     vid = cv2.VideoCapture( videoFile )
     vidName = getVidName( videoFile )
    
     if SEC > getVidDuration(videoFile):
         return print("The video has been divided into frames")
    
     if fr == 0:
         fr = getVidDuration(videoFile)/30
         fr = round(fr,2)
         print("The frame rate is %d\n", fr)
    
     vid.set(cv2.CAP_PROP_POS_MSEC, SEC*1000)
     success,image = vid.read()
    
     if success:
         cv2.imwrite(vidName  +  "_frame_" + str(COUNT) + ".jpg", image) # save frame as JPG file
         FRAME_ARRAY.append(vidName +  "_frame_" + str(COUNT) + ".jpg")
         print(SEC)

         SEC += fr
         SEC = round(SEC,2)

         COUNT += 1
         
     return getFrame( videoFile, SEC, fr, COUNT)


###############################################################################
# FUNCTION NAME: getFrameArray
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def getFrameArray():
    return FRAME_ARRAY


###############################################################################
# FUNCTION NAME: dumpArr 
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def dumpArr():

    while len(FRAME_ARRAY) > 0:
        FRAME_ARRAY.pop()


###############################################################################
# FUNCTION NAME: deleteFiles
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def deleteFiles( directory ):
    os.chdir( directory )

    arrayOfImages = os.listdir( directory )

    for file in range(len(arrayOfImages)):
        fileName = arrayOfImages[file]
        os.remove(fileName)

    os.chdir(originalDir)
    dumpArr()
    
    
###############################################################################
# FUNCTION NAME: getAllImagesNotDeleted
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def getAllImagesNotDeleted( array, directory ):
    files = os.listdir( directory )

    print(files)
    for file in range(len(files)):
        fileName = files[file]
        os.remove(fileName)
    os.chdir(originalDir)


###############################################################################
# FUNCTION NAME:  getFrameRate
# WHAT IT DOES:  
# RETURN:  
###############################################################################
def getFrameRate( videoFile, EXPECTED_FRAMES):
    if(EXPECTED_FRAMES > 0):
        return getVidDuration(videoFile)/EXPECTED_FRAMES
    else:
        return getVidDuration(videoFile)/9 #WE WILL MAKE 9 DEFAULT

#frameRate = vidLen/EXPECTED_FRAMES

#getFrame( '1179_20180822_155018.mp4' , SEC, getFrameRate("1179_20180822_155018.mp4",18))
#print(FRAME_ARRAY)