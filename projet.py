#!/usr/bin/python3.5
# -*-coding:Latin-1 -*

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
import keras
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

class loadImage:

	def __init__(self):
		self.loader=ImageDataGenerator()

	def loadImages(self,dir,size):
		train_images=self.loader.flow_from_directory(directory=dir,target_size=(size,size),color_mode='grayscale')
		return train_images

class neuralNetworkBuilder:

	def load(self,file):
		return load_model(file)

IMG_SIZE=224
CSV_LABELS_TRAIN="labels_2000.csv"
CSV_LABELS_TEST="label_test.csv"
REP_TRAIN="./data_2000/"
REP_TEST="./data_test/"
REP_TRY="./try/"

loader=loadImage()
builder=neuralNetworkBuilder()
model=builder.load('model.hdf5')
img = image.load_img("picture.png",target_size=(224,224), color_mode = "grayscale")
img = np.asarray(img)
img = img.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
prediction=model.predict(img)
if(prediction[0][0]>prediction[0][1]):
	print('0')
elif(prediction[0][0]<prediction[0][1]):
	print('1')







