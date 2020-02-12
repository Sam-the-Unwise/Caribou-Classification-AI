# Below is a brief description of what each file does

### trainingCNN.py

This script contains all the methods necessary for training the AI. This script creates the CNN model and then trains the CNN based on the images that have been placed in the 'Dataset/training' folder. While training the CNN, the program will also test the CNN for accuracy using images from the 'Dataset/test' folder, which will allow the program to display an accuracy of how well the model is predicting. The data of the model is then saved underneath the folder 'models' in the files 'model.h5' and 'weights.h5'.

<i> Note that with our current set up of 25 epochs, 3000 training batch size, and 100 test batch size, the model was roughly at 78% accuracy. </i>

### testingCNN.py

This script contains all the necessary methods for testing our AI against desired photoes. The program accesses the folder 'Dataset/single_prediction' and tests each of the pictures in the folder against the saved model. The program will then output a prediction of what it thinks the picture is of (between the choices of cat, dog, duck, and koala).