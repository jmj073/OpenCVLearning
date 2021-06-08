import cv2
# 이미지 경로 설정
src = cv2.imread("image/8.jpg", cv2.IMREAD_COLOR)
"""
 이미지를 src[높이, 너비]로 관심영역을 설정한 뒤 deep copy로 가져온다.
 Deep Copy를 사용하지 않을 경우(shallow copy)원본 이미지 또한 원본도 영향을 받게 된다.
 dst = src[100:600, 200:700].copy()
"""

# src를 Deep Copy 해온다.
# Shallow Copy를 사용할 경우 dst 이미지와 src 이미지는 동일힌 결과로 반환됩니다.
dst = src.copy()
# roi 이미지를 생성해서 src[높이, 너비]로 관심 영역을 설정합니다.
roi = src[100:600, 200:700]
# dst[높이, 행] = roi를 이용해서 dst 이미지에 해당 영역을 붙여 넣을 수 있다
dst[0:500, 0:500] = roi

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()