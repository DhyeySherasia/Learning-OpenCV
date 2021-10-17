import cv2
import numpy as np
from matplotlib import pyplot as plt

"""

Adaptive thresholding calculates the threshold value for different regions of the image. 
Hence different parts of an image have different threshold value.
This is helpful when image parts have different illumination. 
Poorly illuminated part will entirely become black for certain global threshold value.

"""

# 0 because turn img into gray scale
img = cv2.imread("Resources/page1.jpg", 0)

ret, simple_th = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
adap_th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adap_th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Original", img)
cv2.imshow("Simple", simple_th)
cv2.imshow("Mean", adap_th1)
cv2.imshow("Gaussian", adap_th2)

cv2.waitKey(0)
cv2.destroyAllWindows()



