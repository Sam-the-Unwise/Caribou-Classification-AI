# Smart Software Caribou Classification Tool

Developed for our client Katie Orndahl as a NAU Computer Science Capstone Project. This project is being created in order to make sorting through tens of thousands of videos easier for our client. The videos in question are shot using camera collars that have been applied to Alaskan/Canadia caribou. Currently, these videos are only being analyzed by tens of volunteers, but there are +90,000 videos currently with more on the way, meaning that tens of volunteers will not be enough. 

Our client has issued us this project to make the work of sorting videos both easier on her and her time, as well as the volunteers. Our job is to create a Smart Software Caribou Classification Tool, or as we decided a Convolutional Nerual Network (CNN), in order to sort videos based on their quality of view. This file will discuss in broad terms how our team has desided to design and create this model. If you are looking for a more indepth view of our process, please visit (https://www.cefns.nau.edu/capstone/projects/CS/2020/Caribou-Cams-S20/).

Below we have listed the different stages of our model. As of December 11, 2019, our team finished Stage One of the model. Currently, we are working on gettig Stage Two to work and plan to have it mostly working by February 28th.

### stage one
This is a CNN project that was built with the hopes of it being able to successfully differentiate between four different animals just based on pictures. These animals are: cat, dog, koala, and duck. The CNN was built using Keras with Tensorflow and contains two main files built by us: testing.py and executeTest.py. This CNN was developed in this repository and thus the different version have been saved here, but if you wish to only see the final version of this stage, please go to (https://github.com/Sam-the-Unwise/Four-category-CNN).

### stage two -- where we are now
The CNN is then upgraded in order to work with video instead of pictures. Our team has done this by separating the videos by frames, running each frame against the AI, and then averaging the results from all the frames in order to get a result of the video. This is likewise done when training the model, which will break down the video into frames and use each frame to train the model.

### stage three -- coming soon
Our group is then going to upgrade the CNN in order to successfully be able to determine between four different types of video qualities: "Excellent", "Good", "Fair/Poor", and "Extremely Obstructed". In this stage, we will work with the model in order to develop the most accurate output we possibly can.

## Getting Started

<i> Please note, most of this code was downloaded from or created by the Python library Keras and we are not claiming any of it to be our own work. The only things that were created by us are the testing.py and executeTest.py files </i>

The following instructions are meant to help you understand the code in broad detail. For a more detailed explanation, please see the file notes_on_training_CNN.py, which has extensive comments that explain the code. Also please sea

### Prerequisites

```
python
```
Install
```
pip install  tensorflow, Keras, numpy, os, math, random
```
<i> please note that for our model we had to download specific things that needed to be added to the Keras library but as many of these were different for our individual machines, I have chosen to leave them off </i>

### trainingCNN.py

This script contains all the methods necessary for training the AI. This script creates the CNN model and then trains the CNN based on the images that have been placed in the 'Dataset/training' folder. While training the CNN, the program will also test the CNN for accuracy using images from the 'Dataset/test' folder, which will allow the program to display an accuracy of how well the model is predicting. The data of the model is then saved underneath the folder 'models' in the files 'model.h5' and 'weights.h5'.

<i> Note that with our current set up of 25 epochs, 3000 training batch size, and 100 test batch size, the model was roughly at 78% accuracy. </i>

### testingCNN.py

This script contains all the necessary methods for testing our AI against desired photoes. The program accesses the folder 'Dataset/single_prediction' and tests each of the pictures in the folder against the saved model. The program will then output a prediction of what it thinks the picture is of (between the choices of cat, dog, duck, and koala).

### Team notes

Our reasoning behind choosing these animals is because cats, dogs, and koalas look very similar while ducks look very different. We chose to use these because, while testing the model, we could see specifically if it was giving the wrong prediction because the animals simply looked similar or because the model hadn't been trained correctly (should that mean too small of a data set, not enough epochs, a small training batch size, etc.)

We left the model at 78% accuracy for now because of the sole reason that this current model takes about 12 hours to run on our computers, but the model can indeed be made to be accurate further. This will be a continued project by us as we attempt to see how accurate we can make our model.


# Authors

* **Samantha Muellner** - *Team Lead* - [GitHub](https://github.com/Sam-the-Unwise)

* **Keenan Swanson** - *Customer Communicator* - [GitHub](https://github.com/Keenanks)

* **Dongyang Yu** - *Recorder* - [Github](https://github.com/Dongyang-Yu)

* **Shuyue Qiao** - *Architect* - [Github](https://github.com/SHUYUEQIAO)

## Acknowledgments

* **Katie Orndah, Ecoinformatics PhD. Student** - *Client*
