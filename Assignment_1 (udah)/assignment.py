import numpy
import cv2

image_bmp = cv2.imread('starryNight2.bmp')
image_pgm = cv2.imread('starryNight3.pgm')
image_jpg = cv2.imread('starryNight.jpg')

# showing image
# cv2.imshow('image_bmp', image_bmp)
# cv2.imshow('image_pgm', image_pgm)
# cv2.imshow('image_jpg', image_jpg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# experiment
# custom color
# image_bmp = numpy.zeros((256, 256, 4), dtype=numpy.uint8)
# image_bmp[:] = (255, 0, 0, 50)
# cv2.imwrite("starryNight_blue.jpg", image_bmp)
# cv2.waitKey(0)

# image_jpg = numpy.zeros((256, 256, 3), dtype=numpy.uint8)
# image_jpg[:] = (0, 0, 255)
# cv2.imshow('gambar jpg', image_jpg)
# cv2.imwrite('starryNight_JPGtoBMP-RED.bmp', image_jpg)
# cv2.waitKey(0)

# image_jpg = numpy.zeros((256, 1), dtype=numpy.uint8)
# image_jpg[:] = (255)
# # cv2.imshow('gambar jpg', image_jpg)
# cv2.imwrite('starryNight_JPGtoPGM-BLUE.pgm', image_jpg)
# cv2.waitKey(0)

# changing Alpha
# image_pgm = numpy.zeros((256, 256, 3), dtype=numpy.uint8)
# image_pgm[:] = (255, 0, 0,)
# cv2.imshow("transparent.pgm", image_pgm)
# cv2.waitKey(0)

# grayscale
# image = cv2.imread('starryNight.jpg')
# image = numpy.zeros((256, 256), dtype=numpy.uint8)

# # Tentukan warna grayscale untuk tiap bagian
# gray_values = [150, 255, 100, 200]  # 4 warna berbeda

# Bagi gambar menjadi 4 bagian dan isi dengan warna berbeda
# image[:128, :128] = gray_values[0]  # Kiri atas
# image[:128, 128:] = gray_values[1]  # Kanan atas
# image[128:, :128] = gray_values[2]  # Kiri bawah
# image[128:, 128:] = gray_values[3]  # Kanan bawah

# cv2.imwrite('experimen.pgm', image)

# membuat gambar default dengan ukuran custom (tidak read)
# image = numpy.zeros((839, 748), dtype=numpy.uint8)
# cv2.imwrite("gambar.jpg", image)
# print(image.shape)

# membuat grid gambar custom
# image_grid = numpy.zeros((256, 256, 3), dtype=numpy.uint8)
# image_grid[:, 64] = [255, 0, 0]
# image_grid[:, 192] = [0, 255, 0]
# image_grid[128, :] = [0, 255, 0]
# image_grid[64, :] = [255, 0, 0]
# image_grid[192, :] = [0, 0, 255]
# image_grid[:, 128] = [0, 0, 255]
# cv2.imshow('gambar grid', image_grid)
# cv2.imwrite('gambar_grid.jpg', image_grid)
# cv2.waitKey(0)