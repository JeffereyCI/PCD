import cv2

# declarating file for image processing
starryNightImage = cv2.imread("starryNight.jpg") 

# cv2.imshow(‘Original Image’, starryNightImage) -> showing window
# cv2.waitKey(0) -> make not auto close window
# cv2.destroyAllWindows() -> after X make window destroyed

# GRAYSCALE
# gray_image = cv2.cvtColor(starryNightImage, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('starryNight_gray.jpg', gray_image) -> creating file (write)

# GAUSSIAN BLUR
# gaussian_image = cv2.GaussianBlur(starryNightImage, (15, 15), 0)
# cv2.imwrite('starryNight_gaussian.jpg', gaussian_image)

# Canny Edge Detection
# edges_image = cv2.Canny(starryNightImage, 100, 200)
# cv2.imwrite('starryNight_edges.jpg', edges_image)

# invert color
# invert = ~starryNightImage -> simple negation (inverse)
# inverted_image = np.invert(image) -> numpy
# inverted_image = 255 - image -> color arithmetic concept
# inverted_image = cv2.bitwise_not(image) -> works at the bit level by inverting (inverse) each bit of each pixel in the image

# cv2.imwrite('starryNight_invert.jpg', invert)
# cv2.imshow('Original Invert', invert)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# source:
# https://answers.opencv.org/question/3639/subtract-from-white-invert/
# https://builtin.com/software-engineering-perspectives/image-processing-python
# https://chatgpt.com