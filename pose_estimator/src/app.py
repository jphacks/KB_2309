import cv2
import numpy as np
import matplotlib.pyplot as plt
from trig import tiltGood, wrapTilt, loadConfig

LINE_SCALE = 30

rec = open('recording/file.csv', 'w')
dump = open('recording/out.csv', 'w')
config = loadConfig('config.csv')

def dumpToFile(data, file):
    line = ""
    for val in range(len(data)):
        line += f"{data[val][1]}"
        line += "\n" if val == len(data) - 1 else ", "
    file.write(line)
    file.flush()
    
newLine = 0

def colCode(stat="na") -> tuple:
    if stat=="na":
        return (0,0,0)
    elif stat == "ok":
        return (0,255,0)
    elif stat == "lo":
        return (0,0,255)
    elif stat == "hi":
        return (255,0,0)

def writeCond(frame, text: tuple, val, stat="na", position=(50,50)):
    global newLine
    if stat != "na":
        cv2.putText(
            frame,
            text + " " + (f"[{val[-1][-1]}]" if stat == "hi" else f"[{val[-1][0]}]" if stat == "lo" else ""),
            (position[0], position[1] + newLine),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            colCode(stat), 2)
        newLine += LINE_SCALE
    

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

threshold = 0.01

inWidth = 320  # Adjust to a lower resolution
inHeight = 240  # Adjust to a lower resolution

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

line = ""
for key in config.keys():
    line += f"{key}, "
line = line[:-2]
line += "\n"    
dump.write(line)

img_list = []
import os
img_dir = 'output_images'
if os.path.exists(img_dir) and os.path.isdir(img_dir):
    img_list = [
        os.path.join(img_dir, file)
        for file in os.listdir(img_dir)
        if os.path.isfile(os.path.join(img_dir, file))]

for img in img_list:
    frame = cv2.imread(img)
    print(f"Processing: {img}")

    # フレームをネットワークの入力形式に変換
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(inpBlob)
    output = net.forward()
    # frameCopy = np.copy(frame)
    H = output.shape[2]
    W = output.shape[3]

    # Empty list to store the detected keypoints
    points = []

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    for i in range(nPoints):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > threshold:
            # cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            # cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
            # cv2.circle(frame, (int(x), int(y)), 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

            points.append((int(x), int(y)))
        else:
            points.append(None)

    # for pair in POSE_PAIRS:
    #     partA = pair[0]
    #     partB = pair[1]

    #     if points[partA] and points[partB]:
    #         cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3)

    collect = []
    for key, val in config.items():
        check = tiltGood(points, val)
        # writeCond(frame, f"{key}: {wrapTilt(points, val):.2f}", val, check)
        collect.append([key, check])
    dumpToFile(collect, dump)
    
    # newLine = 0
    
    # cv2.imshow('Skeleton', frame)

cv2.destroyAllWindows()

print("code finish")