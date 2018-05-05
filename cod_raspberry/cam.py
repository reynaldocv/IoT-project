import urllib2
import cv2
import numpy as np
import time
import requests
import os

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://***.**.**.***:8080/shot.jpg'

while True:
	# Use urllib to get the image from the IP camera
	imgResp = urllib2.urlopen(url)

	# Numpy to convert into a array
	imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

	# Finally decode the array to OpenCV usable format ;) 
	img = cv2.imdecode(imgNp,-1)

	# Save a photo
	cv2.imwrite('foto.png',img)
		
	os.system("sshpass -p '********' scp foto.png reynaldo@ime.usp.br:www/phd/internet_coisas/")
	
	#To give the processor some less stress
	time.sleep(1)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


