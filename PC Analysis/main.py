# now we have the pc act as a server
import detect_remove_weight as dw
import socket               
import time
import random
from statistics import stdev
from statistics import harmonic_mean
import ShapeRecogn as sr
from statistics import mean 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import pandas as pd
host = '192.168.50.232' 
#host = '192.168.1.9'
port = 12345  
s.bind((host, port))             
s.listen(5) 

time_one = time.time()
count = 0

std = [0.0,0.0,0.0,0.0,0.0]

while True:
	c, addr = s.accept()
	f = open('image%d' %count + '.jpg', 'wb')
	l = c.recv(1024)

	while(l):
		f.write(l)
		l = c.recv(1024)
	f.close()

	print("Done Recieving Image")

	c,addr = s.accept()
	#print("Recieving_weight")
	#data2 = int(str(c.recv(1024), 'utf8')) #gets the data in a utf8 format, so we decode it here
	data2 = c.recv(1024)
	weight = float(data2.decode())

	std.pop(0)
	std.append(weight)

	if stdev(std) <= 10:
		current_cart_weight = mean(std)
		print(current_cart_weight)
		dw.weightDifference(current_cart_weight)



	print('Current weight', weight)

	if dw.sendCode() == True :
                shopping_list = dw.sendList()
                print(shopping_list)
                c,addr = s.accept()
                string = 'item_name'.encode()
                c.sendall(string)
                

	
	count +=1

	#print(time.time()-time_one)

