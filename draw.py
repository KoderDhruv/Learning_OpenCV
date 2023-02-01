import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red', blank)

cv.rectangle(blank, (50, 70), (300, 400), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

cv.circle(blank, (blank.shape[0]//2, blank.shape[1] //
          2), 40, (255, 255, 255), thickness=-1)
cv.imshow('Circle', blank)

cv.line(blank, (100, 500), (480, 0), (255, 255, 0), thickness=3)
cv.imshow('Line', blank)

cv.putText(blank, 'Dhruv', (255, 255), cv.FONT_HERSHEY_COMPLEX,
           fontScale=1.0, color=(255, 0, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
