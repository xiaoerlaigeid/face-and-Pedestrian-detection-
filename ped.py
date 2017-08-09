from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import mqt
def detect():
	move=0
	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
	cap=cv2.VideoCapture(0)
	while(1):
		ret, img=cap.read()
		gray=cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)
		image = imutils.resize(img, width=min(400, img.shape[1]))
		(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),padding=(8, 8), scale=1.05)
		for (x, y, w, h) in rects:
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
			rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
			pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
			for (xA, yA, xB, yB) in pick:
				cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
			if (xA/480)>0.5 :
				print("move to right")
				move=4
				
			elif (yA/640)>0.5:
				print('move to down')
				move=3
			elif (xB/480)<0.3:
				print('move to left')
				move=2
			elif (yB/640)<0.3:
				print('move to up')
				move=1
			else:
				print('do nothing')
				move=0
			mqt.pass_message(move)
			#eyes = eye_cascade.detectMultiScale(roi_gray)
			
			#for (ex,ey,ew,eh) in eyes:
			#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('img',image)
		k=cv2.waitKey(1)& 0xff
		if k==27:
			break
		elif (k==ord('w')):
			mqt.pass_message(1)
		elif (k==ord('s')):
			mqt.pass_message(3)
			
	cap.release()
	cv2.destroyAllWindows()	

detect()