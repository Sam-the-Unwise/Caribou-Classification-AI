"""
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
Usage

Open the split_v1.4.py and edit the path to the video. Then run:
$ python split_v1.4.py -i directory_path

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
"""
import cv2, os
import re # Regular expression package
import argparse # the package helps us parse and access our command line arguments.
import variables


# decalre variables and paths
INPUT_PATH_TRAINING = variables.INPUT_TRAINING_PATH
INPUT_PATH_VALIDATION = variables.INPUT_VALIDATION_PATH
#INPUT_PATH_TEST = "../dataset/testing_set/"

OUTPUT_PATH_TRAINING = variables.OUTPUT_TRAINING_PATH
OUTPUT_PATH_VALIDATION = variables.OUTPUT_VALIDATION_PATH
#INPUT_PATH_TEST = "../dataset/testing_set_frames/"

PATH_EXCELLENT = variables.EXCELLENT_FOLDER
PATH_GOOD = variables.GOOD_FOLDER
PATH_POOR = variables.POOR_FOLDER
PATH_EXTREMELY_OBSTRUCTED = variables.EXTREMELY_OBSTRUCTED_FOLDER

# create parameters that will tell the splitFrames function how many seconds to
#   wait before splitting another frame from the video
SECONDS = 1


###############################################################################
# FUNCTION NAME: splitFrame
# WHAT IT DOES: goes into the given video and separates it into frames based
#       on the amount of seconds give, then subsequently saves it to 
#       outerVideopath
# RETURN: none
###############################################################################
def splitFrame(videoPath, outerVideoPath, sec):
    vidCap = cv2.VideoCapture( videoPath )
    baseVideoPath = os.path.basename( videoPath )

    # Gets the prefix of the file name
    videoName = re.search(r'(.+?)\.', baseVideoPath).group(1)
    frameInterval = sec

    # initialize the countFrame as 0
    countFrame = 0
    success = True

    while success:
        # capture a frame per second
        vidCap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)

        # Grabs, decodes and returns the next video frame.
        # return True/False to the first parm if frames has been grabbed
        # returns the just grabbed frame to the second parm if frames grabbed,
        #  otherwise returns empty image
        success, frame = vidCap.read()

        # avoid cv2.error: !_img.empty() in function
        if not success:
            # When everything done, release the capture
            vidCap.release()
            cv2.destroyAllWindows()
            break

        # write the file name
        file_name = outerVideoPath + videoName + "_frame" + str(countFrame) + '.jpg'
        print('Creating... ' + file_name)
        
        # save frame as JPG file
        cv2.imwrite(file_name, frame)

        # To stop duplicate images
        sec += frameInterval
        countFrame += 1

    # When everything done, release the capture
    vidCap.release()
    cv2.destroyAllWindows()


###############################################################################
# FUNCTION NAME: getAllFiles
# WHAT IT DOES: get all the files in the given file path
# RETURN: none
###############################################################################
def getAllFile( path ):
    # initialize list to store path and name of all files
    allPath = []

    #  get the list of all files and directories in the specified directory
    fileList = os.listdir(path)

    for file in fileList:
        filePath = os.path.join(path, file)

        # append file names to the list
        allPath.append(filePath)

    return allPath


###############################################################################
# FUNCTION NAME: checkAllDirectories
# WHAT IT DOES: check that all the directories needed to be used in this
#       program
# RETURN: none
###############################################################################
def checkAllDirectories():
    
    ###################### CHECK TRAINING SET LOCATIONS ######################
    try:
        if not os.path.exists(INPUT_PATH_TRAINING):
            os.makedirs(INPUT_PATH_TRAINING)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_TRAINING)

    try:
        if not os.path.exists(INPUT_PATH_TRAINING + PATH_EXCELLENT):
            os.makedirs(INPUT_PATH_TRAINING + PATH_EXCELLENT)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_TRAINING + PATH_EXCELLENT)

    try:
        if not os.path.exists(INPUT_PATH_TRAINING + PATH_GOOD):
            os.makedirs(INPUT_PATH_TRAINING + PATH_GOOD)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_TRAINING + PATH_GOOD)

    try:
        if not os.path.exists(INPUT_PATH_TRAINING + PATH_POOR):
            os.makedirs(INPUT_PATH_TRAINING + PATH_POOR)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_TRAINING + PATH_POOR)

    try:
        if not os.path.exists(INPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED):
            os.makedirs(INPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED)

    # check training set frame locations

    try:
        if not os.path.exists(OUTPUT_PATH_TRAINING):
            os.makedirs(OUTPUT_PATH_TRAINING)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_TRAINING)

    try:
        if not os.path.exists(OUTPUT_PATH_TRAINING + PATH_EXCELLENT):
            os.makedirs(OUTPUT_PATH_TRAINING + PATH_EXCELLENT)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_TRAINING + PATH_EXCELLENT)

    try:
        if not os.path.exists(OUTPUT_PATH_TRAINING + PATH_GOOD):
            os.makedirs(OUTPUT_PATH_TRAINING + PATH_GOOD)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_TRAINING + PATH_GOOD)

    try:
        if not os.path.exists(OUTPUT_PATH_TRAINING + PATH_POOR):
            os.makedirs(OUTPUT_PATH_TRAINING + PATH_POOR)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_TRAINING + PATH_POOR)

    try:
        if not os.path.exists(OUTPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED):
            os.makedirs(OUTPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED)
    except OSError:
        print('Error: Creating directory of ' + 
                            OUTPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED)


    ###################### CHECK VALIDATION SET LOCATIONS #####################
    
    try:
        if not os.path.exists(INPUT_PATH_VALIDATION):
            os.makedirs(INPUT_PATH_VALIDATION)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_VALIDATION)

    try:
        if not os.path.exists(INPUT_PATH_VALIDATION + PATH_EXCELLENT):
            os.makedirs(INPUT_PATH_VALIDATION + PATH_EXCELLENT)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_VALIDATION + PATH_EXCELLENT)

    try:
        if not os.path.exists(INPUT_PATH_VALIDATION + PATH_GOOD):
            os.makedirs(INPUT_PATH_VALIDATION + PATH_GOOD)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_VALIDATION + PATH_GOOD)

    try:
        if not os.path.exists(INPUT_PATH_VALIDATION + PATH_POOR):
            os.makedirs(INPUT_PATH_VALIDATION + PATH_POOR)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_VALIDATION + PATH_POOR)

    try:
        if not os.path.exists(INPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED):
            os.makedirs(INPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED)
    except OSError:
        print('Error: Creating directory of ' + INPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED)

    # check training set frame locations

    try:
        if not os.path.exists(OUTPUT_PATH_VALIDATION):
            os.makedirs(OUTPUT_PATH_VALIDATION)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_VALIDATION)

    try:
        if not os.path.exists(OUTPUT_PATH_VALIDATION + PATH_EXCELLENT):
            os.makedirs(OUTPUT_PATH_VALIDATION + PATH_EXCELLENT)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_VALIDATION + PATH_EXCELLENT)

    try:
        if not os.path.exists(OUTPUT_PATH_VALIDATION + PATH_GOOD):
            os.makedirs(OUTPUT_PATH_VALIDATION + PATH_GOOD)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_VALIDATION + PATH_GOOD)

    try:
        if not os.path.exists(OUTPUT_PATH_VALIDATION + PATH_POOR):
            os.makedirs(OUTPUT_PATH_VALIDATION + PATH_POOR)
    except OSError:
        print('Error: Creating directory of ' + OUTPUT_PATH_VALIDATION + PATH_POOR)

    try:
        if not os.path.exists(OUTPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED):
            os.makedirs(OUTPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED)
    except OSError:
        print('Error: Creating directory of ' + 
                            OUTPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED)

    # ####################### CHECK TESTING SET LOCATIONS #######################

    # try:
    #     if not os.path.exists(INPUT_PATH_TESTING):
    #         os.makedirs(INPUT_PATH_TESTING)
    # except OSError:
    #     print('Error: Creating directory of ' + INPUT_PATH_TESTING)

    # try:
    #     if not os.path.exists(INPUT_PATH_TESTING + PATH_EXCELLENT):
    #         os.makedirs(INPUT_PATH_TESTING + PATH_EXCELLENT)
    # except OSError:
    #     print('Error: Creating directory of ' + INPUT_PATH_TESTING + PATH_EXCELLENT)

    # try:
    #     if not os.path.exists(INPUT_PATH_TESTING + PATH_GOOD):
    #         os.makedirs(INPUT_PATH_TESTING + PATH_GOOD)
    # except OSError:
    #     print('Error: Creating directory of ' + INPUT_PATH_TESTING + PATH_GOOD)

    # try:
    #     if not os.path.exists(INPUT_PATH_TESTING + PATH_POOR):
    #         os.makedirs(INPUT_PATH_TESTING + PATH_POOR)
    # except OSError:
    #     print('Error: Creating directory of ' + INPUT_PATH_TESTING + PATH_POOR)

    # try:
    #     if not os.path.exists(INPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED):
    #         os.makedirs(INPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED)
    # except OSError:
    #     print('Error: Creating directory of ' + INPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED)

    # # check training set frame locations

    # try:
    #     if not os.path.exists(OUTPUT_PATH_TESTING):
    #         os.makedirs(OUTPUT_PATH_TESTING)
    # except OSError:
    #     print('Error: Creating directory of ' + OUTPUT_PATH_TESTING)

    # try:
    #     if not os.path.exists(OUTPUT_PATH_TESTING + PATH_EXCELLENT):
    #         os.makedirs(OUTPUT_PATH_TESTING + PATH_EXCELLENT)
    # except OSError:
    #     print('Error: Creating directory of ' + OUTPUT_PATH_TESTING + PATH_EXCELLENT)

    # try:
    #     if not os.path.exists(OUTPUT_PATH_TESTING + PATH_GOOD):
    #         os.makedirs(OUTPUT_PATH_TESTING + PATH_GOOD)
    # except OSError:
    #     print('Error: Creating directory of ' + OUTPUT_PATH_TESTING + PATH_GOOD)

    # try:
    #     if not os.path.exists(OUTPUT_PATH_TESTING + PATH_POOR):
    #         os.makedirs(OUTPUT_PATH_TESTING + PATH_POOR)
    # except OSError:
    #     print('Error: Creating directory of ' + OUTPUT_PATH_TESTING + PATH_POOR)

    # try:
    #     if not os.path.exists(OUTPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED):
    #         os.makedirs(OUTPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED)
    # except OSError:
    #     print('Error: Creating directory of ' + 
    #                         OUTPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED)




###############################################################################
# FUNCTION NAME: main
# WHAT IT DOES: runs all our previously declared functions
# RETURN: none
###############################################################################
def main():
    checkAllDirectories()
    
    ######################### GET TRAINING SET FRAMES #########################
    train_file_storage_excellent = getAllFile(INPUT_PATH_TRAINING + PATH_EXCELLENT)
    train_file_storage_good = getAllFile(INPUT_PATH_TRAINING + PATH_GOOD)
    train_file_storage_poor = getAllFile(INPUT_PATH_TRAINING + PATH_POOR)
    train_file_storage_extremely_obstructed = getAllFile(INPUT_PATH_TRAINING + PATH_EXTREMELY_OBSTRUCTED)

    for excellent_file in train_file_storage_excellent:
        splitFrame(excellent_file, OUTPUT_PATH_VALIDATION + PATH_EXCELLENT, SECONDS)

    for good_file in train_file_storage_good:
        splitFrame(good_file, OUTPUT_PATH_VALIDATION + PATH_GOOD, SECONDS)

    for poor_file in train_file_storage_poor:
        splitFrame(poor_file, OUTPUT_PATH_VALIDATION + PATH_POOR, SECONDS)

    for extremely_ob_file in train_file_storage_extremely_obstructed:
        splitFrame(extremely_ob_file, OUTPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED, SECONDS)


    ######################## GET VALIDATION SET FRAMES ########################
    val_file_storage_excellent = getAllFile(INPUT_PATH_VALIDATION + PATH_EXCELLENT)
    val_file_storage_good = getAllFile(INPUT_PATH_VALIDATION + PATH_GOOD)
    val_file_storage_poor = getAllFile(INPUT_PATH_VALIDATION + PATH_POOR)
    val_file_storage_extremely_obstructed = getAllFile(INPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED)


    for excellent_file in val_file_storage_excellent:
        splitFrame(excellent_file, OUTPUT_PATH_VALIDATION + PATH_EXCELLENT, SECONDS)

    for good_file in val_file_storage_good:
        splitFrame(good_file, OUTPUT_PATH_VALIDATION + PATH_GOOD, SECONDS)

    for poor_file in val_file_storage_poor:
        splitFrame(poor_file, OUTPUT_PATH_VALIDATION + PATH_POOR, SECONDS)

    for extremely_ob_file in val_file_storage_extremely_obstructed:
        splitFrame(extremely_ob_file, OUTPUT_PATH_VALIDATION + PATH_EXTREMELY_OBSTRUCTED, SECONDS)



    # ######################### GET TESTING SET FRAMES ##########################
    # test_file_storage_excellent = getAllFile(INPUT_PATH_TESTING + PATH_EXCELLENT)
    # test_file_storage_good = getAllFile(INPUT_PATH_TESTING + PATH_GOOD)
    # test_file_storage_poor = getAllFile(INPUT_PATH_TESTING + PATH_POOR)
    # test_file_storage_extremely_obstructed = getAllFile(INPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED)


    # for excellent_file in test_file_storage_excellent:
    #     splitFrame(excellent_file, OUTPUT_PATH_TESTING + PATH_EXCELLENT, SECONDS)

    # for good_file in test_file_storage_good:
    #     splitFrame(good_file, OUTPUT_PATH_TESTING + PATH_GOOD, SECONDS)

    # for poor_file in test_file_storage_poor:
    #     splitFrame(poor_file, OUTPUT_PATH_TESTING + PATH_POOR, SECONDS)

    # for extremely_ob_file in test_file_storage_extremely_obstructed:
    #     splitFrame(extremely_ob_file, OUTPUT_PATH_TESTING + PATH_EXTREMELY_OBSTRUCTED, SECONDS)


main()





# Reference: https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/
