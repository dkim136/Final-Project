import math
import cv2
import os
import numpy as np
import glob
import os
import statistics
import csv
import time
from matplotlib import pyplot as plt
import pandas as pd
import shutil
from tempfile import NamedTemporaryFile
prev = 0


final_list = pd.read_csv('final_list.csv')
final_list = final_list[['Item','Number']]


path = "C:/Users/Lydia Yeeun Cho/Desktop/senior project/receive/*.jpg"
files = glob.glob(path)
count = 0

total_file = pd.read_csv("list_items.csv")
total_file = total_file[['Name','Weight', 'Barcode', 'Rect','Tri', 'Cir' ]]


def checkShapeRecogn(barcode) :

    if data.loc[data['total'] == barcode, 'numbers'].values[0] > 1 :
        print('yes')
        return True

    else :
        return False
def writeFinalList(name) :
    if final_list.loc[final_list['Item'] == name, 'Number'].index.tolist():
        row = final_list.loc[final_list['Item'] == name].index.tolist()
        num = final_list.loc[final_list['Item'] == name, 'Number'].values[0] + 1
        final_list.loc[row, 'Number'] = num
        final_list.to_csv('final_list.csv')
    
        
def findBarcode(dif, num) :
    data = pd.read_csv('total.csv')
    data = data[['total','numbers']]

    for i in range(0, 30) :
        
        if total_file.loc[total_file['Weight'] == (dif+i)].index.tolist() :
            
            ix = total_file.loc[total_file['Weight'] == dif+i, 'Barcode'].values[0]
            print("barcode: "+ str(ix))
            print(data.loc[data['total'] == ix, 'numbers'].values[0])
            

            if data.loc[data['total'] == ix, 'numbers'].values[0] > 2 :
                name = total_file.loc[total_file['Weight'] == (dif+i), 'Name'].values[0]
                print("name: " + name)
                writeFinalList(name)
                weight_list.pop(num)
                print(weight_list)
                continue

        elif total_file.loc[total_file['Weight'] == (dif-i)].index.tolist() :
            
            ix = total_file.loc[total_file['Weight'] == dif-i, 'Barcode'].values[0]
            print("barcode: "+ str(ix))
            print(data.loc[data['total'] == ix, 'numbers'].values[0])
            
            if data.loc[data['total'] == ix, 'numbers'].values[0] > 3  :
                name = total_file.loc[total_file['Weight'] == (dif-i), 'Name'].values[0]
                print("name: " + name)
                writeFinalList(name)
                weight_list.pop(num)
                print(weight_list)
                continue
weight_list = []              
def weightDifference(weight):
    global prev
    dif = weight - prev

    if abs(dif) > 30.0:
        weight_list.append(int(dif))
        prev = weight
        
    for i in range (0, len(weight_list)) :
        print(str(i)+ "_weight: " + str(weight_list[i]))  
        findBarcode(weight_list[i], i)
        

##while (1) :
##    weight = input("what is the weight?")
##    weightDifference(int(weight))
