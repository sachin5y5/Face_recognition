import cv2
import numpy as np

# url = "http://192.168.43.157:8080/video"
# cap = cv2.VideoCapture(url)


# Access video feed
cap = cv2.VideoCapture(0)  # Change '0' to the camera ID if multiple cameras are used

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Classroom Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
