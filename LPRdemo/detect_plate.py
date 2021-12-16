import cv2
import numpy as np

license_plate = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture(0)


while True:
    success, frames = cap.read()
    imgGray =cv2.cvtColor(frames, cv2.COLOR_BGR2BGRA)

    plate = license_plate.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in plate:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Video", frames)

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break