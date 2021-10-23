import cv2
import os
import sys

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

while True:

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    if k%256 == 32:
        path = os.getcwd()
        path = path + "/main/img/"
        os.chdir(path)
        img_name = sys.argv[1] + ".jpg"
        cv2.imwrite(img_name, frame)
        os.chdir("../../")
        break


cam.release()
cv2.destroyAllWindows()