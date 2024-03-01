import pyfingerprint
import os

import cv2
import numpy as np

def compare_fingerprints(image1_path, image2_path):
    # Load the two images
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Compute SIFT features for both images
    sift = cv2.SIFT_create()
    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

    # Use FLANN based matcher with knn
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Apply ratio test to select good matches
    good_matches_ratio = 0.7
    good_matches_count = 0
    for m, n in matches:
        if m.distance < good_matches_ratio * n.distance:
            good_matches_count += 1
            
    # Calculate confidence score
    confidence_score = (good_matches_count / len(keypoints_1)) * 100
    
    return confidence_score

# Example usage:


# Example usage (assuming the fingerprint images are in a folder called "fingers")

