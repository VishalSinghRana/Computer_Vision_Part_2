import cv2
import numpy as np


# the function to draw the circle
def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 10,(255, 0, 0),-1)
        

cv2.namedWindow(winname = 'Puppy')

cv2.setMouseCallback('Puppy', draw_circle)


# Opening the image.
img = cv2.imread("../DATA/dog_backpack.jpg")

while True:
    cv2.imshow('Puppy', img)
    if cv2.waitKey(1) & 0xFF==27:
        break
    
cv2.destroyAllWindows()
    