import cv2
import os
import time

my_path = "D:\\Programming Projects\\Sentdex Tensorflow own dataset\\fist"
module_val = 5
min_blur = 100
gray_img = False
save_data = True
show_image = True
img_width = 50
img_height = 50

global count_folder
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

count = 0
count_save = 0


def save_data_function():
    global count_folder
    count_folder = 0
    while os.path.exists(my_path + str(count_folder)):
        count_folder += 1

    os.makedirs(my_path + str(count_folder))


if save_data:
    save_data_function()

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (img_width, img_height))
    if gray_img:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if save_data:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % module_val == 0 and blur > min_blur:
            now_time = time.time()
            cv2.imwrite(my_path + str(count_folder) + '/' + str(count_save)
                        + '_' + str(int(blur)) + '_' + str(now_time) + ".png", img)
            count_save += 1
        count += 1

    if show_image:
        cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
