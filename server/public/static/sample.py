import cv2

# カメラを起動する
cap = cv2.VideoCapture(0)

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()

    # フレームを表示する
    cv2.imshow('frame', frame)

    # 'q'キーが押されたらループから抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ループが終了したらカメラを解放し、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
