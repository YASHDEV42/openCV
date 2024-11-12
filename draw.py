import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)
# 1. Paint the image a certain color
blank[200:300, 300:400] = 100, 200, 50
# cv.imshow('Green', blank)
# 2. Draw a Rectangle
cv.rectangle(blank, (100, 100), (400, 400), (100, 200, 50), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)
# 3. Draw a Circle
cv.circle(blank, (250, 250), 40, (100, 0, 50), thickness=-1)
# cv.imshow('Circle', blank)
# 4. Draw a Line
cv.line(blank, (100, 100), (400, 400), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)
# 5. Write text
cv.putText(blank, 'Tubitak project', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 2)
cv.imshow('Text', blank)


cv.waitKey(0)