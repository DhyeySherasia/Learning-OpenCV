import cv2
import numpy as np

img = cv2.imread("Resources/soccur.jpg")
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Resources/boy.jpg", 0)
template = cv2.resize(template, (0, 0), fx=0.75, fy=0.75)

# Slicing --> [start:stop:step]
width, height = template.shape[::-1]  # [::-1] reverse the position of returned values

result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Select threshold such that we get only one coordinate point
threshold = 0.96
max_point_loc = np.where(result >= threshold)
print(max_point_loc)

for pt in zip(*max_point_loc[::-1]):  # Unzipping each element(here one) in reverse order
    cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (255, 255, 0), 3)

cv2.imshow("Object Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
