import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average_blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian_blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median_blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 10, 10)
cv.imshow('Bilateral_blur', bilateral)

cv.waitKey(0)
