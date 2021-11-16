import cv2
import numpy as np
import matplotlib.pyplot as plt
i = 8

img = cv2.imread(str(i) + ".jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array((19, 61, 132), np.uint8)
upper = np.array((19, 95, 198), np.uint8)

img = cv2.inRange(img, lower, upper)
img = cv2.resize(img, (200, 300))
cv2.imshow("", img)
cv2.waitKey(0)
###
