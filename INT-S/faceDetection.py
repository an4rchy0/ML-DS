import cv2
import sys

casPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
fasCascade = cv2.CascadeClassifier(casPath)

vidCapture = cv2.VideoCapture(0)

if not vidCapture.isOpened():
    print("Error: Could not open video device")
    sys.exit(1)

while True:
    ret, frame = vidCapture.read()
    if not ret:
        print("Error: Could not read frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fasCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vidCapture.release()
cv2.destroyAllWindows()
