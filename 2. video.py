import cv2

cap_video = cv2.VideoCapture("Resources/test_video.mp4")
print(cap_video.get(7))  # Number of frames in the video

while True:
    # Capture frame by frame and return if successfully captured or not.
    success_or_not, current_frame = cap_video.read()

    if success_or_not == True:

        # Our operation on current frame
        gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

        # Display current frame
        cv2.imshow("Video", gray_frame)
        if cv2.waitKey(20) == 27:  # wait for 20ms. If ESC pressed, break the loop, else read next frame
            break

    else:
        break

cap_video.release()
cv2.destroyAllWindows()
