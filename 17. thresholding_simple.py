import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Resources/4.png")

# pixels < threshold: black. pixels > threshold: white.
ret, th1 = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)

# Inverse of simple binary shown above
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# pixels < threshold: original pixels. pixels > threshold: pixel value becomes threshold value
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# pixels < threshold: black. pixels > threshold: original
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# pixels < threshold: original. pixels > threshold: black
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Original", img)
cv2.imshow("Binary", th1)
cv2.imshow("Binary Inverse", th2)
cv2.imshow("Trunc", th3)
cv2.imshow("Tozero", th4)
cv2.imshow("Tozero Inverse", th5)

# titles = ["Original", "Binary", "Binary Inverse", "Trunc", "Tozero", "Tozero Inverse"]
# images_to_show = [img, th1, th2, th3, th4, th5]
#
# for i in range(6):
#     plt.subplot(2, 3, i+1)
#     plt.imshow(images_to_show[i])
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()