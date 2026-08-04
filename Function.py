# Creation Date: 2024.04.04. Thu, 22:16:08
# Modified Date: 2024.04.04. Thu, 22:17:20
import cv2

def Threshold(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    return image