# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 00:10:25 2018

@author: CodersMine
"""

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn import svm
import cv2

digits=load_digits()
cv2.cv2.imload("untitled.jpg")
img=cv2.imread("untitled.jpg")

plt.gray()
for i in range(20):
    print(i)
    plt.matshow(digits.images[i])
    plt.show()

print(digits.images[20])

clf=svm.SVC()
clf.fit(digits.data[:-1],digits.target[:-1])
prediction=clf.predict(digits.data[2:3])

print(prediction)