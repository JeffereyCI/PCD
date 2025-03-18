import numpy
import cv2

image_bmp = cv2.imread('starrynight2.bmp')
image_pgm = cv2.imread('starryNight3.pgm')

# showing image
# cv2.imshow('imgae_bmp', image_bmp)
# cv2.imshow('imgae_pgm', image_pgm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# experiment
# custom color
# image_bmp = numpy.zeros((256, 256, 4), dtype=numpy.uint8)
# image_bmp[:] = (255, 0, 0, 50)
# cv2.imwrite("starryNight_blue.png", image_bmp)
# cv2.waitKey(0)

# changing Alpha
# image_pgm = numpy.zeros((256, 256, 3), dtype=numpy.uint8)
# image_pgm[:] = (255, 0, 0,)
# cv2.imshow("transparent.pgm", image_pgm)
# cv2.waitKey(0)
