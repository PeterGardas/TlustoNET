import time
import mss

import cv2
import mss
import numpy as np

training_data = []

def grab_screen(top, left, width, height):
	with mss.mss() as sct:
		# Part of the screen to capture
		monitor = {'top': top, 'left': left, 'width': width, 'height': height}
		last_time = time.time()
		# Get raw pixels from the screen, save it to a Numpy array
		img = np.array(sct.grab(monitor))
		img = cv2.resize(img, dsize=(240, 120), interpolation=cv2.INTER_CUBIC)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		return img
