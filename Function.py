import cv2

def Threshold(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    return image