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

# Removing Old Dataset
def remove_old_set(emotions):

    print("Removing old dataset")

    # Getting one emotion in emotions
    for emotion in emotions:
        #getting the files list
        filelist = glob.glob("data/sorted_set/%s/*" % emotion)
        # Take the file one by one and remove it
        for f in filelist:
            os.remove(f)


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
        
# Extracting faces
# Input -> emotions                    
def extract_faces(emotions):
    print ("extract faces")
    
    # getting the emotion from emotions 
    for emotion in emotions:
        
        # Getting all photos corresponding to that emotion
        photos = glob.glob('data/sorted_set/%s/*' % emotion)
        
        # Getting the file number and photo
        for file_number, photo in enumerate(photos):
            
            # Reading the photo
            frame = cv2.imread(photo)
            
            # getting the (normalized face , face coord)
            normalized_faces = find_faces(frame)
            
            # Removing the photo
            os.remove(photo)

            # Getting the face <- ((normalized face , face coord))
            for face in normalized_faces:
                try:
                    # Writing photo (normalized face) to the path given
                    cv2.imwrite("data/sorted_set/%s/%s.png" % (emotion, file_number + 1), face[0])  # write image
                except:
                    # Printing error 
                    print("error in processing %s" % photo)

# Main              
if __name__ == '__main__':
    
    '''
    Emotions list
    1. Neutral
    2. Anger
    3. Contempt
    4. disgust
    5. fear
    6. happy
    7. sadness
    8. surprise
    '''
    emotions = ['neutral', 'anger', 'contempt', 'disgust', 'fear', 'happy', 'sadness', 'surprise']
    
    # Removing old dataset
    remove_old_set(emotions)
    
    # Cleaning the Dataset
    Clean_Dataset(emotions)
    
    # Extracting the faces 
    extract_faces(emotions)                    
                    