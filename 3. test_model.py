import numpy as np
from showscreen import grab_screen
import cv2
import time
from models import otherception3 as googlenet
import pyautogui

import random

WIDTH = 240
HEIGHT = 120
LR = 1e-3
EPOCHS = 1
MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.09

w = [1, 0, 0]
a = [0, 1, 0]
d = [0, 0, 1]



    
model = googlenet(HEIGHT, WIDTH, 1, LR, output=5)
model.load('TlustoNETv1.1.tfl')

#Hold key for an amout of secs coz lesser is better than morrer??
def hold_key(hold_time, key):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)
    pyautogui.keyUp(key)


def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    while True:
        # 800x600 windowed mode
        #screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        img = np.array(grab_screen(0, 0, 1680, 1050))
        #print('loop took {} seconds'.format(time.time()-last_time))
        #last_time = time.time()


        prediction = model.predict([img.reshape(120,240,1)])[0]
        #prediction = model.predict(img)
            
        print(prediction)
        #Gets the index of the biggest value in the array
        biggest_value = np.argmax(prediction, axis=0)
        print(biggest_value)
        #test = np.round(prediction)

        if biggest_value == 0:
            pyautogui.press('w')
        elif biggest_value == 1:
        	pyautogui.press('w')
        	hold_key(0.125, 'a')
        elif biggest_value == 2:
        	pyautogui.press('w')
        	hold_key(0.125, 'd')
        elif biggest_value == 3:
            pyautogui.press('s')
        elif biggest_value == 4:
            pyautogui.press('w')



main()       

