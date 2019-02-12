# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:17:32 2019

@author: CodersMine

pitch yaw and roll calculator 

it uses eyes and face parts to check the motion of the face 

pitch is tilting of head in front
roll is tilting head on shoulders
yaw is moving head from left to right



"""

#import required libraries 
#import OpenCV library
import cv2
#import matplotlib library
import matplotlib.pyplot as plt
#importing time library for speed comparisons of both classifiers
import time 
#%matplotlib inline
import numpy as np
pitch=0
yaw=0
ex=0
ey=0
ew=0
eh=0


def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

video_capture=cv2.VideoCapture(0)

while True:
    ret,test1=video_capture.read()
    #load test iamge
    #test1 = cv2.imread(r'data/straight.jpg')
    #convert the test image to gray image as opencv face detector expects gray images 
    test1=np.array(test1,dtype=np.uint8)
    gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    
    #img = np.full((100,80,3), 100, np.uint8)
    
    #if you have matplotlib installed then  
    plt.imshow(gray_img, cmap='gray')  
    
    # or display the gray image using OpenCV 
    # cv2.imshow('Test Imag', gray_img) 
    # cv2.waitKey(0) 
    # cv2.destroyAllWindows()
    
    #haar_face_cascade=cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
    
    haar_face_cascade=cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
    
    eye_cascade=cv2.CascadeClassifier('data/haarcascade_eye.xml')
    
    smile_cascade=cv2.CascadeClassifier('data/haarcascade_smile.xml')
    #let's detect multiscale (some images may be closer to camera than others) images 
    faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);  
    
    eyes=eye_cascade.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=5)
    
    #smile=smile_cascade.detectMultiScale(gray_img,scaleFactor=2.9,minNeighbors=5)
    
    print(len(faces))
    
    
    #go over list of faces and draw them as rectangles on original colored 
    #for (x, y, w, h) in faces :     
    #         cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
             
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(test1,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    
    """
    ex=800
    ey=200
    ew=100
    eh=100
    cv2.rectangle(test1,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    
    if y is less : no tilting on sholders zero roll
    
    
    if x is large then no yaw 
    
    """
    #corrections
    pc=10
    yc=137
    try:
        pitch =(eyes[0][1]-eyes[1][1])+pc
    
        yaw =(eyes[0][0]-eyes[1][0])+yc
    except:
        print("No eyes found")
    
    print("pitch is "+str(pitch))
    print("yaw is "+str(yaw))
    #for (sx,sy,sw,sh) in smile:
    #    cv2.rectangle(test1,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    
    plt.imshow(convertToRGB(test1))
    cv2.imshow('Video', convertToRGB(test1))

    print("\n\n\n\nex ey ew eh")
    print(ex,ey,ew,eh)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
    
    
video_capture.release()
cv2.destroyAllWindows()