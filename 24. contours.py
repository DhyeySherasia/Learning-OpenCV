import cv2

img = cv2.imread("Resources/4.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(f"Number of contours: {str(len(contours))}")

# -1 --> all contour coordinates. Can use 0,1,2 in place of -1 for diff results
cv2.drawContours(img, contours, -1, (255, 255, 0), 3)

cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()