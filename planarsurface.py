import cv2
import numpy as np

imgs = cv2.imread('/home/jechis/Downloads/images.png')

# menentukan koordinat asal
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# menentukan koordinat tujuan
pts2 = np.float32([[70, 80], [220, 60], [70, 230], [220, 220]])

# ambil transformasi matriksnya
M = cv2.getPerspectiveTransform(pts1, pts2)

# perpektif gambar
hasil = cv2.warpPerspective(imgs, M, (imgs.shape[1], imgs.shape[0]))

cv2.imshow("Planar Surface Flow", hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
