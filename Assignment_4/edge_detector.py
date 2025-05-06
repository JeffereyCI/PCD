import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

# Load grayscale image
gray = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Roberts
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])
edge_roberts = np.sqrt(
    ndimage.convolve(gray.astype(float), roberts_x)**2 +
    ndimage.convolve(gray.astype(float), roberts_y)**2
)

# Laplace
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Prewitt
prewitt_x = ndimage.convolve(gray.astype(float), np.array([[1,0,-1],[1,0,-1],[1,0,-1]]))
prewitt_y = ndimage.convolve(gray.astype(float), np.array([[1,1,1],[0,0,0],[-1,-1,-1]]))
prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)

# Sobel
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobel_x**2 + sobel_y**2)

# Robinson (4 arah)
robinson_kernels = [
    np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),
    np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]]),
    np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
    np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
]
robinson = np.max([cv2.filter2D(gray, -1, k) for k in robinson_kernels], axis=0)

# Kirsch (8 arah)
kirsch_kernels = [
    np.array([[-3,-3,5],[-3,0,5],[-3,-3,5]]),
    np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]]),
    np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]]),
    np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]]),
    np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]]),
    np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]]),
    np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]]),
    np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])
]
kirsch = np.max([cv2.filter2D(gray, -1, k) for k in kirsch_kernels], axis=0)

# Canny
canny = cv2.Canny(gray, 100, 200)

# Display all
titles = ['Roberts', 'Laplace', 'Prewitt', 'Sobel', 'Robinson', 'Kirsch', 'Canny']
images = [edge_roberts, laplacian, prewitt, sobel, robinson, kirsch, canny]

plt.figure(figsize=(14, 8))
for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
