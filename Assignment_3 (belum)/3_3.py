import numpy as np
import matplotlib.pyplot as plt

# 1. Buat gambar contoh: garis vertikal
image = np.zeros((100, 100))  # Gambar 100x100 piksel hitam
image[:, 50] = 1  # Garis vertikal putih di kolom ke-50

# 2. Hitung FFT 2D
fft = np.fft.fft2(image)  # Transformasi Fourier 2D
fft_shifted = np.fft.fftshift(fft)  # Memindahkan frekuensi nol ke tengah
magnitude = np.log(np.abs(fft_shifted))  # Magnitudo spektrum (di-log untuk visualisasi)

# 3. Plot hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Gambar Asli (Garis Vertikal)")

plt.subplot(1, 2, 2)
plt.imshow(magnitude, cmap='gray')
plt.title("Spektrum FFT")
plt.colorbar()
plt.show()