import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load grayscale image
gray = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
canny_edges = cv2.Canny(gray, 100, 200)

# Display the result
plt.figure(figsize=(6,6))
plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edge Detector')
plt.axis('off')
plt.show()
