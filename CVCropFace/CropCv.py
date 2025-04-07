import cv2
img = cv2.imread('1.png')
import cv2

# Pastikan jalur ke Haar cascade benar
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

face = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3)

for x,y,w,h in face :
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    face = img[y:y+h, x:x+w]

    cv2.imwrite('f.png',face)
    cv2.imwrite('f2.png',img)