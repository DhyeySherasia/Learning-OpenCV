import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Resources/sudoku.jpg", 0)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_y = np.uint8(np.absolute(sobel_y))
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)
added = cv2.add(sobel_x, sobel_y)
sobels = cv2.Sobel(img, cv2.CV_64F, 1, 1)
sobels = np.uint8(np.absolute(sobels))

titles = ["Original", "Laplacian", "Sobel X", "Sobel Y", "Sobels combined", "Sobels", "Added"]
images = [img, lap, sobel_x, sobel_y, sobel_combined, sobels, added]

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
