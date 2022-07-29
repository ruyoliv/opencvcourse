
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while(1):
    _, frame = cap.read()
    # It converts the BGR color space of image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     
    # Threshold of blue in HSV space
    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])

    # Threshold of green in HSV space
    # (40, 40,40) ~ (70, 255,255)
    # outro (25, 20, 20) ~(100,255,255)
    lower_green = np.array([25, 20, 20])
    upper_green = np.array([100, 255, 255])
 
    # Threshold of red in HSV space
    # (165,87,111) ~ (180,255,255)
    lower_red = np.array([165,87,111])
    upper_red = np.array([180, 255, 255])

    # preparing the mask to overlay
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    #mask = cv2.inRange(hsv, lower_red, upper_red)

    # The black region in the mask has the value of 0,
    # so when multiplied with original image removes all non-blue regions
    result = cv2.bitwise_and(frame, frame, mask = mask)
 
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
     
    #cv2.waitKey(0)
    if cv2.waitKey(1) & 0xff == 27:
 
        cv2.destroyAllWindows()
        cap.release()