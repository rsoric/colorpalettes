import cv2

im = cv2.imread('parrot.png')
cv2.imshow("Image", im)
cv2.waitKey(0)