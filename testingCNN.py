# -*- coding: utf-8 -*-
"""
Created on Tue Dev 7 2:56:12 2019

@author: Samantha
"""

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

model_path = 'models/model.h5'
model_weights_path = 'models/weights.h5'
#test_path = './dataset/test2/single_prediction'
test_path = 'dataset/single_prediction'

model = load_model(model_path)
model.load_weights(model_weights_path)

img_width, img_height = 50, 50

def predict(file):
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    answer = np.argmax(result)
    
    if answer == 0:
        #print("Predicted Dog Eating")
        print("Predicted Cat")
    elif answer == 1:
        #print("Predicted dog running")
        print("Predicted Dog")
    elif answer == 2:
        #print("Predicted dog sitting")
<<<<<<< Updated upstream:executeTest.py
        print("Predicted Duck")
    elif answer == 3:
        #print("Predicted dog sleeping")
        print("Predicted Koala")
    else:
        print("Unable to predict specimen. Need further training")
=======
        print("Predicted Ducks")
    elif answer == 3:
        #print("Predicted dog sleeping")
        print("Predicted Koala")
>>>>>>> Stashed changes:executeTest.py
        
    return answer

for i, ret in enumerate(os.walk(test_path)):
    for i, filename in enumerate(ret[2]):
        if filename.startswith("."):
            continue
        
        print(ret[0]+'/'+filename)
        result = predict(ret[0]+'/'+filename)
        print(" ")