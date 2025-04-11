import cv2

imgs = cv2.imread('/home/jechis/Downloads/images.png')

# gray
gray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray.jpg', gray)

# hsv
# cv2.waitKey(0)
hsv = cv2.cvtColor(imgs, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv.jpg', hsv)
# cv2.waitKey(0)

# rgb
rgb = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb.jpg', rgb)
cv2.waitKey(0)

cv2.destroyAllWindows()