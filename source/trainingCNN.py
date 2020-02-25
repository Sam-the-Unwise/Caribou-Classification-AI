###############################################################################
# AUTHOR: Samantha Muellner, Keenan Swanson
#
# DESCRIPTION: will train our CNN using the video frames in the provided 
#                   folder paths
#
# VERSION: 4.2.2v
###############################################################################

# Importing the Keras libraries and packages
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from keras.layers.core import Flatten, Dropout, Lambda
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
import tensorflow as tf

import numpy as np
import os
import math
import random

def trainAndValidateCNN():
    # declare variables
    ORIGINAL_PATH = os.getcwd()

    TRAIN_BATCH_SIZE = 5225
    TEST_BATCH_SIZE = 1653
    EPOCH_SIZE = 1

    IMAGE_X_DIM = 50
    IMAGE_Y_DIM = 50
    IMAGE_X_DIM = 50
    IMAGE_Y_DIM = 50

    TRAINING_SET_FRAMES_PATH = './dataset/training_set_frames/'
    VALIDATION_SET_FRAMES_PATH = './dataset/validation_set_frames/'

    TARGET_DIR = './models/' # declare where to save our model and weights

    classifier = Sequential()


    ########################## Part 1 - Set up the CNN ############################

    ###### STEP 1 - CONVOLUTION #######
    classifier.add(Conv2D(3, 
                        (1, 1), 
                        input_shape = (IMAGE_X_DIM, IMAGE_Y_DIM, 3), 
                        activation = 'relu'))

    ####### STEP 2 - ADD LAYERS #######
    classifier.add(Conv2D(12, (5, 5), activation='relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Conv2D(16, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Conv2D(24, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Conv2D(48, (3, 3), activation='relu'))

    ####### STEP 3 - FLATTENING ######
    classifier.add(Flatten())

    ##### STEP 4 - FULLY CONNECT #####
    classifier.add(Dense(units = 128, activation = 'relu'))
    classifier.add(Dense(5, activation = 'softmax'))

    # compile the CNN
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])




    ################### Part 2 - Fitting the CNN to the images ####################
    train_datagen = ImageDataGenerator(rescale = None, #= 1./255,
                                        shear_range = 0.2,
                                        zoom_range = 0.2,
                                        horizontal_flip = True)

    test_datagen = ImageDataGenerator(rescale = None)#1./255)

    # declare our paths
    training_path = ORIGINAL_PATH + TRAINING_SET_FRAMES_PATH
    validation_path = ORIGINAL_PATH + VALIDATION_SET_FRAMES_PATH

    # get training set
    training_set = train_datagen.flow_from_directory(training_path,
                                        target_size = (IMAGE_X_DIM, IMAGE_Y_DIM),
                                        batch_size = 64,
                                        class_mode = 'categorical')

    # get validation set
    test_set = test_datagen.flow_from_directory(validation_path,
                                        target_size = (IMAGE_X_DIM, IMAGE_Y_DIM),
                                        batch_size = 64,
                                        class_mode = 'categorical')

    #we want to avoid over fitting because that gives false accuracy
    #   than normally is shown if accuracy is far off from val_accuracy.
    #   The real accuracy is about when the accuracy and val accuracy converge.
    classifier.fit_generator(training_set,
                                #NOTE==========Mess with batch sizes to find best accuracy
                                steps_per_epoch = TRAIN_BATCH_SIZE, #train_len//TRAIN_BATCH_SIZE
                                #mess around with epochs to find a better accuracy
                                epochs = EPOCH_SIZE,
                                validation_data = test_set,
                                validation_steps = TEST_BATCH_SIZE) 

    classifier.save(TARGET_DIR + 'model.h5')
    classifier.save_weights(TARGET_DIR + 'weights.h5')