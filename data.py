# -*- coding: utf-8 -*-
"""data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g8NGz6h7sLgOgNvgNjYmX56qAti3GZt6
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import cv2
from glob import glob
from tqdm import tqdm
import imageio
from albumentations import HorizontalFlip ,VerticalFlip,Rotate #data augmentation
from sklearn.model_selection import train_test_split

def load_data(path,split=0.1):
  images=sorted(glob(os.path.join(path,"images/*")))
  masks=sorted(glob(os.path.join(path,"masks/*")))

  total_size = len(images)
  valid_size = int(split * total_size)
  test_size = int(split * total_size)

  #splitting images data into train and valid
  train_x,valid_x = train_test_split(images,test_size=valid_size,random_state=42)
  train_y,valid_y = train_test_split(masks,test_size=valid_size,random_state=42)

  #splitting train data into train and test
  train_x,test_x = train_test_split(train_x,test_size=test_size,random_state=42)
  train_y,test_y = train_test_split(train_y,test_size=test_size,random_state=42)

  #print(total_size,valid_size,test_size)
  return (train_x,train_y),(valid_x,valid_y),(test_x,test_y)