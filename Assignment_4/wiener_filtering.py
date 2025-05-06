import cv2
import numpy as np
from skimage.restoration import wiener
from matplotlib import pyplot as plt

# Load the image (grayscale)
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Cek apakah gambar berhasil dimuat
if image is None:
    print("Gambar tidak ditemukan atau tidak dapat dibaca.")
    exit()

# Apply Wiener Filtering dengan balance
# Kernel size adalah (5, 5) dan balance diatur ke 0.1 (dapat diubah)
balance = 0.1
wiener_filtered_image = wiener(image, np.ones((5, 5)), balance=balance)

# Display the result
plt.figure(figsize=(6, 6))
plt.imshow(wiener_filtered_image, cmap='gray')
plt.title('Wiener Filtering')
plt.axis('off')
plt.show()
