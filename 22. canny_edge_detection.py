import cv2


def nothing(x):
    print(x)


img = cv2.imread("Resources/messi.jpg", 0)

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Min", "Trackbar", 0, 500, nothing)
cv2.createTrackbar("Max", "Trackbar", 500, 500, nothing)

while True:

    if cv2.waitKey(1) == 27:
        break

    min_value = cv2.getTrackbarPos("Min", "Trackbar")
    max_value = cv2.getTrackbarPos("Max", "Trackbar")

    canny = cv2.Canny(img, min_value, max_value)
    cv2.imshow("Canny", canny)

cv2.destroyAllWindows()
