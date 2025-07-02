import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar dan konversi ke grayscale
image = cv2.imread('coin_jpg.jpg', cv2.IMREAD_GRAYSCALE)

# Hitung gradien Sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Gradien horizontal
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Gradien vertikal
edges = np.sqrt(sobel_x**2 + sobel_y**2)  # Magnitudo gradien

# Normalisasi dan konversi ke uint8
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Tampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Gambar Asli')
plt.subplot(122), plt.imshow(edges, cmap='gray'), plt.title('Tepi (Sobel)')
plt.show()

