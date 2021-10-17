import cv2
import numpy as np

# events = [i for i in dir(cv2) if "EVENT" in i]
# print(events)


def mouse_callback(event, x, y, flag, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        text = str(x)+', '+str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Coordinates", img)  # Output on coordinates window (new window is created)

    elif event == cv2.EVENT_LBUTTONDOWN:
        blue_img = img[y, x, 0]  # Rows: y axis   and   Columns: x axis
        green_img = img[y, x, 1]
        red_img = img[y, x, 2]
        text = 'B: ' + str(blue_img) + ' G: ' + str(green_img) + ' R: ' + str(red_img)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("RGB", img)  # Output on RGB window


img = cv2.imread("Resources/test_img.png")
cv2.imshow("RGB", img)
cv2.setMouseCallback("RGB", mouse_callback)  # Action on RGB window

cv2.waitKey(0)
cv2.destroyAllWindows()
