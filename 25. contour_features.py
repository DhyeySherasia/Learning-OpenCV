import cv2
import numpy as np

img = cv2.imread("Resources/star.jpg")
img = cv2.resize(img, None, fx=2, fy=2)
img2 = img.copy()
img3 = img.copy()
img4 = img.copy()
img5 = img.copy()
img6 = img.copy()
img7 = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
contours, ret = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(f"Length of contours: {str(len(contours))}")
cv2.drawContours(img, contours, -1, (255, 255, 0), 3)

# returns dictionary of all moment values calculated
# contours is higher dimensional than contours[0]
cnt = contours[0]
M = cv2.moments(cnt)
print(M)

# Centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv2.circle(img, (cx, cy), 5, (0, 0, 0), -1)

# Area
print("Area: " + str(cv2.contourArea(cnt)))
print("Area is also: " + str(M['m00']))

# Perimeter
print("Perimeter: " + str(cv2.arcLength(cnt, True)))

# Approximation
epsilon = 0.01 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)  # returns contour/points
cv2.drawContours(img2, approx, -1, (0, 255, 0), 3)

# Convex Hull
hull = cv2.convexHull(cnt)  # returns a contour/points
cv2.drawContours(img3, hull, -1, (0, 0, 255), 3)

# Convex or not
k = cv2.isContourConvex(cnt)
print(k)

# Bounding Rectangle. Doesn't consider rotation of object, hence area of rect not min
x, y, w, h = cv2.boundingRect(cnt)
rect = cv2.rectangle(img4, (x, y), (x + w, y + h), (255, 0, 0), 3)

# Rotated rectangle
rect2 = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect2)
box = np.int0(box)
cv2.drawContours(img5, [box], -1, (127, 255, 95), 3)

# Minimum enclosing circle
(x, y), r = cv2.minEnclosingCircle(cnt)
x, y, r = int(x), int(y), int(r)
cv2.circle(img6, (x, y), r, (95, 127, 255), 3)

# Ellipse
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img7, ellipse, (127, 30, 200), 3)

# cv2.imshow("Contours", img)
cv2.imshow("Approx", img2)
cv2.imshow("Hull", img3)
cv2.imshow("Bounding rectangle", img4)
cv2.imshow("Rotating rectangle", img5)
cv2.imshow("Enclosing circle", img6)
cv2.imshow("Ellipse", img7)

cv2.waitKey(0)
cv2.destroyAllWindows()
