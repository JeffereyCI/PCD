import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread('/home/jechis/Downloads/images.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape

# Titik asal (dari gambar asli)
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# Titik tujuan (distorsi bebas: projective/homografi)
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [250, 250]])

# Matriks transformasi projective (homography)
M_proj = cv2.getPerspectiveTransform(pts1, pts2)

# Terapkan transformasi
dst_proj = cv2.warpPerspective(gray, M_proj, (cols, rows))

# Tampil
plt.figure(figsize=(10,4))
plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(dst_proj, cmap='gray'), plt.title('Projective Transform')
plt.tight_layout()
plt.show()
