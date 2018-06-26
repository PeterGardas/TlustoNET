# TlustoNET
Deep learning type of neural network used for self driving.

This was a one year project done in three weeks :D. It is used in Tesla Simulator to self drive a car, all the files all messy but
I will change that in the future.

Inspired by sentdexe's pygta5

Usage:

`pip3 install tensorflow==1.5.0 tflearn pandas numpy scipy pyautogui keyboard`.

Then adjust resolution of the game in `1. Generate Training data.py`.

Then run `python3 1.\ Generate\ Training\ data.py`, record enought samples, ideally 1000000 samples.

Now you need to train the model so run `python3 2.\ train_model.py`.

When your model is trained you can test it by issuing command `python3 3.\ test_model.py`

Sit back and enjoy your model driving (or hope to :D).

If you want to add more keys than `W`, `A`, `D`, `S` and `NoKeys` you need to change `get_keys.py`


