import cv2
import numpy as np


img = cv2.imread("Resources/Abdul_Kalam.jpg")
img = cv2.resize(img, (512, 512))
constant = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(255, 255, 0))
reflect = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT)
replicate = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
wrap = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_WRAP)
cv2.imshow("Constant", constant)
cv2.imshow("Reflect", reflect)
cv2.imshow("Replicate", replicate)
cv2.imshow("Wrap", wrap)

cv2.waitKey(0)
cv2.destroyAllWindows()