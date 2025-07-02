import cv2
import matplotlib
from matplotlib import pyplot as plt

img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

equalized_img = cv2.equalizeHist(img)

# Plot
plt.figure(figsize=(10,4))
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1,2,2), plt.imshow(equalized_img, cmap='gray'), plt.title('Histogram Equalized')
plt.tight_layout()
plt.show()
