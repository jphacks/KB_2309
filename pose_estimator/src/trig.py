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

def getTilt(pointA, pointB):
    line = np.array(pointB - pointA)
    h = np.array([1,0])
    if line[0] < 0: line = -line
    m_l = np.linalg.norm(line)
    m_h = np.linalg.norm(h)
    dot_product = np.dot(line, h)
    return np.degeres(np.arccos(dot_product / (m_l * m_h)))
    
def angleTreshold(angle, target, treshold=5.0):
    return angle < target + treshold and angle > target - treshold 

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