import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


ret, old = cap.read()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(cv.subtract(old, frame),cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', cv.flip(gray, 1))
    if cv.waitKey(1) == ord('q'):
        break
    old = frame
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()