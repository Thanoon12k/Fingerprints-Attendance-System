

import cv2
from django.conf import settings
from mainapp.connections import SCAN_IMAGE
from mainapp.models import Student


temp_image_name = 'temp_000.bmp'
temp_image_path =str( settings.BASE_DIR / f'media/temp/{temp_image_name}')
temp_image_url = '/media/temp/'+temp_image_name



def scanFingerprintImage():
    SCAN_IMAGE(temp_image_path)
    return temp_image_path

from django.db.models import Q

from django.db.models import Q

def getStudentData():
        student=Student.objects.filter(name='shaahad').first()#shahad
        best_score=-1
        best_student=None
        scores= []
        for std in Student.objects.all():
            try:
                 ss = compare_fingerprints(temp_image_path, std.fingerprint_image.path)
            except:
                 return None
            if ss>best_score:
                 best_student=std
                 best_score=ss
            scores.append([std.name,ss])
        if best_score <1 or best_score > 7:
            return None
        print('stndts',student)
        print('sift1 score',scores)
        return best_student
    
def compare_fingerprints(temp_finger_path, studnts_finger_path):
        img1 = cv2.imread(temp_finger_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(studnts_finger_path, cv2.IMREAD_GRAYSCALE)

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
