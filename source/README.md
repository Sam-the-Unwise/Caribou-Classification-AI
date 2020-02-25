# Below is a brief description of each of the files in this folder in alphabetical order

<i> please note our main file is called <b>runCNN.py</b> </i>


### deleteVideoFrames.py

A script that will go through the folders our video frames have been saved in and delete them once training the model has been finished


### organizingTrainAndValidation.py

This script is only used to separate data that has already been classified into the train and validation datasets. It will sort 20% of the data into the validation set and 80% of the data into the training set.


### runCNN.py

This is our <b>main</b> script that will run all the code from other files


### sortPreclassifiedVideos.py

This script is used to sort the preclassified videos (videos already classified by volunteers) into their correct folders based 


### splitVideosIntoFrames.py

This script contains all the necessary methods to split our videos into frames. This script is specifically used for the <i> training </i> and <i> validation </i> data as we need to save these frames for a longer period of time than the testing frames. For splitting testing videos into frames, please reference <i> testingVideosToFrames.py </i>. 

This script will split the videos into the desired amount of frames and save them each to the according folder (for example, a frame from '../dataset/training_set/Excellent' will be saved to '../dataset/training_set_frames/Excellent'). These frames will then be deleted by <i>deleteVideoFrames.py</i> 


### testingCNN.py

This script contains all the necessary methods for testing our AI against desired photoes. The program accesses the folder 'Dataset/single_prediction' and tests each of the pictures in the folder against the saved model. The program will then output a prediction of what it thinks the picture is of (between the choices of cat, dog, duck, and koala).


### testingVideosToFrames.py

This script contains all the methods necessary to split a single video into frames, which are thus stored in an array. This is used by the <i>testing.py</i> script in order to analyze each from of the video individually. The script will also delete the array once the analyzation has been finished. 

<i> Note: the analyzation takes place in testing.py </i>


### trainingCNN.py

This script contains all the methods necessary for training the AI. This script creates the CNN model and then trains the CNN based on the images that have been placed in the 'Dataset/training' folder. While training the CNN, the program will also test the CNN for accuracy using images from the 'Dataset/test' folder, which will allow the program to display an accuracy of how well the model is predicting. The data of the model is then saved underneath the folder 'models' in the files 'model.h5' and 'weights.h5'.

<i> Note that with our current set up of 25 epochs, 3000 training batch size, and 100 test batch size, the model was roughly at 78% accuracy. </i>


### unzip.py

This is a script simply used by our team to unzip the files provided to us by our client and is not necessary to actually running the CNN


### variables.py

A helpful script that contains all the common variables used throughout the other program files in this repository. If anyone is to change the names of their folder locations, they should change them in this script and only this script.
