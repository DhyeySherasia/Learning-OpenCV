import cv2
import numpy as np

img = cv2.imread("Resources/balls.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray_img, 21)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
print(circles)

for (x, y, r) in circles[0]:
    # x, y, r = circle
    cv2.circle(img, (x, y), r, (0, 255, 0), 3)

cv2.imshow("HoughCircles", img)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()


