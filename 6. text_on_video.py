import cv2
import datetime
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(datetime.datetime.now())
    cv2.putText(frame, text, (20, 450), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Text2", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()