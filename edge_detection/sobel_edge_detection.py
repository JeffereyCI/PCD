import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path gambar
image_path = 'clown.webp'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel X dan Y
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Kombinasi gradien
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Konversi ke 8-bit (0–255)
sobel_uint8 = cv2.convertScaleAbs(sobel_combined)

# Tampilkan hasil
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobel_uint8, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')
plt.tight_layout()
plt.show()