
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
import requests
import pandas
from sklearn import tree
from flask import request

app = Flask(__name__)
app.config["DEBUG"] = True
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
    try:
        subscription_key = "140044e901ce4ee8951888f862aa1ca3"
        assert subscription_key
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"

        caption=[]
        try:
            image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f1.png";


            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Categories,Description,Color'}
            data     = {'url': image_url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()

            ja=analysis["description"]["captions"][0]["text"].capitalize()
            if ("sky" in ja or "white" in ja or "person" in ja or "sign" in ja):
                caption.append("No")
            else:
                caption.append("carrinho")
        except:
            caption.append("No")

        try:

            image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f2.png";


            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Categories,Description,Color'}
            data     = {'url': image_url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()


            ja=analysis["description"]["captions"][0]["text"]
            if ("sky" in ja or "white" in ja or "person" in ja or "sign" in ja):
                caption.append("No")
            else:
                caption.append("carrinho")
        except:
            caption.append("No")

        try:


            image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f3.png";


            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Categories,Description,Color'}
            data     = {'url': image_url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()


            ja=analysis["description"]["captions"][0]["text"]
            if ("sky" in ja or "white" in ja or "person" in ja or "sign" in ja):
                caption.append("No")
            else:
                caption.append("carrinho")
        except:
            caption.append("No")

        try:

            image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f4.png";


            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Categories,Description,Color'}
            data     = {'url': image_url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()


            ja=analysis["description"]["captions"][0]["text"]
            if ("sky" in ja or "white" in ja or "person" in ja or "sign" in ja):
                caption.append("No")
            else:
                caption.append("carrinho")
        except:
            caption.append("No")

        output=[]
        carros=4
        for i in range(len(caption)):
            if "carrinho" in caption[i]:
                carros-=1
            output.append({'msg': caption[i]})
        vagas=str(carros)+" vaga(s)";
        output.append({'msg': vagas})

        return jsonify({'output': output})
    except:
        output = [{'msg': 'imagen imposible de reconocer'}]
        return jsonify({'output': output})



@app.route("/IoT1")
def IoT1():
    try:
        subscription_key = "140044e901ce4ee8951888f862aa1ca3"
        assert subscription_key
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"

        caption=[]
        try:
            image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/foto.png";


            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Categories,Description,Color'}
            data     = {'url': image_url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()

            caption=analysis["description"]["captions"][0]["text"].capitalize()
            output=[{'msg': caption}]
            return jsonify({'output': output})
        except:
            output = [{'msg': 'imagen imposible de reconocer'}]
            return jsonify({'output': output})

    except:
        output = [{'msg': 'imagen imposible de reconocer'}]
        return jsonify({'output': output})



@app.route("/IoT2")
def index30():
    try:
        subscription_key = "140044e901ce4ee8951888f862aa1ca3"
        assert subscription_key
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"

        caption=[]

        image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f1.png";


        headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
        params   = {'visualFeatures': 'Categories,Description,Color'}
        data     = {'url': image_url}
        response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        analysis = response.json()

        try:
            caption.append(analysis["description"]["captions"][0]["text"].capitalize())
        except:
            caption.append("No")

        image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f2.png";


        headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
        params   = {'visualFeatures': 'Categories,Description,Color'}
        data     = {'url': image_url}
        response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        analysis = response.json()


        try:
            caption.append(analysis["description"]["captions"][0]["text"].capitalize())
        except:
            caption.append("No")

        image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f3.png";


        headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
        params   = {'visualFeatures': 'Categories,Description,Color'}
        data     = {'url': image_url}
        response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        analysis = response.json()


        try:
            caption.append(analysis["description"]["captions"][0]["text"].capitalize())
        except:
            caption.append("No")

        image_url="https://www.ime.usp.br/~reynaldo/phd/internet_coisas/f4.png";


        headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
        params   = {'visualFeatures': 'Categories,Description,Color'}
        data     = {'url': image_url}
        response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        analysis = response.json()


        try:
            caption.append(analysis["description"]["captions"][0]["text"].capitalize())
        except:
            caption.append("No")

        output=[]
        carros=4
        for i in range(len(caption)):
            if "carrinho" in caption[i]:
                carros-=1
            output.append({'msg': caption[i]})
        vagas=str(carros)+" vaga(s)";
        output.append({'msg': vagas})

        return jsonify({'output': output})
    except:
        output = [{'msg': 'imagen imposible de reconocer'}]
        return jsonify({'output': output})



@app.route("/Vagas")
def index3():

    #cargando el dataset

    names = ['dia', 'hora', 'minutos',"carros"]
    dataset = pandas.read_csv("/home/reynaldocv/mysite/dataset.txt", names=names)
    array = dataset.values
    X = array[:,0:3]
    Y = array[:,3]
    clf=tree.DecisionTreeRegressor()
    clf=clf.fit(X,Y)
    rpta=clf.predict([[6,11,24]])
    try:



        output = [{'msg': str(rpta)}]
        return jsonify({'output': output})
    except:
        output = [{'msg': 'error con el archivo'}]
        return jsonify({'output': output})




@app.route('/futuro/<dia>/<hora>/<minuto>/')
def futuro(dia,hora,minuto):
    #cargando el dataset

    names = ['fecha','dia', 'hora', 'minutos',"carros"]
    dataset = pandas.read_csv("/home/reynaldocv/mysite/dataset.txt", names=names)
    dataset = pandas.DataFrame(dataset,columns=["dia",'hora','minutos', "carros"])
    array = dataset.values
    X = array[:,0:3]
    Y = array[:,3]
    clf=tree.DecisionTreeRegressor()
    clf=clf.fit(X,Y)
    rpta=clf.predict([[dia,hora,minuto]])
    rpta2=" Vagas cheias: "+str(rpta)+" de 4"
    try:
        output = [{'msg': str(rpta2)}]
        return jsonify({'output': output})
    except:
        output = [{'msg': 'error con el archivo'}]
        return jsonify({'output': output})


    output = [{'msg': str(dia)},{'msg': str(hora)},{'msg': str(minuto)}]
    return jsonify({'output': output})

@app.route('/file')
def file():
    file = open("/home/reynaldocv/mysite/testfile.txt","w")

    file.write("Hello World")
    file.write("This is our new text file")
    file.write("and this is another line.")
    file.write("Why? Because we can.")

    file.close()
    output = [{'msg': 'se creo un archivo'}]
    return jsonify({'output': output})









@app.route('/success/<dia>/<hora>/')
def success(dia,hora):
    output = [{'msg': str(dia)},{'msg': str(hora)}]
    return jsonify({'output': output})


@app.route('/add__/<text>/')
def add(text):
    try:
        fh = open("/home/reynaldocv/mysite/testfile.txt","a")
        fh.write("\n"+text)
        fh.close
        output = [{'msg': 'ok'}]
        return jsonify({'output': output})
    except:
        output = [{'msg': 'no'}]
        return jsonify({'output': output})




@app.route('/add2')
def add2():
    try:
        task=[]
        fh = open("/home/reynaldocv/mysite/testfile.txt","r")
        for line in fh:
            task.append({'msg':line})
        return jsonify({'output': task})
    except:
        output = [{'msg': 'no'}]
        return jsonify({'output': output})

@app.route('/add/<text1>')
def add00(text1):
    try:
        fh = open("/home/reynaldocv/mysite/dataset.txt","a")
        fh.write(text1+"\n")
        fh.close
        output = [{'msg': 'ok'}]
        return jsonify({'output': output})
    except:
        output = [{'msg': 'no'}]
        return jsonify({'output': output})

@app.route('/dataset')
def dataset():
    try:
        task=[]
        fh = open("/home/reynaldocv/mysite/dataset.txt","r")
        for line in fh:
            linesplit=line.split(",");
            task.append(({'fecha':linesplit[0]},{'carros':linesplit[4].replace("\n","")}))
        return jsonify({'output': task})
    except:
        output = [{'msg': 'no'}]
        return jsonify({'output': output})

@app.route('/dataset-file')
def datasetfile():
    try:
        task=[]
        fh = open("/home/reynaldocv/mysite/dataset.txt","r")
        for line in fh:
            task.append(({'msg':line.replace("\n","")}))
        return jsonify({'output': task})
    except:
        output = [{'msg': 'no'}]
        return jsonify({'output': output})

@app.route('/reset')
def reset():
    try:
        fh = open("/home/reynaldocv/mysite/dataset.txt","w")
        fh.close()
        output = [{'msg': 'file reseteado'}]
        return jsonify({'output': output})
    except:
        output = [{'msg': 'no'}]
        return jsonify({'output': output})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)












