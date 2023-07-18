import cv2
import mediapipe
import time
import HandTrackingModule as htm

wCam, hCam = 640, 640
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = htm.handDetector()

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    img = detector.findHands(img, draw=True)
    lmlist = detector.findPosition(img, draw=False)
    #print(lmlist)
    # CODE FOR 1st FINGER
    #if len(lmlist) != 0:
     #   if lmlist[8][2] < lmlist[6][2]:
      #      print("Index finger is open")


    if len(lmlist) != 0:
        fingers = []

        # Thumb
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)


        # Logic for all 4 fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)
        totalfingers = fingers.count(1)
        print(totalfingers)

        cv2.putText(img, str(totalfingers), (45, 175), cv2.FONT_ITALIC, 5, (255,0,0), 10 )

        cTime = time.time()  # current time
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    1, (255, 0, 139), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
