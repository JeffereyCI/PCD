import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca gambar dan ubah ke grayscale
img = cv2.imread('/home/jechis/Downloads/images.png')  # Pastikan file ada dan formatnya benar
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Dapatkan ukuran gambar
rows, cols = gray.shape

# Tentukan 3 titik sebelum dan sesudah transformasi
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Matriks transformasi Affine
M_affine = cv2.getAffineTransform(pts1, pts2)

# Terapkan transformasi
dst_affine = cv2.warpAffine(gray, M_affine, (cols, rows))

# Tampilkan hasil
cv2.imshow("Original", gray)
cv2.imshow("Affine Transformation", dst_affine)
cv2.waitKey(0)
cv2.destroyAllWindows()
