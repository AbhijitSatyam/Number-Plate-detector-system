import cv2
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count=0
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlate= nPlateCascade.detectMultiScale(imgGray, 1.1, 5)
    for (x, y, w, h) in numberPlate:
        if w*h>500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 150, 0), 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_PLAIN,2,(150,10,255),2)
            imgROI=img[y:y+h,x:x+w]
            cv2.imshow("numberPlate",imgROI)
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Resources/ScannednPlate/NoPlate_ "+str(count)+".jpg",imgROI)
        NOplate= cv2.imread("Resources/ScannednPlate/NoPlate_ "+str(count)+".jpg")
        cv2.resize(NOplate,(200,1000),interpolation=cv2.INTER_LINEAR)
        cv2.imshow("Plate",NOplate)
        cv2.waitKey(500)
        count += 1