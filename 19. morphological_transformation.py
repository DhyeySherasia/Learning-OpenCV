import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("Resources/4.png", 0)

# ret, binary = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
kernal = np.ones((2, 2), np.uint8)

# A pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’.
dilated = cv2.dilate(binary, kernal, iterations=2)

# A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels
# under the kernel is 1, otherwise it is eroded (made to zero).
erosion = cv2.erode(binary, kernal, iterations=1)

# Erosion followed by dilation
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernal)

# Dilation followed by erosion
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernal)

# Difference between image and opening
tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernal)

# Difference between closing and image
blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernal)

# Difference between dilation and erosion
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernal)


cv2.imshow("dilated", dilated)
cv2.imshow("erosion", erosion)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("tophat", tophat)
cv2.imshow("blackhat", blackhat)
cv2.imshow("gradient", gradient)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# titles = ["Image", "Binary", "Dilated", "Eroded", "Opening Morph",
#           "Closing Morph", "BlackHat", "Gradient", "Tophat"]
# images = [img, binary, dilated, erosion, opening, closing, blackhat, gradient, tophat]
#
# for i in range(len(images)):
#     plt.subplot(3, 3, i+1)
#     plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
