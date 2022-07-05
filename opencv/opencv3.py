import cv2 
import numpy as np

cap = cv2.VideoCapture(0) # 0 1 2 sırasıyla bilgisayara bağlı kameraları temsil eder.
# burada video dosyaso adresi de yazabiliriz.
yuzler = cv2.CascadeClassifier('opencv/cascades/haarcascade_frontalface_default.xml')
gozler = cv2.CascadeClassifier('opencv/cascades/haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bulunanYuzler = yuzler.detectMultiScale(gray, 1.3, 5)
    # yuz => (x,y,w,h)
    for (x,y,w,h) in bulunanYuzler:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        # gozleri bulmak için yuzun içinde bulunan gozleri buluyoruz.
        roigri = gray[y:y+h, x:x+w]
        roirenkli = frame[y:y+h, x:x+w]
        bulunanGozler = gozler.detectMultiScale(roigri, 1.3, 5)
        for (gx,gy,gw,gh) in bulunanGozler:
            cv2.rectangle(roirenkli, (gx,gy), (gx+gw,gy+gh), (0,255,0), 2)
    cv2.imshow("frame", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
