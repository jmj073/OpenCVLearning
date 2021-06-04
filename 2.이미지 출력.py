import cv2

image = cv2.imread("image/2.jpg", cv2.IMREAD_ANYCOLOR)
"""
cv2.IMREAD_UNCANGED : 원본 사용
cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
cv2.IMREAD_COLOR: 3 채널, BGR 이미지 사용
cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1채널, 1/2 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1채널, 1/4 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1채널, 1/8 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용
"""

#이미지 표시하기
cv2.imshow("image", image)
# 키 입력 대기함수
cv2.waitKey()
cv2.destroyWindow()

#높이 너비 채널 확인하기
height, width, channel = image.shape
print(height, width, channel)