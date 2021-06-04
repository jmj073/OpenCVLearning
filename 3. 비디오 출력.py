import cv2

#동영상 파일 설정
cap = cv2.VideoCapture("image/3.mp4")

# 6초 동안 반복
while cv2.waitKey(6) < 0:
    # 현재 동영상의 프레임 수와 동영상의 총 프레임 수를 받아온다.
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_POS_FRAMES):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # read() 카메라 상태와 프레임을 받아온다.
    ret, frame = cap.read()
    cv2.imshow("VideoFrame", frame)

# 메모리 헤제
cap.release()
# 모든 윈도우 창 제거
cv2. destroyAllWindows()