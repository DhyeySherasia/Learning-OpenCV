import cv2
import numpy as np

img = cv2.imread("Resources/chess.png")
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 255, 0), -1)

cv2.imshow("Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

