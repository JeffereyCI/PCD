import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load grayscale image
gray = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Low Pass Filter (Gaussian Blur)
low_pass = cv2.GaussianBlur(gray, (5, 5), 0)

# High Pass Filter (subtracting low pass from original image)
high_pass = gray - low_pass

# Median Filter
median_filter = cv2.medianBlur(gray, 5)

# Display all filters in a single plot
plt.figure(figsize=(12, 8))

# Low Pass Filter
plt.subplot(1, 3, 1)
plt.imshow(low_pass, cmap='gray')
plt.title('Low Pass Filter (Gaussian Blur)')
plt.axis('off')

# High Pass Filter
plt.subplot(1, 3, 2)
plt.imshow(high_pass, cmap='gray')
plt.title('High Pass Filter (Subtracting Low Pass)')
plt.axis('off')

# Median Filter
plt.subplot(1, 3, 3)
plt.imshow(median_filter, cmap='gray')
plt.title('Median Filter')
plt.axis('off')

plt.tight_layout()
plt.show()
