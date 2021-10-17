import urllib.request as ur
import cv2
import numpy as np

my_url = 'http://192.168.50.187:8080/shot.jpg'

while True:
    img_response = ur.urlopen(my_url)
    img_np = np.array(bytearray(img_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_np, -1)
    cv2.imshow("External camera", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()