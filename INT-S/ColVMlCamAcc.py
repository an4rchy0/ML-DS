import cv2 
import numpy as np

#define color range to detect (in HSV format)
lower_color = np.array([0,100,100])
upper_color = np.array([10,255,255])
#initialize the camera
cap = cv2.VideoCapture(0)

while True:
    #capture frame by frame
    ret, frame = cap.read()
    #convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #create mask to detect specified color 
    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    #find contours in the mask 
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #draw contours on original frame
    for contour in contours:
        cv2.drawContours(frame, [contour], -1, (0,255,0), 2)
    
    #display frame with detection color
    cv2.imshow('Color Detection dek', frame)

    #break loop if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

#realease camera and close all windows
cap.release()
cv2.destroyAllWindows()