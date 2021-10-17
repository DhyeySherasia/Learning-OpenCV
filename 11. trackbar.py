import cv2
import numpy as np


def nothing(x):
    pass


img = np.zeros([300, 512, 3], np.uint8)
cv2.namedWindow("Trackbars")

# Creating trackbars for colour changes
# Callback function is executed every time the trackbar value changes
# Name of trackbar, window name, initial value, total values, callback function
cv2.createTrackbar('B', "Trackbars", 0, 255, nothing)
cv2.createTrackbar('G', "Trackbars", 0, 255, nothing)
cv2.createTrackbar('R', "Trackbars", 0, 255, nothing)


while True:
    cv2.imshow("Trackbars", img)

    if cv2.waitKey(1) == 27:
        break

    # Current value of every trackbar
    b = cv2.getTrackbarPos('B', "Trackbars")
    g = cv2.getTrackbarPos('G', "Trackbars")
    r = cv2.getTrackbarPos('R', "Trackbars")

    # img pixels get value of r,g,b (0-255) and hence change colour
    img[:] = [b, g, r]

cv2.destroyAllWindows()













