#3

import cv2 as cv
import numpy as np

img = cv.imread('Photos/snow.jpg')
cv.imshow('Snow', img)


#rescale
def rescaleFrame(frame, scale=0.75):
    # work for images, videos, live videos
    width = int(frame.shape[1] * scale) # shape[1] = width
    height = int(frame.shape[0] * scale) # shape[0] = height

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# change resolution

# def changeRes(width, height):
#     # only live videos (from webcam,...)
#     capture.set(3, width)
#     capture.set(4, height)

# reading videos
capture = cv.VideoCapture('Videos/geography.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

