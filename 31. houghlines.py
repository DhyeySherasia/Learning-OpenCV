import cv2
import numpy as np

img = cv2.imread("Resources/sudoku.jpg")
img = cv2.resize(img, (0, 0), fx=1.4, fy=1.4)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_img, 50, 150, apertureSize=3)
cv2.imshow("Edges", edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

print(lines)
print(lines.shape)

for line in lines:
    r, theta = line[0]
    x0, y0 = int(r * np.cos(theta)), int(r * np.sin(theta))
    x1, y1 = int(x0 + 1000 * np.sin(theta)), int(y0 + 1000 * (-(np.cos(theta))))
    x2, y2 = int(x0 - 1000 * np.sin(theta)), int(y0 - 1000 * (-(np.cos(theta))))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("HoughLines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()