import cv2
import numpy


i = 3

photo = cv2.imread(str(i) + ".jpg")
photo = cv2.resize(photo, (150, 300))
cv2.imshow(str(i), photo)

cutedPhoto = photo[20:272, 50:120]
# cv2.imshow("cutedPhoto" + str(i), cutedPhoto)

hsv = cv2.cvtColor(cutedPhoto, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2]
cv2.imshow("v" + str(i), v)

red_sum = numpy.sum(v[0:63, 0:68])
yellow_sum = numpy.sum(v[84:147, 0:68])
green_sum = numpy.sum(v[180:243, 0:68])

cv2.rectangle(cutedPhoto, (0, 0), (68, 63), (0, 0, 255), 2)
cv2.rectangle(cutedPhoto, (0, 84), (68, 155), (0, 255, 255), 2)
cv2.rectangle(cutedPhoto, (0, 180), (68, 250), (0, 255, 0), 2)
cv2.imshow("FrameCopy" + str(i), cutedPhoto)

print("красн. массив " + str(red_sum) + " | " + "жёлт. масив " + str(yellow_sum) + " | " + "зел. массив " + str(green_sum))

if green_sum > yellow_sum and green_sum > red_sum:
    print("зелёный")
elif yellow_sum > green_sum and yellow_sum > red_sum:
    print("жёлтый")
elif red_sum > green_sum and red_sum > yellow_sum:
    print("красный")
else:
    print("красный")

while True:
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
