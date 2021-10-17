import cv2
import numpy as np

# Line
img1 = np.ones((255, 255, 3))  # Creating white window
# img1[:, 0:125] = [255, 255, 0]  # Changing pixel value of 0-255 columns of all rows
# image, start pt, end pt, colour, thickness
cv2.line(img1, (10, 10), (230, 230), (0, 125, 0), 3)
cv2.imshow("Line", img1)

# Rectangle
img2 = np.ones((255, 255, 3))
# image, top left pt, bottom right pt, colour, thickness
# Using -1 in place of thickness fills the entire closed figure
img2 = cv2.rectangle(img2, (60, 60), (200, 120), (255, 255, 0), -1)
cv2.imshow("Rectangle", img2)

# Circle
img3 = np.ones((255, 255, 3))
# image, center pt, radius, colour, thickness
img3 = cv2.circle(img3, (125, 125), 60, (0, 0, 255), 3)
cv2.imshow("Circle", img3)

# Ellipse
img4 = np.ones((255, 255, 3))
# image, center, (major axis, minor axis), angle of ellipse, start angle of arc, end angle of arc, colour, thickness
img4 = cv2.ellipse(img4, (150, 150), (80, 50), -20, 0, 360, (0, 255, 255), 3)
cv2.imshow("Ellipse", img4)

# Polygon
img5 = np.ones((255, 255, 3))
# Create an array of points
pts = np.array([[10, 20], [30, 80], [175, 125], [180, 78]])
# image, array of pts, isClosed, colour, thickness
img5 = cv2.polylines(img5, [pts], True, (255, 0, 255), 3)
cv2.imshow("Polygon", img5)

cv2.waitKey(0)
cv2.destroyAllWindows()
