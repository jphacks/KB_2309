import cv2
import time
import numpy as np
import matplotlib.pyplot as plt


MODE = "COCO"

if MODE is "COCO":
    protoFile = "learnopencv/OpenPose/pose/coco/pose_deploy_linevec.prototxt"
    weightsFile = "learnopencv/OpenPose/pose/coco/pose_iter_440000.caffemodel"
    nPoints = 5
    POSE_PAIRS = [[1, 0], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [1, 8], [8, 9]]


elif MODE is "MPI" :
    protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "pose/mpi/pose_iter_160000.caffemodel"
    nPoints = 15
    POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]



cap = cv2.VideoCapture(0)
desired_fps = 10
cap.set(cv2.CAP_PROP_FPS, desired_fps)

frameWidth = int(cap.get(3))
frameHeight = int(cap.get(4))
threshold = 0.01


inWidth = 320  # Adjust to a lower resolution
inHeight = 240  # Adjust to a lower resolution


net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

while True:
    ret, frame = cap.read()  # ビデオからフレームを読み込む
    if not ret:
        break

    # フレームをネットワークの入力形式に変換
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()
    frameCopy = np.copy(frame)
    H = output.shape[2]
    W = output.shape[3]

    # Empty list to store the detected keypoints
    points = []

    for i in range(nPoints):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > threshold:
            cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(x), int(y)), 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

            points.append((int(x), int(y)))
        else:
            points.append(None)

    # for pair in POSE_PAIRS:
    #     partA = pair[0]
    #     partB = pair[1]

    #     if points[partA] and points[partB]:
    #         cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3)

    cv2.imshow('Skeleton', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("code finish")


