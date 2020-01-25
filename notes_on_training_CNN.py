<<<<<<< Updated upstream
'''THIS FILE CONTAINS THE CODE THAT WE ARE BASING OUR CODE OFF OF'''


# Importing the Keras libraries and packages
=======
'''THIS PAGE CONTAINS THE BASE CODE THAT WE ARE TRYING TO EXPAND ON'''


# Importing the Keras Libraries and Packages

>>>>>>> Stashed changes
from keras.models import Sequential # initialize neural network model as a sequential network
from keras.layers import Conv2D # need 2D arrays for images, 3D arrays for videos
from keras.layers import MaxPooling2D # need the maximum value pixel from the respsective region of interest
from keras.layers import Flatten # converts all the resultant 2D arrays into a single long, continuous linear vector
from keras.layers import Dense # performs the full connection of neural network
<<<<<<< Updated upstream
=======
from keras.preprocessing.image import ImageDataGenerator
>>>>>>> Stashed changes

################ BUILDING OUR CNN MODEL ##################

# create object of the sequential class
<<<<<<< Updated upstream
# Initialising the CNN
=======
>>>>>>> Stashed changes
classifier = Sequential()

# 1 - CONVOLUTION
# add a convolution layer to our sequential object
'''
    CONVO2D EXPLAINED
        4 arguements:
            1. number of filters [32 here]
            2. shape of each filter [3x3]
            3. input shape and type of image (RGB or Black 
             and White) [64x64 res and '3' for RGB]
            4. the activation function we want to use ['relu' 
             for rectifier function]

'''
<<<<<<< Updated upstream
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
=======
classifier.add(Conv2D(32, (3, 3), 
                inputshape = (64, 64, 3), 
                activation = 'relu'))
>>>>>>> Stashed changes

# 2 - POOLING
# add pooling layer to clasiffier object
'''
    MAXPOOLING2D EXPLAINED
        We take a 2x2 matrix, we'll have minimum pixel loss and 
          get a precise region where the features are located
'''
<<<<<<< Updated upstream
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
=======
classifier.add(MaxPooling2D(pool_size=(2, 2)))
>>>>>>> Stashed changes

# 3 - FLATTENING
# convert the pooling object into a continuous vector
'''
    FLATTEN EXPLAINED
        Simply used to perform flattening--i.e., transform the 
         2x2 matrix into a single vector
'''
classifier.add(Flatten())

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
# 4 - FULL CONNECTION
# create a fully connected layer by connecting the nodes we 
#   got after the flattening step
'''
    DENSE FUNCTION EXPLAINED
        adds a fully connected layer
        'units' is the number of nodes that should be present in 
          this hidden layer
            value will always be between the number of input nodes 
              and the output nodes bu tthe art of chosing the most 
              optimal number of nodes can be achieved only through 
              experimental tries
            it's common practice to use a power of 2
'''
<<<<<<< Updated upstream
# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
=======
classifier.add(Dense(units = 128, 
                    activation = 'relu'))

>>>>>>> Stashed changes

# initialise our output layer, which should contain only 1 node
#   as its a binary classification
# the single node will give us the binary output of either CAT or DOG
classifier.add(Dense(units = 1, activation = 'sigmoid'))


################ COMPILING OUR CNN MODEL ##################

'''
    COMPILE EXPLAINED
        optimizer -> to choose the stochastic gradient descent algorithm
        loss -> choose the loss function
        metric -> choose the performance metric
'''
<<<<<<< Updated upstream
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

################ PART 2 ###################
### FITING OUR CNN TO THE IMAGE DATASET ###

from keras.preprocessing.image import ImageDataGenerator
=======
classifier.compile(optimizer = 'adam', 
                    loss = 'binary_crossentropy', 
                    metrics = ['accuracy'])


################ PART 3 ###################
### FITING OUR CNN TO THE IMAGE DATASET ###
>>>>>>> Stashed changes

################ PERFORMING IMAGE AUGMENTATION #################
'''
    IMAGE AUGMENTATION EXPLAINED
        we are doing this to prevent over-fitting
            this is where you get a great training accuracy and very 
              poor testing accuracy due to overfitting of nodes from one 
              layer to another
'''

<<<<<<< Updated upstream
train_datagen = ImageDataGenerator(rescale = 1./255,
                                    shear_range = 0.2,
                                    zoom_range = 0.2,
                                    horizontal_flip = True)
                                    
test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                    target_size = (64, 64),
                                                    batch_size = 32,
                                                    class_mode = 'binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')
=======
train_datagen = ImageDataGenerator(rescale = 1./255, 
                                    shear_range = 0.2, 
                                    zoom_range = 0.2, 
                                    horizontal_flip = True)

test_datagen = ImageDataGenerator (rescale = 1./255)

training_set = train_datagen.flow_from_directory('training_set', 
                                                    target_size = (64, 64), 
                                                    batch_size = 32, 
                                                    class_mode = 'binary')

test_set = test_datagen.flow_from_directory('test_set', 
                                                target_size = (64, 64), 
                                                batch_size = 32, 
                                                class_mode = 'binary')

>>>>>>> Stashed changes

############## FITING DATA INTO MODEL ###############
'''
    FIT GENERATOR EXPLAINED
        steps_per_epoch -> holds the num of training images
        epochs -> a single epoch is a single step in training a neural network
            when a neural network is trained on every training samples only in one 
              pass, we say that one epoch is finished
            so training process should consist of more than 1 epoch
'''

<<<<<<< Updated upstream
classifier.fit_generator(training_set,
                            steps_per_epoch = 8000,
                            epochs = 25,
                            validation_data = test_set,
                            validation_steps = 2000)

=======
classifier.fit_generator(training_set, 
                            steps_per_epoch = 8000, 
                            epochs = 25, 
                            validation_data = test_set, 
                            validation_steps = 2000)


>>>>>>> Stashed changes
################# PART 3 #####################
### new predictions from our trained model ###

import numpy as np
from keras.preprocessing import image

'''
test_image holds the image that needs to be tested on the CNN
Once we have the test image, we will prepare the image to be sent into the model by converting
  its resolution to 64x64 as the model only expects that resolution
Predict() using method on our classifier object to get the prediction
    --will be in binary form
'''

<<<<<<< Updated upstream
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices

if result[0][0] == 0:
    prediction = '1: dog'
else:
    prediction = '1: cat'


print(prediction)
=======
test_image = image.load_image('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

result = classifier.predict(test_image)
training_set.class_indices

if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'
>>>>>>> Stashed changes
