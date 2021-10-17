import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Resources/4.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.uint8)/25

dst = cv2.filter2D(img, -1, kernal)
blur = cv2.blur(img, (5, 5))
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
median_blur = cv2.medianBlur(img, 5)
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ["Original", "2d Convolution", "Blur", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
images = [img, dst, blur, gaussian_blur, median_blur, bilateral_filter]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
