# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
import requests

app = Flask(__name__)


# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "OK, coneccion con reynaldocv.pythonanywhere'!!!!"

@app.route("/IoT")
def index2():
    output = [{'msg': 'conectado a reynaldocv.pythonanywhere.com/IoT!!!'}]
    return jsonify({'output': output})

@app.route("/Cam")
def index3():
    subscription_key = "6d3a0d747e7e4a86b3f68504c45369a0"
    assert subscription_key

    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

    vision_analyze_url = vision_base_url + "analyze"

    image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/foto.png";


    headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
    params   = {'visualFeatures': 'Categories,Description,Color'}
    data     = {'url': image_url}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()


    image_caption = analysis["description"]["captions"][0]["text"].capitalize()

    output = [{'msg': image_caption}]
    return jsonify({'output': output})
