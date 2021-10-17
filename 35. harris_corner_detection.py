import cv2
import numpy as np

img = cv2.imread("Resources/chess.png")
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

dst = cv2.cornerHarris(gray_img, blockSize=2, ksize=3, k=0.04)
dst = cv2.dilate(dst, None)

img[dst > 0.1 * dst.max()] = (0, 0, 255)

cv2.imshow("Corners", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

