import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmlist = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        print(lmlist[4])


    cv2.imshow("Video", img)
    cv2.waitKey(1)