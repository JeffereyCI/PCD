import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image in grayscale
img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Brightness transformation: tambah brightness
bright_img = cv2.convertScaleAbs(img, alpha=1, beta=50)  # beta = brightness

# Negative image
negative_img = 255 - img

# Tampilkan
plt.figure(figsize=(10,4))
plt.subplot(1,3,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(bright_img, cmap='gray'), plt.title('Brighter')
plt.subplot(1,3,3), plt.imshow(negative_img, cmap='gray'), plt.title('Negative')
plt.tight_layout()
plt.show()
