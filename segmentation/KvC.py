import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path gambar thermal
image_path = "Fernando 2 s.tif"

# Baca gambar grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Validasi jika gambar gagal dibaca
if img is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan: {image_path}")

# Gunakan teknik adaptif threshold (karena kaki dan celana beda tekstur)
adapt = cv2.adaptiveThreshold(img, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY_INV,
                              25, 10)

# Morphology untuk memperjelas batas
kernel = np.ones((3, 3), np.uint8)
morph = cv2.morphologyEx(adapt, cv2.MORPH_OPEN, kernel)

# Tampilkan hasil
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.title("Original Picture")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Adaptive Threshold")
plt.imshow(adapt, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Kaki vs Celana")
plt.imshow(morph, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()