import numpy as np
from scipy.signal import convolve2d

# 1. Definisi fungsi konvolusi via FFT
def fft_convolution(image, kernel):
    # Padding gambar dan kernel agar ukuran sama
    image_padded = np.zeros((image.shape[0] + kernel.shape[0] - 1, 
                           image.shape[1] + kernel.shape[1] - 1))
    image_padded[:image.shape[0], :image.shape[1]] = image

    kernel_padded = np.zeros_like(image_padded)
    kernel_padded[:kernel.shape[0], :kernel.shape[1]] = kernel

    # Hitung FFT, perkalian spektrum, dan IFFT
    fft_image = np.fft.fft2(image_padded)
    fft_kernel = np.fft.fft2(kernel_padded)
    result = np.fft.ifft2(fft_image * fft_kernel).real  # Ambil bagian real

    return result[:image.shape[0], :image.shape[1]]  # Potong ke ukuran asli

# 2. Contoh penggunaan
image = np.random.rand(256, 256)  # Gambar acak 256x256
kernel = np.ones((3, 3)) / 9     # Kernel blur 3x3 (rata-rata)

# Konvolusi langsung (spatial domain)
conv_direct = convolve2d(image, kernel, mode='same')

# Konvolusi via FFT (frequency domain)
conv_fft = fft_convolution(image, kernel)

# 3. Bandingkan hasil
print("Perbedaan maksimal:", np.max(np.abs(conv_direct - conv_fft)))