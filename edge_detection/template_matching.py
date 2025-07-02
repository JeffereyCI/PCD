import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'clown.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
template = img[100:150, 100:150]  

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

h, w = template.shape[:2]
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title('Template')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Hasil Matching')
plt.axis('off')
plt.tight_layout()
plt.show()