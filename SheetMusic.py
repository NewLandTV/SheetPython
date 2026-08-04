import cv2
import os
import Module

RESOURCES_PATH = os.getcwd() + "/Resources/"

# Load image
image = cv2.imread(RESOURCES_PATH + "Image.png")
image = Module.RemoveNoise(image)

# Show image
cv2.imshow("Sheet Music", image)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()