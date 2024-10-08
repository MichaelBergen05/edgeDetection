import cv2 as cv

# Reading an image
img = cv.imread('Photos/catTest.jpg')
cv.imshow('Cat', img)

# Converting image to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

cv.waitKey(0)