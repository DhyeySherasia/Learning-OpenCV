import cv2

cap = cv2.VideoCapture(0)
print("Width: ", cap.get(3))
print("Height: ", cap.get(4))

# cap.set(3, 640)  # Width
# cap.set(4, 480)  # Height
#
# print(cap.get(3))
# print(cap.get(4))

while True:
    # Frame by frame
    success_or_not, frame = cap.read()

    # Display frame
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
