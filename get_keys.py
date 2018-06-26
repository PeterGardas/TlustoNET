import keyboard #Using module keyboard
import time


w = [1, 0, 0, 0, 0]
a = [0, 1, 0, 0, 0]
d = [0, 0, 1, 0, 0]
s = [0, 0, 0, 1, 0]
n = [0, 0, 0, 0, 1]


def KeysGet():
	if keyboard.is_pressed('w'):
		return w
	elif keyboard.is_pressed('a'):
		return a
	elif keyboard.is_pressed('d'):
		return d
	elif keyboard.is_pressed('s'):
		return s
	else:
		return n
		
	

