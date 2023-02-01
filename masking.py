import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats_2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle_mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle_mask)

masked = cv.bitwise_and(img, img, mask=circle_mask)
cv.imshow('Masked_Image', masked)

cv.waitKey(0)
