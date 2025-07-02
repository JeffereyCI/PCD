import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
gray = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Harris Corner Detection
harris_corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate the corners to mark them clearly
harris_corners_dilated = cv2.dilate(harris_corners, None)

# Mark the corners on the original image (optional)
image_with_corners = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # Convert grayscale to color for marking corners
image_with_corners[harris_corners_dilated > 0.01 * harris_corners_dilated.max()] = [0, 0, 255]  # Red color for corners

# Display the result
plt.figure(figsize=(6,6))
plt.imshow(image_with_corners)
plt.title('Harris Corner Detector')
plt.axis('off')
plt.show()
