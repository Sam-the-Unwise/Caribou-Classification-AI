from PIL import Image
import numpy as np
import os

data=[]
labels=[]

cats = os.listdir("cats")
for cat in cats:
    imag = cv2.imread("cats/"+cat)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

dogs=os.listdir("dogs")
for dog in dogs:
    imag=cv2.imread("dogs/"+dog)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)
    
birds=os.listdir("birds")
for bird in birds:
    imag=cv2.imread("birds/"+bird)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

fishs=os.listdir("fishs")
for fish in fishs:
    imag=cv2.imread("fishs/"+fish)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)