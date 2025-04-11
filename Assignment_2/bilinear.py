import cv2
import numpy as np

imgs = cv2.imread('/home/jechis/Downloads/images.png')

# menentukan titik affine
M = np.float32([[1.2, 0.3, 0],  # Horizontal shear + scaling
                [0.3, 1.5, 0]]) # Vertical shear + scaling

# menggunakan affine
result = cv2.warpAffine(imgs, M, (imgs.shape[1], imgs.shape[0]), flags=cv2.INTER_LINEAR)

cv2.imshow("Bilinear Interpolation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
