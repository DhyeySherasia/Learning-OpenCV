import cv2

cap = cv2.VideoCapture("Resources/people_movement.avi")
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=10)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (255, 255, 0), 2)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # if area > some value then only draw rectangle
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 255, 0), 3)
        cv2.putText(frame1, "Status: Movement", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

    cv2.imshow("Movement Tracking", frame1)
    # cv2.imshow("diff", diff)
    # cv2.imshow("gray", gray)
    # cv2.imshow("blur", blur)
    # cv2.imshow("thresh", thresh)
    # cv2.imshow("dilated", dilated)
    # cv2.drawContours(frame1, contours, -1, (255, 255, 0), 3)
    # cv2.imshow("Contours", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()