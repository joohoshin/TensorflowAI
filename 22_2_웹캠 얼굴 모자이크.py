# cvlib를 통해 손쉽게 얼굴 디텍션 가능함
# https://www.cvlib.net/
# anaconda console에서 pip install cvlib 로 설치하세요

# 로컬에서 cudart64_110.dll 관련 오류가 뜨면 아래의 cuda 라이브러리를 설치하세요 
# 그래픽카드 드라이버(nvidia)입니다.
# https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal

import cvlib as cv
import cv2
 
# open webcam
webcam = cv2.VideoCapture(0)
 
if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    
 
# loop through frames
while webcam.isOpened():
 
    # read frame from webcam 
    status, frame = webcam.read()
 
    if not status:
        print("Could not read frame")
        exit()
 
    # apply face detection
    face, confidence = cv.detect_face(frame)
 
    print(face)
    print(confidence)
 
    # loop through detected faces
    for idx, f in enumerate(face):
        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]
 
        '모자이크 효과 주기: 얼굴 부분을 줄였다가 다시 원크기로 복구시키면 모자이크처럼 됨.'
        face_region = frame[startY:endY, startX:endX]
        
        M = face_region.shape[0]
        N = face_region.shape[1]
 
        face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
        face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
        frame[startY:endY, startX:endX] = face_region
 
    # display output
    cv2.imshow("Real-time face detection", frame)
 
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows() 
