from math import fabs
import os
import cv2
import pandas as pd
import numpy as np
dataset_csv_path = "dataset/employees.csv"

df = pd.read_csv("dataset/employees.csv")

def FindEmployeeData(fingerprint_to_compare):
    
    scores_arr = []  # Array to store employee_score scores

    for index, row in df.iterrows():
        fingerprint_path = row["fingerprint-image"]
        _,employee_score = CompareFingerPrints(fingerprint_to_compare, fingerprint_path)
        print(f"start comparing............ ( {fingerprint_to_compare} , {fingerprint_path} )  >>>>>>  SCORE: {employee_score} %")

        scores_arr.append(employee_score)
    best_score=max(scores_arr)
    max_score_index = np.argmax(scores_arr)
    employee_data = df.iloc[max_score_index].to_dict()
    employee_data['score']=best_score
    employee_data["state"]="تم تسجيل الحضور"
    employee_data["attendance_date"]="1/1/2025"
    
    if best_score>0:
            return employee_data
    else:
        return None
def CompareFingerPrints(image1_path,image2_path):
    best_score = 0
    filename = None
    image = None
    kp1, kp2, mp = None, None, None

    finger_print_one = cv2.imread(image1_path)
    finger_print_two = cv2.imread(image2_path)

   
    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(finger_print_one, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(finger_print_two, None)

    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []

    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    keypoints = 0

    if len(keypoints_1) < len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    if len(match_points) / keypoints * 100 > best_score:
        best_score = len(match_points) / keypoints * 100
        image = finger_print_two
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points

    is_identical=best_score>0
    return  is_identical,round(best_score,2)
 

