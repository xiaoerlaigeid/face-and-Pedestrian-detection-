import numpy as np
import cv2
from matplotlib import pyplot as plt
import mqt

def detect():
	move=0
	face_cascade = cv2.CascadeClassifier(r'D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
	#eye_cascade = cv2.CascadeClassifier(r'D:\OpenCV\opencv\sources\data\haarcascades\haarcascade_eye.xml')haarcascade_upperbody.xml
	cap=cv2.VideoCapture(0)
	while(1):
		ret, img=cap.read()
		gray=cv2. cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces=face_cascade.detectMultiScale(gray,1.3,5)
		for(x,y,w,h) in faces:
			mqt.pass_message(move)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray= gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			featrue=img[y:y+h, x:x+w]
			if (x/480)>0.5 :
				print("move to right")
				move=4
				
			elif (y/640)>0.5:
				print('move to down')
				move=3
			elif (x/480)<0.3:
				print('move to left')
				move=2
			elif (y/640)<0.3:
				print('move to up')
				move=1
			else:
				print('do nothing')
				move=0
			#eyes = eye_cascade.detectMultiScale(roi_gray)
			
			#for (ex,ey,ew,eh) in eyes:
			#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('img',img)
		k=cv2.waitKey(1)& 0xff
		if k==27:
			break
		elif (k==ord('w')):
			mqt.pass_message(1)
		elif (k==ord('s')):
			mqt.pass_message(3)
			
	cap.release()
	cv2.destroyAllWindows()	
	