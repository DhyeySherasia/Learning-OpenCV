import cv2
import numpy as np

"""
Limitations:
Need to provide initial location. 
Size of rect does not change as car comes closer.
"""

cap = cv2.VideoCapture("Resources/traffic_video.mp4")
# take first frame of the video
ret, frame = cap.read()
# setup initial location of the window
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# setup the ROI for tracking and create histogram back projected image
roi = frame[y:y + height, x:x + width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# setup the termination criteria, either 10 iterations or move by at least 1 pt
term_criteria = (cv2.TERM_CRITERIA_EPS or cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    # apply mean shift to get new location
    ret, track_window = cv2.meanShift(dst, track_window, term_criteria)
    # draw it on the frame
    x, y, width, height = track_window
    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 3)

    cv2.imshow("Traffic", frame)
    cv2.imshow("dst", dst)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()