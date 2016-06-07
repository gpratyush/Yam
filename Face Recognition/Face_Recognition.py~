import cv2, os
import numpy as np
import math
from PIL import Image
count=0
conf_sum=0
nbr_predicted=0
x1=y1=h1=w1=0
labels_last=1
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
profileface_cascade=cv2.CascadeClassifier('haarcascade_profileface.xml')
recognizer = cv2.face.createLBPHFaceRecognizer()
path = './yalefaces'
cap = cv2.VideoCapture(0)
def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
        # Detect the face in the image
        faces = face_cascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    # return the images list and labels list
    return images, labels
def add() :
	global labels_last
	#cv2.destroyAllWindows()
	labels_last += 1	
	i=1
	while i <= 10 :
		x1=y1=h1=w1=0
		print "Press c to click Picture {}.".format(i)
		#cv2.imshow('Picture Click',img1) 		
		cv2.waitKey(10000)
		ret1,img1 = cap.read()
		gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
		faces2=face_cascade.detectMultiScale(gray1)
		for(x,y,w,h) in faces2 :
			if (w*h) > (w1*h1) :
				x1=x
				y1=y
				w1=w
				h1=h
		roi1 = gray[y1-100:y1+h1+100, x1-100:x1+w1+100]
		name = "subject" + str(labels_last) + "." + chr(i+96) +".jpg"
		cv2.imwrite(name,roi1)
		i += 1
def main() :
	global x1,y1,h1,w1,nbr_predicted,conf_sum,count
	images, labels = get_images_and_labels(path)
	cv2.destroyAllWindows()
	recognizer.train(images, np.array(labels))
	while True :
		ret,img = cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces1=face_cascade.detectMultiScale(gray)
		profilefaces=profileface_cascade.detectMultiScale(gray)
		for(x,y,w,h) in faces1 :
			if (w*h) > (w1*h1) :
				x1=x
				y1=y
				w1=w
				h1=h
		for(x,y,w,h) in profilefaces :
			if (w*h) > (w1*h1) :
				x1=x
				y1=y
				w1=w
				h1=h
		cv2.rectangle(img, (x1,y1), (x1+w1, y1+h1), (255,0,0), 2)
		cv2.imshow('Face Detect',img)
		if (faces1 is None and profilefaces is None) :
			count=0
		if (x1 > 0 and y1 > 0 and w1 > 0 and h1 > 0 and count < 10) :
			roi = gray[y1:y1+h1, x1:x1+w1]	
			predict_image = np.array(roi,'uint8')
			nbr_predict, conf=recognizer.predict(predict_image)
			if (conf < 80 ) :
				nbr_predicted += nbr_predict
				conf_sum += conf
			else :
				nbr_predicted += 0
			count += 1
		else :
			#count=0
			nbr_predicted=0
			conf_sum=0
		if count == 10 :
			nbr_predicted = math.ceil(nbr_predicted/10)
			conf_sum = conf_sum/10
		if (nbr_predicted != 0 and count == 10) :
			print "HI {} with {} confidence.".format(nbr_predicted,conf)
		elif (nbr_predicted == 0 and count == 10 and conf_sum != 0) :
			print "Not Found."
		k = cv2.waitKey(1) & 0xff
		if k==27 :
			break	
		else :
			x1=y1=h1=w1=0
main()
cap.release()
cv2.destroyAllWindows()
      
