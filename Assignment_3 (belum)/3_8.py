import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon, iradon
from skimage.draw import line

# 1. Buat gambar dengan garis diagonal
image = np.zeros((100, 100))
rr, cc = line(0, 0, 99, 99)  # Garis dari (0,0) ke (99,99)
image[rr, cc] = 1  # Gambar garis putih

# 2. Hitung Transformasi Radon
theta = np.linspace(0., 180., 180, endpoint=False)  # Sudut 0-180 derajat
sinogram = radon(image, theta=theta)  # Hasil Radon

# 3. Ekstrak maxima (garis dominan)
max_angle = theta[np.argmax(np.max(sinogram, axis=0))]  # Sudut dengan intensitas maks
print("Sudut garis dominan:", max_angle)

# 4. Visualisasi
plt.figure(figsize=(12, 4))
plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title("Gambar Asli")
plt.subplot(132), plt.imshow(sinogram, cmap='gray'), 
plt.title(f"Sinogram (Garis dominan: {max_angle:.1f}°")
plt.subplot(133), plt.imshow(iradon(sinogram, theta=theta), cmap='gray'), 
plt.title("Rekonstruksi dari Radon")
plt.show()