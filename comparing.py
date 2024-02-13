from math import fabs
import os
import cv2


def Compare(image1_path,image2_path):
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

    print("SCORE: .................................. " + str(round(best_score,2))+" %")
    is_identical=best_score>0
    return  is_identical,best_score
    # if len(match_points) > 0:
    #     result = cv2.drawMatches(finger_print_one, kp1, image, kp2, mp, None)
    #     result = cv2.resize(result, None, fx=4, fy=4)
    #     cv2.imshow("Result", result)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

