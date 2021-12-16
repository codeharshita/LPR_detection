import cv2
##########################################
frameWidth = 640
frameHeight = 480
minArea = 800
color= (255,0,255)
plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
##########################################

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
count = 0

while True:
    _, frames = cap.read()
    imgGray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    numberPlate = plateCascade.detectMultiScale(imgGray, 1.1,4)

    for (x, y, w,h) in numberPlate:
        area= w*h
        if area>minArea:
            cv2.rectangle(frames, (x,y), (x+w, y+h), (255,0,255), 3)
            cv2.putText(frames, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            #TO EXTRACT THE REGION WE WANTED
            imgRoi=frames[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Video", frames)

    if cv2.waitKey(1) & 0xFF ==ord('s'):
        #cv2.imwrite("Resources/Scanned/NoPlate_"+ str(count)+".jpg",imgRoi)
        cv2.imwritemulti("LPRdemo/Scanned/NoPlate_"+ str(count)+ ".jpg",imgRoi)
        cv2.rectangle(frames,(0,200),(640,300),(0,255,0), cv2.FILLED)
        cv2.putText(frames, "Scan Saved", (150,265),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,0,255),2)
        cv2.imshow("RESULT", frames)
        cv2.waitKey(500)
        count +=1