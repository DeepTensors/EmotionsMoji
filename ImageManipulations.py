#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:38:10 2018

@author: anmol
"""

import cv2 
import numpy as np
#if cv2.__version__ == '3.1.0':
from PIL import Image
#else:
 #   import Image

# Function to Convert Image to Numpy array
def ImageToArray(image):
    return np.asarray(image)

# Frunction to Convert numpy array into Image
def ArrayToImage(nparray , mode = 'RGB'):
    return Image.fromarray(np.asarray(np.clip(nparray, 0, 255), dtype='uint8'), mode)
    
# Function to  Load Image and convert into Gray Scale
def Load_Image(path):
    source_image = cv2.imread(path)
    return cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
    
# Function to  Draw Partially Transparent Image over another image
def draw_with_alpha(source_image , image_to_draw , coordinates):
    
    # Getting the coordinates
    x , y , w , h = coordinates
    
    # Resizing the image that is to be drawn
    image_to_draw = image_to_draw.resize((h,w) , Image.ANTIALIAS)
    
    # Converting image that is to be drawn into numpy array
    image_array = ImageToArray(image_to_draw)
    
    # Lets Draw it
    for c in range(0,3):
        source_image[y:y+h , x:x+w , c] = image_array[: ,: , c] * (image_array[: , : , 3] / 255.0)\
                                            + source_image[y:y+h , x:x+w , c] * (1.0 - image_array[:,:,3] / 255.0)
                                            