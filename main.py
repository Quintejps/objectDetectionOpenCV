import cv2
import numpy as np 

threshold = 0.60

#Read images 
farmImg = cv2.imread('farm.png')
wheatImg = cv2.imread('wheat.png')

#Search for matches between farmImg and wheatImg
result = cv2.matchTemplate(farmImg, wheatImg, cv2.TM_CCOEFF_NORMED)

#Search for best matches locations comparing the result with threshold
yLoc, xLoc = np.where(result >= threshold)

#Get width and height of wheatImg
w = wheatImg.shape[1]
h = wheatImg.shape[0]

rectangles = []

#Append best matches locations, width and height of wheatImg to rectangles
for (x, y) in zip(xLoc, yLoc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

#Transform overlap rectangles into single ones
rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.3)

#Draw rectangles on farmImg
for (x, y, w, h) in rectangles:
    cv2.rectangle(farmImg, (x, y), (x + w, y + h), (0, 255, 255), 3)

#Show image farmImg
cv2.imshow('Farm Image', farmImg)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image