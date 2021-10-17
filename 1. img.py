import cv2

img = cv2.imread("Resources/messi.jpg")
cv2.imshow("Output_image", img)

# wait until any key is pressed. Returns ascii value of the key pressed
key = cv2.waitKey(0)

if key == 27:                  # if key pressed == 'ESC'
    cv2.destroyAllWindows()
elif key == ord('s'):          # wait for s key. ord('s') returns ascii value of s
    cv2.imwrite("saved_img.png", img)
    print("Image is saved in your working directory with filename 'saved_img'")
    cv2.destroyAllWindows()

print(f"Value of key pressed: {key}")
print(f"Value of ord('s'): {ord('s')}")
