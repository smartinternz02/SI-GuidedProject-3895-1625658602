import numpy as np
import cv2
# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# Initiate video capture for video file
cap = cv2.VideoCapture('moskva.mov')
# Loop once video is successfully loaded
while cap.isOpened():
    
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.1, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)
        cv2.putText(frame,'PEDESTRIANS',(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1)
    if cv2.waitKey(1) == ord('q'): #13 is the Enter Key
        cap.release()
        cv2.destroyAllWindows()
        break
