import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1. Baca gambar dan hitung FFT
image = cv2.imread('coin_jpg.jpg', 0)  # Baca gambar grayscale
fft = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft)

# 2. Buat filter (contoh: low-pass)
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # Pusat frekuensi
mask = np.zeros((rows, cols), np.uint8)
r = 30  # Radius filter
cv2.circle(mask, (ccol, crow), r, 1, -1)  # Low-pass: lingkaran di tengah

# 3. Aplikasikan filter
filtered = fft_shifted * mask
fft_filtered = np.fft.ifftshift(filtered)
image_filtered = np.fft.ifft2(fft_filtered).real

# 4. Plot hasil
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title("Asli")
plt.subplot(1, 3, 2), plt.imshow(mask, cmap='gray'), plt.title("Mask Low-pass")
plt.subplot(1, 3, 3), plt.imshow(image_filtered, cmap='gray'), plt.title("Hasil Filter")
plt.show()