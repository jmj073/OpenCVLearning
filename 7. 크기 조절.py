import cv2

# 이미지 경로 설정
src = cv2.imread("image/7.jpg", cv2.IMREAD_COLOR)

# 이미지 크기 조절 함수
"""cv2.resize(src, dstSize, fx, fy, interpolation)
: 입력이미지(src), 절대 크기(dstSize), 상대 크기(fx, fy), 보간법(interpolation)으로 출력이미지(dst)를 생성한다."""
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
# 키 입력 대기 함수
cv2.waitKey()
# 윈도우 창 제거 함수
cv2.destroyWindow()
