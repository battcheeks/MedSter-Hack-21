import cv2
import numpy as np
import os 
import csv
names=[]
conf=[]
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

frame_id = 0
with open('Doctors.csv', newline='') as f:
	reader = csv.reader(f)
	name_list = list(reader)
names = ['None']
for i in range(0,len(name_list)):
	names.append(name_list[i][0])


cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
	
	ret, img = cam.read()

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale( 
		gray,
		scaleFactor = 1.2,
		minNeighbors = 5,
		minSize = (int(minW), int(minH)),
	)

	for(x,y,w,h) in faces:
		frame_id=frame_id+1
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

		id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

		if (confidence < 100):
			id = names[id]
			confidence = "  {0}%".format(round(100 - confidence))
		else:
			id = "unknown"
			confidence = "  {0}%".format(round(100 - confidence))
		
		cv2.putText(img, str(id), (x+5,y-5), font, 0.5, (0,255,0), 2)
		cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
		names.append(str(id))
		conf.append(str(confidence))
	cv2.imshow('camera',img) 

	k = cv2.waitKey(10) & 0xff 
	if k == 27 or frame_id==20:
		break
cam.release()
cv2.destroyAllWindows()
for i in range(0,len(conf)):
	if conf[i]==max(conf):
		print("Welcome to the system, "+names[i])
		import os
		os.system("gnome-terminal -- python3 --debug 0 post_doctor.py")
		from time import sleep
		# sleep(5)
print("You have been logged into the System!")
