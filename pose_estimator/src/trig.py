import numpy as np

def five_angle(points):
    
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



def to_joints(lst):
    # Ensure that all sublists have the same length
    max_len = max(len(sublist) if sublist is not None else 0 for sublist in lst)
    joints_list = [list(sublist) if sublist is not None else None for sublist in lst]
    
    # Pad sublists with None values to make them of equal length
    for sublist in joints_list:
        if sublist is not None and len(sublist) < max_len:
            sublist.extend([None] * (max_len - len(sublist)))
    
    print(joints_list)
    
    # Convert the list of lists to a NumPy array
    joints_array = np.array(joints_list)
    print(joints_array)
    
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