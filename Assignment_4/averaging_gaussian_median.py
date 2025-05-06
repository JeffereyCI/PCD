# Convert to grayscale
import cv2
import matplotlib as plt

img = cv2.imread('input.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Averaging
avg_blur = cv2.blur(gray, (5, 5))

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Median Filter
median_blur = cv2.medianBlur(gray, 5)

# Display
plt.figure(figsize=(12,4))
plt.subplot(1,4,1), plt.imshow(gray, cmap='gray'), plt.title('Original')
plt.subplot(1,4,2), plt.imshow(avg_blur, cmap='gray'), plt.title('Averaging')
plt.subplot(1,4,3), plt.imshow(gaussian_blur, cmap='gray'), plt.title('Gaussian')
plt.subplot(1,4,4), plt.imshow(median_blur, cmap='gray'), plt.title('Median')
plt.tight_layout()
plt.show()
