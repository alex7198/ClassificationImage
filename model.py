#!/usr/bin/python3.5
# -*-coding:Latin-1 -*

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

from PIL import Image # used for loading images
import numpy as np
import os # used for navigating to image path
import imageio

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers. normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.optimizers import Adam
import numpy as np
from keras.preprocessing import image
from keras.models import load_model

from matplotlib import pyplot as plt


  
class loadImage:

	def __init__(self):
		self.loader=ImageDataGenerator()

	def loadImages(self,dir,size):
		train_images=self.loader.flow_from_directory(directory=dir,target_size=(size,size),color_mode='grayscale')
		return train_images

class neuralNetworkBuilder:

	def create(self,IMG_SIZE):
		model = Sequential()
		model.add(Conv2D(4, kernel_size = (3, 3),padding='same', activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)))
		model.add(Conv2D(4, kernel_size = (3, 3),padding='same', activation='relu'))
		
		model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
		model.add(Conv2D(8, kernel_size=(3,3),activation='relu',padding='same'))
		model.add(Conv2D(8, kernel_size=(3,3), activation='relu',padding='same'))
		
		model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
		model.add(Conv2D(16, kernel_size=(3,3), activation='relu',padding='same'))
		model.add(Conv2D(16, kernel_size=(3,3), activation='relu',padding='same'))
		model.add(Conv2D(16, kernel_size=(3,3), activation='relu',padding='same'))
		
		model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
		model.add(Conv2D(32, kernel_size=(3,3), activation='relu',padding='same'))
		model.add(Conv2D(32, kernel_size=(3,3), activation='relu',padding='same'))
		model.add(Conv2D(32, kernel_size=(3,3), activation='relu',padding='same'))
		

		model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
		
		model.add(Flatten())
	
		model.add(Dense(32, activation='relu'))
		model.add(Dense(32, activation='relu'))
		model.add(Dense(2, activation = 'softmax'))
		return model
	
	def prepare(self,model):
		opt = Adam(lr=0.001)
		model.compile(optimizer=opt,loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])
	
	def train(self,model,traindata,testdata):
		checkpoint = ModelCheckpoint("cp/1_32/weights.{epoch:02d}-{val_accuracy:.2f}.hdf5", monitor='val_accuracy', 
		verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
		early = EarlyStopping(monitor='val_accuracy', min_delta=0, patience=20, verbose=1, mode='auto')
		model.fit_generator(generator=traindata, validation_data= testdata,epochs=100,callbacks=[early,checkpoint])
	
	def save(self,model,file):
		model.save(file)
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
train_data = loader.loadImages(REP_TRAIN,IMG_SIZE)
test_data=loader.loadImages(REP_TEST,IMG_SIZE)
model = builder.create(IMG_SIZE)
builder.prepare(model)
builder.train(model,train_data,test_data)







