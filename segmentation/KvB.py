import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path gambar thermal
image_path = "Fernando 1.tif"

# Baca gambar grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Otsu Thresholding
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Optional: Morphological closing (mengisi lubang kecil di kaki)
kernel = np.ones((5, 5), np.uint8)
cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Tampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Asli (Grayscale)")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Otsu Threshold")
plt.imshow(thresh, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Kaki vs Background")
plt.imshow(cleaned, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()