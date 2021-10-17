import cv2
import numpy as np

img = np.zeros([500, 500, 3])  # Zeros for black
# image, "Text string", bottom left pt, font style, font scale, colour, thickness
img = cv2.putText(img, "First Text", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)
cv2.imshow("Text", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
