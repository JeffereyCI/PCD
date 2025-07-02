from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt

# 1. Baca gambar dan reshape untuk K-Means
image = cv2.imread('coin_jpg.jpg')  # Ganti dengan path gambar
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixels = image_rgb.reshape((-1, 3))  # Reshape jadi (N_piksel, 3 channel)

# 2. Clustering warna dengan K-Means
kmeans = KMeans(n_clusters=3)  # 3 cluster warna
kmeans.fit(pixels)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 3. Hasil segmentasi
segmented = centers[labels].reshape(image_rgb.shape).astype('uint8')

# 4. Plot hasil
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image_rgb), plt.title("Gambar Asli")
plt.subplot(122), plt.imshow(segmented), plt.title("Hasil Segmentasi (K=3)")
plt.show()