import math
import cv2
import os
import numpy 
import glob
import os
import statistics
import csv
import time
import pandas as pd
import shutil
from tempfile import NamedTemporaryFile

font = cv2.FONT_HERSHEY_COMPLEX


############################################################################
images = []

data_file = open("data2.txt", "w")

data = pd.read_csv('total.csv')
data = data[['total','numbers']]

path = "C:/Users/Lydia Yeeun Cho/Desktop/senior project/shape_recognizing/Frame4/*.jpg"
files = glob.glob(path)
count = 0

total_file = pd.read_csv("list_items.csv")
total_file = total_file[['Name','Weight', 'Barcode', 'Rect','Tri', 'Cir' ]]
################################################################################   
def findPoints(c) :
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    return extLeft, extRight, extTop, extBot

def findSize(extLeft, extRight, extTop, extBot) :
    list_x = [extLeft[0], extRight[0], extTop[0], extBot[0]]
    list_y = [extLeft[1], extRight[1], extTop[1], extBot[1]]
    min_x = min(list_x)
    max_x = max(list_x)
    min_y = min(list_y)
    max_y = max(list_y)
    return(min_x, max_x, min_y, max_y)

def findShapes(img) :
    img = cv2.resize(img, (1000, 500))
    _, threshold = cv2.threshold(img, 70, 155, cv2.THRESH_BINARY)
    _, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #variables for shapes
    total = 0
    tri_cnt = 0
    sqr_cnt = 0
    cir_cnt = 0
    largest_area = 0
    largest_approx = 0
    img_area = 500000

    #########finding the boundingbox##############
    for cnt in contours:      
        approx = cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt, True), True)
        area = abs(cv2.contourArea(cnt))
        if(abs(cv2.contourArea(cnt))< 400 or not(cv2.isContourConvex(approx))):
                continue    

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > largest_area :
            left, right, top, bot = findPoints(approx)

            width_x = abs(left[0] - right[0])
            width_y = abs(top[0] - bot[0])
            height_x = abs(left[1] - right[1])
            height_y = abs(top[1] - bot[1])

            if abs(width_x - width_y) < 200 and abs(height_x - height_y) <100 :
                largest_area = area
                largest_approx = approx
                largest_cnt = cnt
                
        
    if largest_area > 100 :
        ##cv2.drawContours(img, [largest_approx], 0, (0), 5)
        extLeft, extRight, extTop, extBot = findPoints(largest_approx)
        min_x, max_x, min_y, max_y = findSize(extLeft, extRight, extTop, extBot)

        ########find the shapes inside the bounding box##############
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt, True), True)
            area = abs(cv2.contourArea(cnt))

            if(abs(cv2.contourArea(cnt))< 400 or not(cv2.isContourConvex(approx))):
                    continue    
              
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if x <= min_x +30 or x >= max_x -30 or y >= max_y -30 or y <= min_y + 30:
              continue
            if area > largest_area :
                continue
            
            cv2.drawContours(img, [approx], 0, (0), 5)
            if len(approx) == 3:
                cv2.putText(img, "Tri", (x, y), font, 1, (0))
                tri_cnt +=1          
          
            elif len(approx) == 4:
                cv2.putText(img, "Rect", (x, y), font, 1, (0))        
                sqr_cnt += 1
                
            else:
                cv2.putText(img, "Cir", (x, y), font, 1, (0))
                cir_cnt += 1
        print(total)

        if tri_cnt + sqr_cnt + cir_cnt == 10 :
            total = sqr_cnt*10 + tri_cnt*5 + cir_cnt *2
            data_file.write(str(total) + " " + str(cir_cnt) + " " + str(tri_cnt) + " " + str(sqr_cnt) +"\n")
            cnt = 0

            if(data.loc[data['total'] == total].index.tolist()) :
                row = data.loc[data['total'] == total].index.tolist()
                num =data.loc[data.total == total, 'numbers'].values[0] + 1
                data.loc[row, 'numbers'] = num
                print(data.loc[data.total == total, 'numbers'].values[0])
                data.to_csv('total.csv') 
def initiate() :
    for n in data.total :
        data.loc[data.total == n, 'numbers'] = 0
    data.to_csv('total.csv')
    
def ShapeRecogn() :
    for n in files:
      img = cv2.imread( n, cv2.IMREAD_GRAYSCALE) 
      images.append(img)

    for im in images:
        findShapes(im)
img = cv2.imread("C:/Users/Lydia Yeeun Cho/Desktop/senior project/Final_project/image1.jpg",cv2.IMREAD_GRAYSCALE) 
#ShapeRecogn()
#findShapes(img)
initiate()
