import time
import numpy as np
import mss
import cv2
import pyxhook
import keyboard

from get_keys import KeysGet
from showscreen import grab_screen

#Training has been done with SIlver tesla on the road


paused = False

#training_data = list(np.load('training_data.npy'))
training_data = []

def main():

	for i in list(range(5))[::-1]:
		print(i+1)
		time.sleep(1)
		#training_data = list(np.load('training_data.npy'))
	
	while not paused:
		keys = KeysGet()
		img = np.array(grab_screen(0, 0, 1680, 1050))
		training_data.append([img, keys])
#	    if len(training_data) % 100 == 0:
#			np.save('training_data.npy', training_data)
#			print("Saved!")
		if keyboard.is_pressed('t'):
			print("Saved")
			np.save('training_data.npy', training_data)
			break

		
main()
