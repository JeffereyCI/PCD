import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar dan ubah ke grayscale
img = cv2.imread('/home/jechis/Downloads/images.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = gray.shape
center = (cols // 2, rows // 2)
angle = 45  # derajat rotasi
scale = 1.0  # tidak ada scaling

# Matriks rotasi
M_rot = cv2.getRotationMatrix2D(center, angle, scale)

# Terapkan transformasi
rotated = cv2.warpAffine(gray, M_rot, (cols, rows))

scale = 1.5  # perbesar 1.5x
M_scaled_rot = cv2.getRotationMatrix2D(center, angle, scale)
scaled_rotated = cv2.warpAffine(gray, M_scaled_rot, (cols, rows))

plt.figure(figsize=(12,4))
plt.subplot(1, 3, 1), plt.imshow(gray, cmap='gray'), plt.title("Original")
plt.subplot(1, 3, 2), plt.imshow(rotated, cmap='gray'), plt.title("Rotation 45°")
plt.subplot(1, 3, 3), plt.imshow(scaled_rotated, cmap='gray'), plt.title("Rotation + Scale 1.5")
plt.tight_layout()
plt.show()
