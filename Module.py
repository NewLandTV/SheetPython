import cv2
import numpy as np
import Function as F

def RemoveNoise(image):
    image = F.Threshold(image)  # Image binarization
    mask = np.zeros(image.shape, np.uint8)  # To extract only the staff area
    count, labels, stats, centroids = cv2.connectedComponentsWithStats(image)   # Labeling

    for i in range(1, count):
        x, y, w, h, area = stats[i]

        # Only the staff area
        if w > image.shape[1] >> 1:
            cv2.rectangle(mask, (x, y, w, h), (255, 0, 0), -1)

    maskedImage = cv2.bitwise_and(image, mask)

    return maskedImage