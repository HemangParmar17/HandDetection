import cv2
import numpy as np

# global variables
bg = None

def run_avg(image, aWeight):
    global bg
    # initialize the background
    if bg is None:
        bg = image.copy().astype("float")
        return

    # compute weighted average, accumulate it and update the background
    cv2.accumulateWeighted(image, bg, aWeight)


cam = cv2.VideoCapture(0)

# region of interest (ROI) coordinates
top, right, bottom, left = 10, 350, 225, 590

while True:
    # Read the current frame
    successful_frame_read, frame = cam.read()
    
    frame = cv2.flip(frame, 1)
    # clone the frame
    clone = frame.copy()

    # get the ROI
    roi = frame[top:bottom, right:left]

    #converting from gbr to hsv color space
    img_HSV = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    #skin color range for hsv color space
    HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255))
    HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #converting from gbr to YCbCr color space
    img_YCrCb = cv2.cvtColor(roi, cv2.COLOR_BGR2YCrCb)

    #skin color range for hsv color space
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135))
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #merge skin detection (YCbCr and hsv)
    global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
    global_mask=cv2.medianBlur(global_mask,3)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))

    HSV_result = cv2.bitwise_not(HSV_mask)
    YCrCb_result = cv2.bitwise_not(YCrCb_mask)
    global_result=cv2.bitwise_not(global_mask)

    # draw the segmented hand
    cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

    #show results
    cv2.imshow("1_HSV.jpg",HSV_result)
    cv2.imshow("2_YCbCr.jpg",YCrCb_result)
    cv2.imshow("3_global_result.jpg",global_result)
    cv2.imshow("Original",clone)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

#Release the VideoCapture Object
cam.release()
cv2.destroyAllWindows()