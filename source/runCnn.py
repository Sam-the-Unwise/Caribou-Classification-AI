from organizingTrainAndValidation import organizeVideos
from splitVideosIntoFrames import splitVideos
from trainingCNN import trainAndValidateCNN
from testingCNN import testCNN
# import code that will delete the videos

###############################################################################
# FUNCTION NAME: main
# WHAT IT DOES: main function and file for our CNN -- will perform all the 
#           necessary tasks needed in order to properly run our CNN
# RETURN: none
###############################################################################
def main():
    organizeVideosBoolean = input("Do videos need to be organized: (y or n)")

    if organizeVideosBoolean == 'y':
        organizeVideos()
    
    splitVideosBoolean = input("Do videos need to be split into frames: (y or n)")

    if splitVideosBoolean == 'y':
        splitVideos()
    
    trainAndValidateCNN()
    testCNN()