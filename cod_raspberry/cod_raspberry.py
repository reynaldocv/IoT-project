#sudo apt-get install python-opencv
#140044e901ce4ee8951888f862aa1ca3
#13c474333e6f48afb1f4b740271f34f5
import cv2
import time
import sys
import os
import requests
import json
import requests
import datetime
from PIL import Image 
from flask import jsonify

#variables de programacion
segundos=float("60")
partes=int(4)

#cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # dtry to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    try:
        #tirando la foto
        print("tomando foto...")
        rval, frame = vc.read()
        cv2.imwrite('foto.png', frame)

        #partiendo la foto y copiando as partes pro internet
        print("partiendo fotos")
        im=Image.open('foto.png')
        (w,h)=im.size
        w_=w/partes
        for i in range(partes):
            im_=im.crop((i*w_,h-300,(i+1)*w_,h))
            m_='foto__'+str(i+1)+'.png'
            im_.save(m_,"png")
            os.system("sshpass -p 'Rey@1123' scp "+m_+" reynaldo@ime.usp.br:www/phd/internet_coisas/")
        os.system("sshpass -p 'Rey@1123' scp foto.png reynaldo@ime.usp.br:www/phd/internet_coisas/")
        
        #analizando las fotos com a api de computer visual 
        print("analizando fotos")
        subscription_key = "140044e901ce4ee8951888f862aa1ca3"
        assert subscription_key
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"    
        
        caption=[]    
        for i in range(partes):
            m_='foto__'+str(i+1)+'.png'
            image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/"+m_;
            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Categories,Description,Color'}
            data     = {'url': image_url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()
            #print(analysis["description"]["captions"][0]["text"].capitalize())
            image_caption = analysis["description"]["captions"][0]["text"].capitalize()
            caption.append(image_caption)
        
        #creando el json
        print("Creando el json")
					    
	      output = []
	      vagas = partes
	      for i in range(len(caption)):
	          output.append({'msg': caption[i]})
	          if "car" in caption[i]:
	              vagas-=1
	      output.append({'msg': 'Tem '+str(vagas)+' vagas...'})        
	      json_file={'output': output}
	      with open('IoT.json', 'w') as outfile:  
	          json.dump(json_file, outfile)
	      os.system("sshpass -p 'Rey@1123' scp IoT.json reynaldo@ime.usp.br:www/phd/internet_coisas/")    
	    
				#cargando dados no reynaldocv.pythonanyhwere.com	
				print("cargando dados para a database")
				date = datetime.datetime.now()
				aux=str(date)+","+str(date.weekday())+","+str(date.hour)+","+str(date.minute)+","+str(vagas)
				url="http://reynaldocv.pythonanywhere.com/add/"+aux
				response = requests.get(url)		
    except:
        print("error")
    time.sleep(segundos)
    key = cv2.waitKey(30)    
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()

