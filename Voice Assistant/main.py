import RPi.GPIO as GPIO
import speech_recognition as sr
import voice_assistant as va
import time

r = sr.Recognizer()
mic = sr.Microphone(device_index = 1)



#~ print("It is in interrupt")


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(15, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)



while(1):
	if GPIO.input(15) == GPIO.HIGH:
		time.sleep(0.5)
		status = va.speech_recognize(r,mic)
		
