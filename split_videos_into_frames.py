"""
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
Usage

Open the split_v1.4.py and edit the path to the video. Then run:
$ python split_v1.4.py -i directory_path

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
"""
import cv2
import os
# Regular expression package
import re
# the package helps us parse and access our command line arguments.
import argparse

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')


def splitFrame( videoPath, sec):
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
        fileName = "D:/Desktop-New/Video_split_test/data/" + videoName + "_Frame" + str(countFrame) + '.jpg'
        print('Creating... ' + fileName)

        # save frame as JPG file
        cv2.imwrite(fileName, frame)

        # To stop duplicate images
        sec += frameInterval
        countFrame += 1

    # When everything done, release the capture
    vidCap.release()
    cv2.destroyAllWindows()


# get a list of all file names
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


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

# We must specify shorthand and longhand versions ( -i  and --input )
# where either flag could be used in the command line.
# This is a required argument as is noted by required=True
ap.add_argument("-i", "--input", required = True, help = "path to input video")
ap.add_argument("-o", "--output", required = False, help = "path to output image")

# turn the parsed command line arguments into a Python dictionary
args = vars((ap.parse_args()))

# get videos from inputPath and store them in fileStorage
inputPath = args["input"]
fileStorage = getAllFile( inputPath )

for file in fileStorage:
    splitFrame( file, 1 )


# Reference: https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/
