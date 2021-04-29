# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:48:52 2021

@author: User
"""

# OpenCV2 동영상 읽기
# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html


# 영상 파일에서 읽어오기
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('https://www.rmp-streaming.com/media/big-buck-bunny-360p.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break    
    cv.imshow('color', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


# 웹캠, 색상 변환
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

