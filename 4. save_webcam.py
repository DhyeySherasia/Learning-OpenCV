import cv2

cap = cv2.VideoCapture(0)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Defining codec
# Creating video writer object with some builtin functions
video_writer_object = cv2.VideoWriter("Saved_video.mp4", fourcc, 20, (640, 480))

while True:

    success_or_not, frame = cap.read()
    frame = cv2.flip(frame, 0)
    video_writer_object.write(frame)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
video_writer_object.release()
cv2.destroyAllWindows()
