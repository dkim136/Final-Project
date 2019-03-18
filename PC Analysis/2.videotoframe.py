import math
import cv2
import os
import numpy 
import glob
import os
import statistics
import csv

###### divide the video into frames #############
vidcap = cv2.VideoCapture('output.avi')
success,image = vidcap.read()
count = 0

while success:
  path = 'C:/Users/Lydia Yeeun Cho/Desktop/senior project/shape_recognizing/Frame4'
  cv2.imwrite(os.path.join(path, "frame%d.jpg" % count), image)           
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1
