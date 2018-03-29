#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:25:29 2018

@author: anmol
"""
# Importing modules
import glob
import os
from shutil import copyfile
import cv2
from FaceDetector import find_faces

# Making a clean dataset
def Clean_Dataset(emotions):
    
    print ("Making of clean dataset")
    participants = glob.glob('data/source_emotions/*') # returns a list of all folders with participants numbers
    
    for part in participants:
        neutral_added = False
        
        # Getting one session from the participant
        for sessions in glob.glob("%s/*" % part):
        # Getting the files inside one session
            for files in glob.glob('%s/*'% sessions):
                
                # Current Session
                curr_sess = files[20:-30]
                
                print("Current Session :- " + str(curr_sess))
                
                # Opening the file in read mode
                file = open(files , 'r')
                
                # Emotions are encoded as a float , readlines as float and convert into integer
                emotion = int(float(file.readline()))
                
                # Getting the corresponding source images
                images = glob.glob('data/source_images/%s/*' % curr_sess)
                
                # get path for last image in sequence, which contains the emotion
                source_filename = images[-1].split('/')[-1]
                # do same for emotion containing image
                destination_filename = "data/sorted_set/%s/%s" % (emotions[emotion], source_filename)
                # copy file
                copyfile("data/source_images/%s/%s" % (current_session, source_filename), destination_filename)

                if not neutral_added:
                    # do same for neutral image
                    source_filename = images[0].split('/')[-1]
                    # generate path to put neutral image
                    destination_filename = "data/sorted_set/neutral/%s" % source_filename
                    # copy file
                    copyfile("data/source_images/%s/%s" % (current_session, source_filename), destination_filename)
                    neutral_added = True
        
                