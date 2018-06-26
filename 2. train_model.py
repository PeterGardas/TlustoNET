# train_model.py

import numpy as np
from models import otherception3 as googlenet
import tensorflow as tf
from random import shuffle

FILE_I_END = 1860

WIDTH = 240
HEIGHT = 120
LR = 1e-3
EPOCHS = 350


model = googlenet(HEIGHT, WIDTH, 1, LR, output=5, model_name='TlustoNETv1.1')

for e in range(EPOCHS):

    train_data = np.load('training_data_grey_shuffled.npy')
    shuffle(train_data)

    train = train_data[:-50]
    test = train_data[-50:]

    X = np.array([i[0] for i in train]).reshape(-1,HEIGHT,WIDTH,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,HEIGHT,WIDTH,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=2500, show_metric=True, run_id="TlustoNETv1.1")

    model.save('TlustoNETv1.1.tfl')
        #tensorboard --logdir=log



