import cv2
import numpy as np
import matplotlib.pyplot as plt

# ===== Variabel Path Gambar =====
image_path = 'clown.webp'  # Ganti dengan path gambar kamu

# ===== Membaca dan Konversi ke Grayscale =====
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ===== 1. OTSU Thresholding =====
_, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ===== 2. CANNY Edge Detection =====
canny_edges = cv2.Canny(gray, 100, 200)

# ===== 3. SOBEL (EDGE) Detection =====
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)

# ===== VISUALISASI HASIL =====
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(otsu_thresh, cmap='gray')
plt.title("OTSU Thresholding")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(canny_edges, cmap='gray')
plt.title("Canny Edge Detection")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(sobel_edges, cmap='gray')
plt.title("Sobel (Edge Detection)")
plt.axis("off")

plt.tight_layout()
plt.show()