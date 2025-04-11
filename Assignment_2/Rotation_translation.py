import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar dan ubah ke grayscale
img = cv2.imread('/home/jechis/Downloads/images.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Ukuran gambar
rows, cols = gray.shape

# Rotasi + Translasi
angle = 45  # derajat rotasi
scale = 1.0
center = (cols / 2, rows / 2)

# Buat matriks rotasi (dengan pusat rotasi di tengah gambar)
M_rot = cv2.getRotationMatrix2D(center, angle, scale)

# Tambahkan translasi manual ke matriks rotasi
tx, ty = 50, 30  # Translasi x dan y
M_rot[0, 2] += tx
M_rot[1, 2] += ty

# Terapkan transformasi rotasi + translasi
dst = cv2.warpAffine(gray, M_rot, (cols, rows))

# Tampilkan hasil
cv2.imshow("Original", gray)
cv2.imshow("Rotated + Translated", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
