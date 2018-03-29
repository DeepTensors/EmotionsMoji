#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:18:17 2018

@author: anmol
"""

import cv2

fascCascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

# Function for finding faces
def find_faces(image):
    # getting the face coordinates
    face_coord = Locate_Face(image)
    
    # Crop faces
    crop_face = [image[y:y+h , x:x+w] for (x,w,y,h) in face_coord]
    
    # Normalizing the Crop Faces
    normalized_faces = [Noramlizing_Face(face) for face in crop_face]
    
    # Returning
    return zip(normalized_faces, face_coord)    
    
# Function for Normalizing Faces
def Normalizing_Face(face):
    # BGR to Gray Scale
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    
    # Resizing the image
    face = cv2.resize(face, (350, 350))

    return face;    
    
# Function for Locating Faces
def Locate_Face(image):
    faces = fascCascade.detectMultiScale(  
        image,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(70, 70))
    return faces;
    

    
if __name__ == '__main__':
    
    # Read the Test Image
    img = cv2.imread('test_data/test.jpg')

    # Show the Test Image
    cv2.imshow("Img" , img)

    #Show Faces
    for index,face in enumerate(find_faces(img)):
        cv2.imshow("face %s" %index, face[0])
   
    cv2.waitKey(0)