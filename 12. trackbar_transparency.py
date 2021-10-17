import cv2
import numpy as np


def nothing(x):
    pass


img1 = cv2.imread("Resources/Abdul_Kalam.jpg")
img2 = cv2.imread("Resources/Indian_flag.jpg")
img1 = cv2.resize(img1, (512, 400))
img2 = cv2.resize(img2, (512, 400))
cv2.namedWindow("Merged Image")

# Creating trackbars
cv2.createTrackbar("Kalam", "Merged Image", 0, 100, nothing)
cv2.createTrackbar("Colour", "Merged Image", 0, 1, nothing)

while True:
    if cv2.waitKey(1) == 27:
        break

    trans = cv2.getTrackbarPos("Kalam", "Merged Image")
    switch = cv2.getTrackbarPos("Colour", "Merged Image")
    alpha = trans * 0.01
    beta = 1-alpha
    merged_img = cv2.addWeighted(img1, alpha, img2, beta, 0)

    if switch == 0:
        merged_img = cv2.cvtColor(merged_img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Merged Image", merged_img)


cv2.destroyAllWindows()