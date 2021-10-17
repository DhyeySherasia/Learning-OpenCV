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


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbar")
# Lower limit
l_h = cv2.createTrackbar("LH", "Trackbar", 0, 255, nothing)
l_s = cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)
l_v = cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)

# Upper limit
u_h = cv2.createTrackbar("UH", "Trackbar", 255, 255, nothing)
u_s = cv2.createTrackbar("US", "Trackbar", 255, 255, nothing)
u_v = cv2.createTrackbar("UV", "Trackbar", 255, 255, nothing)

while True:

    # HSV - Hue(0-179 in degrees), Saturation(0-255) and Value(0-255)
    # img = cv2.imread("Resources/balls.png")

    ret, img = cap.read()
    img = cv2.flip(img, 1)

    if cv2.waitKey(1) == 27:
        break

    l_h = cv2.getTrackbarPos("LH", "Trackbar")
    l_s = cv2.getTrackbarPos("LS", "Trackbar")
    l_v = cv2.getTrackbarPos("LV", "Trackbar")

    u_h = cv2.getTrackbarPos("UH", "Trackbar")
    u_s = cv2.getTrackbarPos("US", "Trackbar")
    u_v = cv2.getTrackbarPos("UV", "Trackbar")

    # coloured to HSV conversion
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Defining range of HSV
    lower = np.array([l_h, l_s, l_v])  # H,S,V - lower limit
    upper = np.array([u_h, u_s, u_v])  # H,S,V - upper limit

    # Separate out pixels having HSV values in range defined above
    # Pixels in above HSV range become white and remaining everything turns black
    mask_img = cv2.inRange(hsv_img, lower, upper)

    final_img = cv2.bitwise_and(img, img, mask=mask_img)

    cv2.imshow("Final", final_img)

cap.release()
cv2.destroyAllWindows()

