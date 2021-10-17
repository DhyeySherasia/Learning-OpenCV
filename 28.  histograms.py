import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
img histogram shows how many number of pixels inside the image 
which have this pixel value
"""

# img = np.zeros((200, 200), np.uint8)
# cv2.rectangle(img, (10, 10), (100, 100), 255, -1)

img = cv2.imread("Resources/test_img.png", 0)

# plt.hist method
# b, g, r = cv2.split(img)
# cv2.imshow("Blue", b)
# cv2.imshow("Green", g)
# cv2.imshow("Red", r)
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])

# cv2.calcHist method
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

cv2.imshow("Image", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()