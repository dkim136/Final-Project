import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt
import glob
import os

#dictionary of all contours
contours = {}
#array of edges of polygon
approx = []
#scale of the text
scale = 2
#camera
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    #Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret==True:
        #grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Canny
        canny = cv2.Canny(frame,80,240,3)

    #Display the resulting frame
    out.write(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 1048689: #if q is pressed
            break
