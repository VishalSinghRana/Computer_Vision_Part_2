import cv2 

img = cv2.imread("../DATA/00-puppy.jpg")
while True:
    
    cv2.imshow('Puppy', img)
    if cv2.waitKey(1) & 0xFF == 27: 
    # if we waited atleast one milisecond and we pressed escape key.
        break 

cv2.destroyAllWindows()