#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:46:53 2018

@author: anmol
"""

import glob
import random
import numpy as np
import cv2

from ImageManipulations import Load_Image


# Checking the open cv version and initializing the corresponding fish face recog.
# Summary of fish face recog. ->
'''
FisherFaces face recognizer algorithm extracts principal components that differentiate one person from the others.
'''
if cv2.__version__ != '3.1.0':
    fishface = cv2.createFisherFaceRecognizer()
else:
    fishface = cv2.face.createFisherFaceRecognizer()
training_set_size = 0.95


