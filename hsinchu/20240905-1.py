import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(540,320))              # 縮小尺寸，避免尺寸過大導致效能不好
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()