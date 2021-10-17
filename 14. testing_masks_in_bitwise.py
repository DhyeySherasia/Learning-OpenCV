import cv2
import numpy as np

"""

Heu - Defines the colour from the wide available range of rainbow colours.

Saturation - How much quantity of that colour we want to have. 0 means all white components.
255 means all colour components and no white component quantity. 
This does not tell about the brightness of that colour.
50 means bright enough but faded colour. Concentration of the colour is less.

Value - Brightness of that colour. Amount/quantity remains constant.
50 means concentrated/saturated enough but not too bright.

eg: In smartphones when we decrease the brightness, 'value' of colours change. Saturation remains constant.
Vivid mode, natural mode etc change the saturation. Brightness remains constant.



Mask Using cv2.inRange() :
Masks are binary images that indicates the pixel in which an operation is to be performed
Mask is single channeled black(0) and white(1/255) image

In this file,
Mask_image can be created using inRange() function. We have to specify a limit for HSV values.
In an image, pixels having HSV values within that limit are selected and displayed in white.
All other pixels become black.

In a bitwise_and() function, 'mask=' argument takes the above black-white single channeled 
Mask_image as input. Bitwise_and operation is performed only on image pixels corresponding to 
white pixels in Mask_image. Remaining image pixels become black.

"""

img1 = cv2.imread("Resources/test_img.png")
img2 = cv2.imread("Resources/Abdul_Kalam.jpg")
img2 = cv2.resize(img2, (512, 512))

my_mask = np.zeros([512, 512], np.uint8)
my_mask = cv2.rectangle(my_mask, (0, 410), (100, 510), (255, 255, 255), -1)

lower = np.array([114, 32, 46])
upper = np.array([167, 241, 251])

hsv_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_img1, lower, upper)

# Operation (bitwise_and) occurs only on pixels shown white in masked_image
# Remaining part of the window becomes black
final = cv2.bitwise_and(img1, img1, mask=mask)
my_final = cv2.bitwise_and(img1, img2, mask=my_mask)

cv2.imshow("Final", final)
cv2.imshow("My Final", my_final)
# cv2.imshow("mask", mask)
# cv2.imshow("my mask", my_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()