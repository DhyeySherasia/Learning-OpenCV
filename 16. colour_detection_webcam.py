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

cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)

lower_orange = np.array([0, 125, 109])
upper_orange = np.array([255, 255, 255])

lower_blue = np.array([90, 97, 60])
upper_blue = np.array([255, 255, 255])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Getting HSV from webcam
    # orange_book = frame[320, 240]
    # orange_book = np.uint8([[orange_book]])
    # hsv = cv2.cvtColor(orange_book, cv2.COLOR_BGR2HSV)
    # print(hsv)

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Masks are binary images that indicates the pixel in which an operation is to be performed
    # Mask is single channeled black(0) and white(1/255) image
    mask_orange = cv2.inRange(hsv_img, lower_orange, upper_orange)
    mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
    mask_final = cv2.bitwise_or(mask_orange, mask_blue)

    # Masks are binary images that indicates the pixel in which an operation is to be performed
    # Mask is single channeled black(0) and white(1/255) image
    final = cv2.bitwise_and(frame, frame, mask=mask_final)

    # cv2.imshow("Original", frame)
    cv2.imshow("Masked", mask_final)
    cv2.imshow("HSV", hsv_img)
    cv2.imshow("Orange_book", final)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()