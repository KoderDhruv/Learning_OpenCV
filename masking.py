import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask=cv.circle(blank, )

cv.waitKey(0)