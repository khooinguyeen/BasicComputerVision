#2

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0 #paint all pixel
# blank[150:200, 250:300] = 255, 0, 255 #paint 1 spectacular space
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,500), (255, 255, 0), thickness = 2) # Viền
# cv.rectangle(blank, (0,0), (250,500), (255, 255, 0), thickness = cv.FILLED)
# cv.rectangle(blank, (0,0), (250,500), (255, 255, 0), thickness = -1) #cv.FILLED = -1
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 0), thickness = -1)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = -1) # the name thickness is not necessary
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), 3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'I luv U', (300, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)