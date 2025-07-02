import cv2
import matplotlib.pyplot as plt

# Baca gambar dan ubah ke grayscale
imgs = cv2.imread('/home/jechis/Downloads/images.png')

# Hitung histogram (3 channel, dari 0 sampai 256) (berwarna/gbr)
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([imgs], [i], None, [256], [0, 256])
    plt.title("Histogram rgb")
    plt.xlabel("Intensitas Pixel")
    plt.ylabel("Jumlah")
    plt.grid(True)
    plt.plot(hist, color=color)
    
# Tampilkan hasil
plt.show()


# histogram 1 channel (gray)
# Baca gambar dan ubah ke grayscale
img = cv2.imread('/home/jechis/Downloads/images.png', cv2.IMREAD_GRAYSCALE)

# Hitung histogram (1 channel, dari 0 sampai 256)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Tampilkan hasil
plt.figure(figsize=(8, 4))
plt.title("Histogram Grayscale")
plt.xlabel("Intensitas Pixel")
plt.ylabel("Jumlah")
plt.plot(hist, color='gray')
plt.xlim([0, 256])
plt.grid(True)
plt.show()
