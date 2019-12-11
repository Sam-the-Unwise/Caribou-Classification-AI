# Importing the Keras libraries and packages
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from keras.layers.core import Flatten, Dropout, Lambda
from keras.preprocessing.image import ImageDataGenerator
import math
from keras.optimizers import Adam
import tensorflow as tf

import numpy as np
import os
import math
import random

TRAIN_BATCH_SIZE = 3000
TEST_BATCH_SIZE = 100
EPOCH_SIZE = 25

IMAGE_DIMENSION_X = 50
IMAGE_DIMENSION_Y = 50


# #amount of files in training set
# train_len = 350

# #amount of files in test set
# test_len = 100



# Initialising the CNN
classifier = Sequential()

# # Step 1 - Convolution
#classifier.add(Conv2D(36, (3, 3), input_shape = (IMAGE_DIMENSION_X, IMAGE_DIMENSION_Y, 3), activation = 'relu'))
classifier.add(Conv2D(3, (1, 1), input_shape = (IMAGE_DIMENSION_X, IMAGE_DIMENSION_Y, 3), activation = 'relu'))

# # Step 2 - Pooling
# classifier.add(MaxPooling2D(pool_size = (4, 4)))

# # Adding a second convolutional layer
# classifier.add(Conv2D(36, (3, 3), activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (4, 4)))

# # Adding a third convolutional layer
# classifier.add(Conv2D(36, (3, 3), activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (4, 4)))

# # Adding a fourth convolutional layer
# classifier.add(Conv2D(36, (3, 3), activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (4, 4)))


#classifier.add(Conv2D(3, (1, 1), activation='relu'))
classifier.add(Conv2D(12, (5, 5), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Conv2D(16, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Conv2D(24, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
classifier.add(Conv2D(48, (3, 3), activation='relu'))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(4, activation = 'softmax'))


# classifier.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape = INPUT_SHAPE))
# ........
# classifier.add(Flatten())
# classifier.add(Dropout(dropout))
# classifier.add(Dense(64, activation = 'relu'))
# classifier.add(Dropout(dropout))
# classifier.add(Dense(32, activation = 'relu'))
# classifier.add(Dropout(dropout))
# classifier.add(Dense(1))


# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Part 2 - Fitting the CNN to the images

train_datagen = ImageDataGenerator(rescale = None, #= 1./255,
                                    shear_range = 0.2,
                                    zoom_range = 0.2,
                                    horizontal_flip = True)
                                    
test_datagen = ImageDataGenerator(rescale = None)#1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                   target_size = (IMAGE_DIMENSION_X, IMAGE_DIMENSION_Y),
                                                   batch_size = 64,
                                                   class_mode = 'categorical')


test_set = test_datagen.flow_from_directory('dataset/test_set',
                                           target_size = (IMAGE_DIMENSION_X, IMAGE_DIMENSION_Y),
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

target_dir = 'models/'

classifier.save('models/model.h5')
classifier.save_weights('models/weights.h5')