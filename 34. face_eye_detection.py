import cv2

cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier("Resources/face.xml")
eye_model = cv2.CascadeClassifier("Resources/eye.xml")

while cap.isOpened():
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray_img)

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 3)
        gray_roi = gray_img[y:y + h, x:x + w]
        roi = img[y:y + h, x:x + w]
        eyes = eye_model.detectMultiScale(gray_roi)
        for eye in eyes:
            ex, ey, ew, eh = eye
            cv2.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 3)

    cv2.imshow("Detecting faces", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
