import cv2
import numpy as np
import matplotlib.pyplot as plt
from trig import tiltGood, getTilt

CAPTURE_FILE = 0 #"video/test_video_tilted.mp4"
LINE_SCALE = 50

rec = open('recording/file.csv', 'w')

from io import TextIOWrapper
def writeOnFile(data, file):
    line = ""
    for point in range(len(data)):
        if data[point]:
            line += f"({data[point][0]}; {data[point][1]})"
        else:
            line += "(None; None)"
        line += ("\n" if point == (len(data) - 1) else ", ")
    file.write(line)
    file.flush()
    
newLine = 0

def writeCond(frame, text: tuple, good=0, position=(50,50)):
    global newLine
    if good > -1:
        print(f"{'good' if good > 0 else 'bad'}\t\t", end="")
        cv2.putText(frame, text, (position[0], position[1] + newLine), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0) if good > 0 else (0,0,255), 2)
        newLine += LINE_SCALE
    else:
        print("\t\t", end="")
    

protoFile = "model/pose_deploy_linevec.prototxt"
weightsFile = "model/pose_iter_440000.caffemodel"
nPoints = 18
POSE_PAIRS = [[1,0] # neck-head

            ,[0,14] # head-eye right
            ,[14,16] # eye-ear rigt
            
            ,[0,15] # head-eye left
            ,[15,17] # eye-ear left
              
            ,[1,2] # neck-shoulder right
            ,[2,3] # shoulder-elbow right
            ,[3,4] # elbow-wirst right
              
            ,[1,8] # neck-hip right
            ,[8,9] # hip-knee right
            ,[9,10] # knee-ankle right
            
            ,[1,5] # neck-shoulder left
            ,[5,6] # shoulder-elbow left
            ,[6,7] # elbow-wirst left
            
            ,[1,11] # neck-hip left
            ,[11,12] # hip-knee left
            ,[12,13] # knee-ankle left
]

# TODO: add handling for frontal camera
cap = cv2.VideoCapture(CAPTURE_FILE)
desired_fps = 10
cap.set(cv2.CAP_PROP_FPS, desired_fps)

frameWidth = int(cap.get(3))
frameHeight = int(cap.get(4))
threshold = 0.01


inWidth = 320  # Adjust to a lower resolution
inHeight = 240  # Adjust to a lower resolution


net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

print("head_tilt\tneck_tilt\tshoulders")

while cap.isOpened():
    ret, frame = cap.read()  # ビデオからフレームを読み込む
    if not ret:
        break

    # フレームをネットワークの入力形式に変換
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()
    # frameCopy = np.copy(frame)
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
            # cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            # cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(x), int(y)), 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

            points.append((int(x), int(y)))
        else:
            points.append(None)

    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3)

    neck_good = tiltGood((points[1], points[0]), 90, 8)     
    writeCond(frame, f"Neck: {getTilt(points[1],points[0]):.2f}:{90}", neck_good)
    
    left_should_good = tiltGood((points[2], points[5]), 0, 6)
    writeCond(frame, f"Shoulder left: {getTilt(points[1],points[5]):.2f}:{0}", left_should_good)
    
    head_good = tiltGood((points[16], points[17]), 0, 6)
    writeCond(frame, f"Head tilt: {getTilt(points[16],points[17]):.2f}:{0}", head_good)
    
    print("")
    newLine = 0
    
    # cv2.imshow('Skeleton', frame)
    # writeOnFile(points, rec)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("code finish")