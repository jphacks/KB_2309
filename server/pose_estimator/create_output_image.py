
from trig import five_angle, to_joints
import cv2
import numpy as np



def create_output_image(frame, points, num):
    head = np.array(points[0])
    eye_ave = ((np.array(points[14]) + np.array(points[15])))/ 2
    neck = np.array(points[1])
    hip_ave = (np.array(points[11]) + np.array(points[8])) / 2
    knee_ave = (np.array(points[12]) + np.array(points[9])) / 2
    ankle_ave = (np.array(points[13]) + np.array(points[10])) / 2
    elbow_ave = (np.array(points[3]) + np.array(points[6])) / 2
    hand_ave = (np.array(points[4]) + np.array(points[7])) / 2
    


    # Draw the joints
    cv2.circle(frame, (int(head[0]), int(head[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(eye_ave[0]), int(eye_ave[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(neck[0]), int(neck[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(knee_ave[0]), int(knee_ave[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(hip_ave[0]), int(hip_ave[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(ankle_ave[0]), int(ankle_ave[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(elbow_ave[0]), int(elbow_ave[1])), 5, (0, 0, 0), thickness=3)
    cv2.circle(frame, (int(hand_ave[0]), int(hand_ave[1])), 5, (0, 0, 0), thickness=3)


    # Draw the lines
    cv2.line(frame, (int(head[0]), int(head[1])), (int(eye_ave[0]), int(eye_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(neck[0]), int(neck[1])), (int(eye_ave[0]), int(eye_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(neck[0]), int(neck[1])), (int(hip_ave[0]), int(hip_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(hip_ave[0]), int(hip_ave[1])), (int(knee_ave[0]), int(knee_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(knee_ave[0]), int(knee_ave[1])), (int(ankle_ave[0]), int(ankle_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(elbow_ave[0]), int(elbow_ave[1])), (int(hand_ave[0]), int(hand_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(neck[0]), int(neck[1])), (int(elbow_ave[0]), int(elbow_ave[1])), (0, 0, 0), thickness=2)


    cv2.line(frame, (int(hip_ave[0]), int(hip_ave[1])), (int(hip_ave[0]+200), int(hip_ave[1])), (0, 0, 0), thickness=2)
    cv2.line(frame, (int(knee_ave[0])-200, int(knee_ave[1])), (int(knee_ave[0]), int(knee_ave[1])), (0, 0, 0), thickness=2)


    # Calculate the angle between the lines "neck to hip" and "hip to knee"
    line1_vector = np.array([int(hip_ave[0]) - int(hip_ave[0]+100), int(hip_ave[1]) - int(hip_ave[1])])
    line2_vector = np.array([int(knee_ave[0]) - int(hip_ave[0]), int(knee_ave[1]) - int(hip_ave[1])])

    # Calculate the angle between the lines "hip to knee" and "knee to ankle"
    line3_vector = np.array([int(knee_ave[0]) - int(knee_ave[0]-100), int(knee_ave[1]) - int(knee_ave[1])])
    line4_vector = np.array([int(ankle_ave[0]) - int(knee_ave[0]), int(ankle_ave[1]) - int(knee_ave[1])])

    # Draw the protractor arcs for the first and second line segments
    draw_protractor_arc(frame, (int(hip_ave[0]), int(hip_ave[1])), line1_vector, line2_vector, 0)
    draw_protractor_arc(frame, (int(knee_ave[0]), int(knee_ave[1])), line3_vector, line4_vector, 1)



    cv2.imwrite('output_images/frame_'+str(num)+'.jpg', frame)


# Define a function to draw the protractor arc
def draw_protractor_arc(frame, center, line1_vector, line2_vector, joint_idx):

    color = (0, 0, 255)
    angle1 = np.arctan2(line1_vector[1], line1_vector[0])
    angle2 = np.arctan2(line2_vector[1], line2_vector[0])

    # Calculate the start and end angles for the arc
    if joint_idx == 0:
        start_angle = np.degrees(angle2)
        end_angle = 0
        if -5 < start_angle < 5:
            color = (0, 0, 255)
        cv2.ellipse(frame, center, (50, 50), 0, start_angle, end_angle, color, thickness=2)
        cv2.putText(frame, "Back Angle: " + str("{:.3f}".format(start_angle)), (550, 50), cv2.FONT_HERSHEY_DUPLEX, 2, color, 3)

    if joint_idx == 1:
        start_angle = 180
        end_angle = np.degrees(angle2)
        if 70 < end_angle < 100:
            color = (0, 0, 255)
        cv2.ellipse(frame, center, (50, 50), 0, start_angle, end_angle, color, thickness=2)
        cv2.putText(frame, "Knee Angle: " + str("{:.3f}".format(end_angle)), (550, 150), cv2.FONT_HERSHEY_DUPLEX, 2, color, 3)


    # Draw the protractor arc
