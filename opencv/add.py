import cv2

# 웹캠 연결 (기본적으로 0번 웹캠 사용)
cap = cv2.VideoCapture(0)

# 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 ('XVID'는 AVI 형식에 적합)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 파일명, 코덱, FPS, 해상도 설정
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 웹캠에서 영상을 계속 읽고 화면에 출력
while True:
    # 웹캠으로부터 프레임을 읽기
    ret, frame = cap.read()
    
    # 프레임이 제대로 읽히지 않으면 루프 종료
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break
    
    # 프레임을 윈도우에 표시
    cv2.imshow('Webcam Feed', frame)
    
    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release() 
out.release()  # 비디오 저장 중지
cv2.destroyAllWindows()
