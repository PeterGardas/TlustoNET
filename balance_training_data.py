import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import time

train_data = np.load('training_data_grey.npy')

df = pd.DataFrame(train_data)

print(Counter(df[1].apply(str)))


print(len(train_data))


w = []
a = []
d = []
s = []
n = []
final_data = []




for data in train_data:
	img = data[0]
	choice = data[1]
	
	if choice == [1, 0, 0, 0, 0]:
		w.append([img, choice])
	elif choice == [0, 1, 0, 0, 0]:
		a.append([img, choice])
	elif choice == [0, 0, 1, 0, 0]:
		d.append([img, choice])
	elif choice == [0, 0, 0, 1, 0]:
		s.append([img, choice])
	elif choice == [0, 0, 0, 0, 1]:
		n.append([img, choice])
	else:
		print("No matches! (imposible)")
		print(choice)
		
w = w[:len(a)][:len(d)][:len(n)]#[:len(s)]
a = a[:len(d)][:len(n)][:len(w)]
d = d[:len(a)][:len(n)][:len(w)]
n = n[:len(a)][:len(d)][:len(w)]
#s = s[:len(a)][:len(d)][:len(n)]]

#data_data = w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + w + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + d + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n + n+ n + n + n + n + n + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s + s+ s + s + s + s + s
#final_data = data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data + data_data
final_data = w + a + d + s + n

shuffle(final_data)
print(len(final_data))

df = pd.DataFrame(final_data)

print(Counter(df[1].apply(str)))
np.save('training_data_grey_shuffled.npy', final_data)
