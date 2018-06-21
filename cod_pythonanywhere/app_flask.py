
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
import pandas
from sklearn import tree

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












