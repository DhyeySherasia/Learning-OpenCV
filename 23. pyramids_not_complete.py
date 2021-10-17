import cv2

# Up-down means pixel wise
img = cv2.imread("Resources/messi.jpg")

# Gaussian pyramid
dp = [img]
for i in range(6):
    img = cv2.pyrDown(img)
    dp.append(img)
    cv2.imshow(str(i), dp[i])

# Laplacian pyramid
lap = [dp[6]]
# range(start int, stop int, step int)
for i in range(5, 0, -1):
    gaussian_extended = [dp[i]]

cv2.waitKey(0)
cv2.destroyAllWindows()