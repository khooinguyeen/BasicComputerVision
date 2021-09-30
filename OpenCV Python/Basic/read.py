#1

import cv2 as cv

#reading images

# img = cv.imread('OpenCV Python/Photos/astronaut.jpg')
# cv.imshow('Astronaut', img)

#reading videos

capture = cv.VideoCapture('OpenCV Python/Videos/sealife.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)