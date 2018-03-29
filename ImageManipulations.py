#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:38:10 2018

@author: anmol
"""

import cv2 
import numpy as np
import Image

# Function to Convert Image to Numpy array
def ImageToArray(image):
    return np.asarray(image)

# Frunction to Convert numpy array into Image
def ArrayToImage(nparray , mode = 'RGB'):
    return Image.fromarray(np.asarray(np.clip(nparray, 0, 255), dtype='uint8'), mode)
    
# Function to  Load Image and convert into Gray Scale
def Load_Image(path):
    source_image = cv2.imread(source_path)
    return cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
    
# Function to  Draw Partially Transparent Image over another image
def draw_with_alpha():
    