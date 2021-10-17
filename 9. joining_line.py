import cv2
import numpy as np


def mouse_click(event, x, y, flag, param):

    if event == cv2.EVENT_LBUTTONDOWN and len(points) % 2 == 0:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1, cv2.LINE_AA)
        cv2.imshow("Join Line", img)

    elif event == cv2.EVENT_LBUTTONDOWN and len(points) % 2 == 1:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1, cv2.LINE_AA)
        cv2.line(img, points[-2], points[-1], (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Join Line", img)


img = np.zeros([512, 512, 3])
cv2.imshow("Join Line", img)
points = []
cv2.setMouseCallback("Join Line", mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()


