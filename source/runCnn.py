###############################################################################
# AUTHOR: Samantha Muellner
#
# DESCRIPTION: main file that will run all our otherfiles as needed in order
#           to fully train, validate, and test the CNN
#               - file will also be able to organize videos and split them into
#                   frames if need be
#
# VERSION: 4.2.3v
###############################################################################
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

    # only organize videos into training and validation set if needed
    if organizeVideosBoolean == 'y':
        organizeVideos()
    
    splitVideosBoolean = input("Do videos need to be split into frames: (y or n)")

    # only split files up if needed
    if splitVideosBoolean == 'y':
        splitVideos()
    
    trainAndValidateCNN()
    testCNN()