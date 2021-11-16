import cv2
import numpy
#
# img = cv2.imread("C:/Users/Wee66_/Documents/GitHub/Syomin_2020/maxresdefault.jpg")  # ввод картинки в программу
#
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # пропорциоальное сжатие
# # img = cv2.GaussianBlur(img, (9, 9), 0)  # размытие картинки
# # img[0:100, 0:150]  # обрезание картинки
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # перевод картинки в серо-белый формат
#
# # img = cv2.Canny(img, 320, 320)  # бинарный формат картинки, работает идеально в связке с переводом картинки в серо-белый формат
# # kernal = np.ones((5, 5), np.uint8)  # параметр обводки
# # img = cv2.dilate(img, kernal, iterations=1)  # метод обводки, где iterations это количество обводки, работает c бинарными изображениями
# # img = cv2.erode(img, kernal, iterations=1)  # уменьшение обводки
#
# cv2.imshow("img", img)  # показ картинки
# cv2.waitKey(0)  # время показа картинки, 0  по умолчанию будет показывать картинку бесконечно


i = 1

img = cv2.imread(str(i) + ".jpg")
cv2.namedWindow("out_window")

height, width = img.shape[:2]
edge = 10

low_blue = numpy.array((90, 20, 20), numpy.uint8)
high_blue = numpy.array((150, 255, 255), numpy.uint8)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask_blue = cv2.inRange(img_hsv, low_blue, high_blue)

result = cv2.bitwise_and(img_hsv, img_hsv, mask=mask_blue)
result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

moments = cv2.moments(mask_blue, 1)

dM01 = moments['m01']
dM10 = moments['m10']
dArea = moments['m00']

x = 0

if dArea > 150:
    x = int(dM10 / dArea)
    y = int(dM01 / dArea)
    cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

if (x>(width/2+edge)) and x != 0:
    cv2.rectangle(img, (0, 0), (30, height), (0, 255, 0), -1)
if (x<(width/2-edge)) and x != 0:
    cv2.rectangle(img, (width-30, 0), (width, height), (0, 255, 0), -1)

cv2.imshow("img", img)
cv2.waitKey(0)
