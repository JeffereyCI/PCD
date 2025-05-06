import cv2
import numpy as np
from scipy.signal import convolve2d
from skimage.restoration import wiener
from matplotlib import pyplot as plt

# Load image (grayscale)
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Wiener Filtering (using skimage's wiener function)
wiener_filtered_image = wiener(image, (5, 5))  # Kernel size (5, 5)

# Display the result
plt.figure(figsize=(6,6))
plt.imshow(wiener_filtered_image, cmap='gray')
plt.title('Wiener Filtering')
plt.axis('off')
plt.show()
