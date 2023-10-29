import numpy as np

def backLegsAngle(points):
    
    knee_left = np.array(points[12])
    knee_right = np.array(points[9])
    hip_left = np.array(points[11])
    hip_right = np.array(points[8])
    neck = np.array(points[1])
    
    leg_left = knee_left - hip_left
    leg_right = knee_right - hip_right
    legs = (leg_left + leg_right) / 2
    h = np.array([1,0])
    
    low_back = (hip_left + hip_right) / 2
    back = neck - low_back
    
    m_b = np.linalg.norm(back)
    m_l = np.linalg.norm(legs)
    m_h = np.linalg.norm(h)
    dot_product_b = np.dot(back, h)
    dot_product_l = np.dot(legs, h)
    
    return (np.degrees(np.arccos(dot_product_b / (m_b * m_h))),np.degrees(np.arccos(dot_product_l / (m_l * m_h))))

def shouldersNeck(points):
    
    head = np.array(points[0])
    neck_base = np.array(points[1])
    up = head - neck_base
    shoulder_right = np.array(points[2])
    right = shoulder_right - neck_base
    shoulder_left = np.array(points[5])
    left = shoulder_left - neck_base
    h = np.array([1,0])
    
    m_l = np.linalg.norm(left)
    m_r = np.linalg.norm(right)
    m_u = np.linalg.norm(up)
    m_h = np.linalg.norm(h)
    
    dot_product_l = np.dot(left, h)
    dot_product_r = np.dot(right, h)
    dot_product_u = np.dot(up, h)
    
    return (
        np.degrees(np.arccos(dot_product_l / (m_l * m_h))),
        np.degrees(np.arccos(dot_product_r / (m_r * m_h))),
        np.degrees(np.arccos(dot_product_u / (m_u * m_h))))

def getTilt (pointA, pointB):
    if pointA and pointB:
        line = np.array(np.array(pointB) - np.array(pointA))
        h = np.array([1,0])
        m_l = np.linalg.norm(line)
        m_h = np.linalg.norm(h)
        dot_product = np.dot(line, h)
        return np.degrees(np.arccos(dot_product / (m_l * m_h)))
    return 0

def wrapTilt(points, val):
    pointA, pointB = points[val[0]], points[val[1]]
    return getTilt(pointA, pointB)

def getTriTilt(pointA, pointB, pointC):
    firstLine = getTilt(pointB, pointA)
    secondLine = getTilt(pointB, pointC)
    return firstLine - secondLine

def tiltGood(points: tuple, val: tuple) -> int:
    """check if the line is close to a certain angle within a treshold

    Args:
        line (tuple): containing the two points
        tt (tuple): float, float target and treshold
        treshold (float, optional): angle treshold (deg). Defaults to 5.0.

    Returns:
        int: tribool:
        - 1: in treshold
        - 0: out treshold
        - -1: not detected
    """
    id1, id2, target, treshold = val
    A, B = points[id1], points[id2]
    if A and B:
        angle = wrapTilt(points, val)
        return 1 if angle < target + treshold and angle > target - treshold else 0
    return -1

def loadConfig(filename):
    conf = {}
    with open(filename, newline='') as csvfile:
        for line in csvfile:
            val = line.split(",")
            if len(val) != 5: print(f"Config Error, specify 5 values (name, pointA, pointB, target, treshold)\nFound\"{line}\""); exit(1)
            conf[val[0].replace(" ", "")] = (int(val[1]), int(val[2]), float(val[3]), float(val[4]))
    return conf
            

def to_joints(list):
    joints_list = np.array(list)
    print(joints_list)
    joints = {}
    joints["head"] = joints_list[0]
    joints["neck"] = joints_list[1]
    joints["eye-right"] = joints_list[14]
    joints["ear-right"] = joints_list[16]
    joints["eye-left"] = joints_list[15]
    joints["ear-left"] = joints_list[17]
    joints["shoulder-right"] = joints_list[2]
    joints["elbow-right"] = joints_list[3]
    joints["wirst-right"] = joints_list[4]
    joints["hip-right"] = joints_list[8]
    joints["knee-right"] = joints_list[9]
    joints["ankle-right"] = joints_list[10]
    joints["shoulder-left"] = joints_list[5]
    joints["elbow-left"] = joints_list[6]
    joints["wirst-left"] = joints_list[7]
    joints["hip-left"] = joints_list[11]
    joints["knee-left"] = joints_list[12]
    joints["ankle-left"] = joints_list[13]