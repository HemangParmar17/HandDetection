# HandDetectionHand Detection
Hand segmentation using Skin color and Motion Detection
Table of Contents
About The Project
Built With
Getting Started
Installation
Usage
Results
Contact
About The Project
Human-Computer Interaction using hand gesture recognition is a great advancement in technology that makes our life easier and convenient. For any gesture recognition, Hand detection is important that is a pre-processing step. In this project, hand segmentation is done using skin color and motion detection using thresholding. Using a web camera, the hand is segmented and then we can use it in any application.

Hand segmentation using two methods: 1) Skin color detection 2) Motion detection using thresholding

Built With
Python
Opencv
Getting Started
To get started, first need to install all important libraries for image processing.

Hardware
A simple web cam or any other external camera.

Installation
List of things you need to install.

pip

pip install opencv-python 
pip install imutils
pip install numpy
Libraries
Opencv - Opencv is a library for computer vision, machine learning and image processing.

Some functionality
Apply threshold value to the image
Befor applying it, convert image into grayscale

thresh = cv.threshold(imgray, 127, 255, 0)
Find and draw contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0,255,0), 3)
Usage
Hand gesture recognition using in many areas for human-computer interaction. HCI can makes our life easier and faster. Hand gesture is the best way to interact with the machines. To control the robot, sign language recognition, etc are the example of its applications.

Results
Hand Detection using Skin color:
Combination of HSV and YCbCr model is used for hand segmentation.

Original

Hue, Saturation and Value color model
HSV

YCbCr (Luminance and Chrominance color model)
YCbCr_

Result - Combination of HSV and YCbCr color model
Final

Hand detection using motion detection using thresholding:
Otsu's method selects the threshold value automatically and assigned to the image. Then Contours are drawn around the hand region to extract the hand.

FinalHand

Contact
Your Name - Hemang Parmar - hparmar6@lakeheadu.ca.com

Project Link: https://github.com/HemangParmar/Hand-Detection

Project Presentation Link : Youtube

References
https://docs.opencv.org/4.5.2/d6/d00/tutorial_py_root.html

[https://github.com/CHEREF-Mehdi/SkinDetection]

[https://github.com/dtaneja123/Hand_Recognition/blob/master/Hand_gesture_final.py]
