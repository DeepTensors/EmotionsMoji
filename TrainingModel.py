#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:18:55 2018

@author: anmol
"""

# Importing libraries
import glob
import random
import numpy as np
import cv2
from PIL import Image

from ImageManipulations import Load_Image as load_image

print(help(cv2.face))
print(cv2.__version__)

# Checking the opencv version
if cv2.__version__ != '3.1.0':
    fishface = cv2.createFisherFaceRecognizer()
else:
    fishface = cv2.face.createFisherFaceRecognizer()
training_set_size = 0.95


def get_files(emotion):
    """
    gets paths to all images of given emotion and splits them into two sets: trainging and test
    :param emotion: name of emotion to find images for
    """
    files = glob.glob("data/sorted_set/%s/*" % emotion)
    random.shuffle(files)
    
    print (files)
    
    training = files[:int(len(files) * training_set_size)]
    
    print (training_set_size)
    print(training)
    
    prediction = files[-int(len(files) * (1 - training_set_size)):]
    
    print (prediction)
    
    return training, prediction


def make_sets():
    """
    method used to create datasets for all emotions. It loads both images and its labels to memory into training and test labels
    """
    training_data = []  # Training Data
    training_labels = [] # Training Data label (index of corresponding emotions)
    prediction_data = [] # Prediction data
    prediction_labels = [] # Training Data label (index of corresponding emotions)
    
    # Emotion in list of emotions
    for emotion in emotions:
        
        # Getting random training and prediction data
        training, prediction = get_files(emotion)

        # One item from training
        for item in training:
            # Append the corresponding data
            training_data.append(load_image(item))
            training_labels.append(emotions.index(emotion))

        for item in prediction:
            prediction_data.append(load_image(item))
            prediction_labels.append(emotions.index(emotion))

    return training_data, training_labels, prediction_data, prediction_labels


def run_recognizer():
    """
    method is creating datasets using make_sets method, then it trains a model and tet with a test set. It returns correct guesses to test data count ratio
    """
    training_data, training_labels, prediction_data, prediction_labels = make_sets()

    print("size of training set is:", len(training_labels), "images")
    fishface.train(training_data, np.asarray(training_labels))

    print("predicting classification set")
    correct = sum(1 for id, image in enumerate(prediction_data) if fishface.predict(image) == prediction_labels[id])

    return ((100 * correct) / len(prediction_data))


if __name__ == '__main__':
    emotions = ["neutral", "anger", "disgust", "happy", "sadness", "surprise"]

    for i in range(0, 1):
        correct = run_recognizer()
        print("got", correct, "percent correct!")

    fishface.save('classifier/emotion_detection_model.xml')