import cv2
import numpy as np

imgs = cv2.imread('/home/jechis/Downloads/images.png')

# pakai sobel filter untuk co-vector
# Sobel operator untuk menghitung gradien dalam arah X dan Y
grad_x = cv2.Sobel(imgs, cv2.CV_64F, 1, 0, ksize=3)  # Gradien X (horizontal)
grad_y = cv2.Sobel(imgs, cv2.CV_64F, 0, 1, ksize=3)  # Gradien Y (vertikal)

# Magnitude dan arah gradien (co-vector)
magnitude = cv2.magnitude(grad_x, grad_y)  # Magnitude gradien
angle = cv2.phase(grad_x, grad_y, angleInDegrees=True)  # Arah gradien dalam derajat

cv2.imshow("Magnitude of Gradients", magnitude)
cv2.imshow("Angle of Gradients", angle)

cv2.waitKey(0)
cv2.destroyAllWindows()