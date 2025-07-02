from skimage import io
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Membaca gambar
img = io.imread('coin_jpg.jpg')  # Ganti dengan path gambar yang digunakan

# Mendapatkan dimensi asli gambar
rows, cols, channels = img.shape

# Mengubah gambar ke bentuk array 2D (setiap piksel = vektor RGB)
img_2d = img.reshape(rows * cols, channels)

# Menjalankan KMeans clustering dengan jumlah klaster 3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(img_2d)

# Mendapatkan label klaster untuk setiap piksel
labels = kmeans.labels_

# Mengubah label menjadi tampilan segmentasi (klaster ke warna)
segmented_img = kmeans.cluster_centers_[labels].reshape(rows, cols, channels).astype(np.uint8)

# Menampilkan gambar asli dan hasil segmentasi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Gambar Asli')

plt.subplot(1, 2, 2)
plt.imshow(segmented_img)
plt.title('Segmentasi dengan K-Means')

plt.show()
