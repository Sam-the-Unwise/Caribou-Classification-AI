# # Importing the Keras Libraries and Packages

# from keras.models import Sequential # initialize neural network model as a sequential network
# from keras.layers import Conv2D # need 2D arrays for images, 3D arrays for videos
# from keras.layers import MaxPooling2D # need the maximum value pixel from the respsective region of interest
# from keras.layers import Flatten # converts all the resultant 2D arrays into a single long, continuous linear vector
# from keras.layers import Dense # performs the full connection of neural network
# from keras.preprocessing.image import ImageDataGenerator

# ################ BUILDING OUR CNN MODEL ##################

# # create object of the sequential class
# classifier = Sequential()

# # 1 - CONVOLUTION
# # add a convolution layer to our sequential object
# '''
#     CONVO2D EXPLAINED
#         4 arguements:
#             1. number of filters [32 here]
#             2. shape of each filter [3x3]
#             3. input shape and type of image (RGB or Black 
#              and White) [64x64 res and '3' for RGB]
#             4. the activation function we want to use ['relu' 
#              for rectifier function]

# '''
# classifier.add(Conv2D(32, (3, 3), 
#                 inputshape = (64, 64, 3), 
#                 activation = 'relu'))

# # 2 - POOLING
# # add pooling layer to clasiffier object
# '''
#     MAXPOOLING2D EXPLAINED
#         We take a 2x2 matrix, we'll have minimum pixel loss and 
#           get a precise region where the features are located
# '''
# classifier.add(MaxPooling2D(pool_size=(2, 2)))

# # 3 - FLATTENING
# # convert the pooling object into a continuous vector
# '''
#     FLATTEN EXPLAINED
#         Simply used to perform flattening--i.e., transform the 
#          2x2 matrix into a single vector
# '''
# classifier.add(Flatten())


# # 4 - FULL CONNECTION
# # create a fully connected layer by connecting the nodes we 
# #   got after the flattening step
# '''
#     DENSE FUNCTION EXPLAINED
#         adds a fully connected layer
#         'units' is the number of nodes that should be present in 
#           this hidden layer
#             value will always be between the number of input nodes 
#               and the output nodes bu tthe art of chosing the most 
#               optimal number of nodes can be achieved only through 
#               experimental tries
#             it's common practice to use a power of 2
# '''
# classifier.add(Dense(units = 128, 
#                     activation = 'relu'))


# # initialise our output layer, which should contain only 1 node
# #   as its a binary classification
# # the single node will give us the binary output of either CAT or DOG
# classifier.add(Dense(units = 1, activation = 'sigmoid'))


# ################ COMPILING OUR CNN MODEL ##################

# '''
#     COMPILE EXPLAINED
#         optimizer -> to choose the stochastic gradient descent algorithm
#         loss -> choose the loss function
#         metric -> choose the performance metric
# '''
# classifier.compile(optimizer = 'adam', 
#                     loss = 'binary_crossentropy', 
#                     metrics = ['accuracy'])


# ################ PART 3 ###################
# ### FITING OUR CNN TO THE IMAGE DATASET ###

# ################ PERFORMING IMAGE AUGMENTATION #################
# '''
#     IMAGE AUGMENTATION EXPLAINED
#         we are doing this to prevent over-fitting
#             this is where you get a great training accuracy and very 
#               poor testing accuracy due to overfitting of nodes from one 
#               layer to another
# '''

# train_datagen = ImageDataGenerator(rescale = 1./255, 
#                                     shear_range = 0.2, 
#                                     zoom_range = 0.2, 
#                                     horizontal_flip = True)

# test_datagen = ImageDataGenerator (rescale = 1./255)

# training_set = train_datagen.flow_from_directory('training_set', 
#                                                     target_size = (64, 64), 
#                                                     batch_size = 32, 
#                                                     class_mode = 'binary')

# test_set = test_datagen.flow_from_directory('test_set', 
#                                                 target_size = (64, 64), 
#                                                 batch_size = 32, 
#                                                 class_mode = 'binary')


# ############## FITING DATA INTO MODEL ###############
# '''
#     FIT GENERATOR EXPLAINED
#         steps_per_epoch -> holds the num of training images
#         epochs -> a single epoch is a single step in training a neural network
#             when a neural network is trained on every training samples only in one 
#               pass, we say that one epoch is finished
#             so training process should consist of more than 1 epoch
# '''

# classifier.fit_generator(training_set, 
#                             steps_per_epoch = 8000, 
#                             epochs = 25, 
#                             validation_data = test_set, 
#                             validation_steps = 2000)


# ################# PART 3 #####################
# ### new predictions from our trained model ###

# import numpy as np
# from keras.preprocessing import image

# '''
# test_image holds the image that needs to be tested on the CNN
# Once we have the test image, we will prepare the image to be sent into the model by converting
#   its resolution to 64x64 as the model only expects that resolution
# Predict() using method on our classifier object to get the prediction
#     --will be in binary form
# '''

# test_image = image.load_image('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis = 0)

# result = classifier.predict(test_image)
# training_set.class_indices

# if result[0][0] == 1:
#     prediction = 'dog'
# else:
#     prediction = 'cat'

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))



# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(4, activation = 'softmax'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

TRAIN_BATCH_SIZE = 100
TEST_BATCH_SIZE = 60

train_datagen = ImageDataGenerator(rescale = 1./255,
                                    shear_range = 0.2,
                                    zoom_range = 0.2,
                                    horizontal_flip = True)
                                    
test_datagen = ImageDataGenerator(rescale = 1./255)

#training_set = train_datagen.flow_from_directory('dataset/test2/training_set',
#                                                    target_size = (64, 64),
#                                                    batch_size = 32,
#                                                    class_mode = 'categorical')

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                    target_size = (64, 64),
                                                    batch_size = TRAIN_BATCH_SIZE,
                                                    class_mode = 'categorical')

#test_set = test_datagen.flow_from_directory('dataset/test2/testing_set',
#                                            target_size = (64, 64),
#                                            batch_size = 32,
#                                            class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = TEST_BATCH_SIZE,
                                            class_mode = 'categorical')
#amount of files in training set
train_len = 294

#amount of files in test set
test_len = 94


#we want to avoid over fitting because that gives false accuracy
#   than normally is shown if accuracy is far off from val_accuracy.
#   The real accuracy is about when the accuracy and val accuracy converge.
classifier.fit_generator(training_set,
                            #NOTE==========Mess with batch sizes to find best accuracy
                            steps_per_epoch = train_len//TRAIN_BATCH_SIZE,
                            #mess around with epochs to find a better accuracy
                            epochs = 50,
                            validation_data = test_set,
                            validation_steps = test_len//TEST_BATCH_SIZE)

target_dir = './models/'

classifier.save('./models/model.h5')
classifier.save_weights('./models/weights.h5')