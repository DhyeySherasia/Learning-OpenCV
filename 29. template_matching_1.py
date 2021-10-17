import cv2
import numpy as np

img = cv2.imread("Resources/soccur.jpg")
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Resources/boy.jpg", 0)
template = cv2.resize(template, (0, 0), fx=0.75, fy=0.75)
height, width = template.shape

# Brightest point will be the top left corner of the template inside the original image
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(result)
location = max_loc
print(max_loc)
bottom_right = (location[0] + width, location[1] + height)
cv2.rectangle(img, location, bottom_right, (255, 255, 0), 3)

cv2.imshow("Object Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
