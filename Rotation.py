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

