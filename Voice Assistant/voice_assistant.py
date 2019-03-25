import speech_recognition as sr
import itemlist as item
import time
import RPi.GPIO as GPIO
#~ import socket_client as sc
from math import ceil
#~ from espeak import espeak
from gtts import gTTS
from pygame import mixer as m
import os

keyword = "strawberry"
status = False
m.init(25500)

def search_item(userinput):
	flag = 0
	x = userinput.split()
	j = 0
	m.music.load('searching.mp3')
	m.music.play()
	time.sleep(3)
	while j < len(x):
		if item.itemloct.get(x[j], -1) != -1:
			output = "Item name: %s \n" %(x[j])
			output += "\n \n \n \n \n"
			output += "Item location is isle %d \n" %(item.itemloct.get(x[j]))
			output += "\n \n \n \n \n"
			num = round(float(item.itemprice.get(x[j])),2)
			#~ num = ceil(num*100.0)/100
			output += "Item price is  %.2f dollars" %num
			time.sleep(2)
			tts = gTTS(text=output, lang='en')
			tts.save("response.mp3")
			m.music.load('response.mp3')
			m.music.play()
			flag = 1
		j+=1
	if userinput == 'checkout':
		return False
	if flag != 1:
		m.music.load('no_item.mp3')
		m.music.play()		
		return True
		

def question_recognize(r,mic):
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	userinput = ''
	try:	
		userinput = r.recognize_google(audio)
	except sr.UnknownValueError:
		m.music.load('invalid.mp3')
		m.music.play()
		question_recognize(r,mic)
	except sr.RequestError as e:
		m.music.load('invalid.mp3')
		m.music.play()
		question_recognize(r,mic)
	status = search_item(userinput)	
	return status

def speech_recognize(r, mic):
	userinput = ''
	m.music.load('intro.mp3')
	m.music.play()
	status = False
	userinput = ''
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	try:	
		userinput = r.recognize_google(audio)
	except sr.UnknownValueError:
		speech_recognize(r,mic)
	except sr.RequestError as e:
		speech_recognize(r,mic)
	if keyword in userinput:
		m.music.load('help.mp3')
		m.music.play()
		status = question_recognize(r,mic)
	return status
	
	
#~ if __name__ == "__main__":	
	#~ r = sr.Recognizer()
	#~ mic = sr.Microphone(device_index = 3)
	#~ status = speech_recognize(r,mic)
	#~ speech_recognize(r,mic)
	#~ while status != False:
		#~ status = speech_recognize(r,mic)

