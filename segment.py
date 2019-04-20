import cv2
import numpy as np



img1 = cv2.imread("/Users/zrain/Desktop/scshot/pic7.png")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)





cv2.namedWindow("match", cv2.WINDOW_NORMAL)
cv2.imshow("match", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()