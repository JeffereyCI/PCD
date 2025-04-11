import cv2
import numpy as np

imgs = cv2.imread('/home/jechis/Downloads/images.png')

M = np.float32([[2, 0, 0],   # posisi x
                [0, 0.5, 0]]) # posisi y

# affine
hasil = cv2.warpAffine(imgs, M, (imgs.shape[1], imgs.shape[0]))

cv2.imshow("Stretch/Squash", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
