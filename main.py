import data as data
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

@app.route("/test-G41/<string:cedula>", methods=['GET'])
def testMethodoGet(cedula):
    VariablerespuestaGet={
        "Respuesta": "GET",
        "cedula":cedula
    }
    return VariablerespuestaGet


@app.route("/test2-G41", methods=['POST'])
def testMethodoPost():
    Variablerespuestapost={
        "Esta es la respuesta del post": "..."
    }
    return Variablerespuestapost

@app.route("/test3-G41", methods=['PUT'])
def testMethodoPut():
    Variablerespuestaput={
        "Esta es la respuesta del put": "..."
    }
    return Variablerespuestaput

@app.route("/test4-G41", methods=['DELETE'])
def testMethodoDelete():
    Variablerespuestadelete={
        "Esta es la respuesta del delete": "..."
    }
    return Variablerespuestadelete


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
