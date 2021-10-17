import cv2
import numpy as np

cap = cv2.VideoCapture("Resources/people_movement.avi")
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, img = cap.read()
    fg_mask = fgbg.apply(img)

    cv2.imshow("Video", img)
    cv2.imshow("Fore Ground", fg_mask)
    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()
