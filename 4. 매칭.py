import cv2

# 로컬 파일에서 이미지 불러오기
src = cv2.imread("image/4.jpg", cv2.IMREAD_COLOR)
# cv2.flip(이미지, flipcode) 이미지 대칭하기
# 매칭 축(flipcode)을 기준으로 출력한 이미지를 반환하는 코드
dst = cv2.flip(src, 0)
"""
대칭 축은 상수를 입력해 대칭할 축을 설정할 수 있습니다.
flipCode < 0은 XY축 대칭 (상하좌우 대칭)
flipCode = 0은 X축 대칭 (상하 대칭)
flipCode > 0은 Y축 대칭 (좌우 대칭)
"""

# 이미지 출력
cv2.imshow("src", src)
cv2.imshow("dst", dst)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()