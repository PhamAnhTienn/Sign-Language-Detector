import sys, os
import shutil
from src.pipeline.training_pipeline import TrainPipeline
from src.exception import SignException
from src.utils.utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 


@app.route("/predict", methods=['POST','GET'])
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clientApp.filename)

        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 640 --conf 0.5 --source ../data/inputImage.jpg")

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        shutil.rmtree('yolov5/runs', ignore_errors=True)

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


@app.route("/live", methods=['GET'])
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 640 --conf 0.5 --source 0")
        shutil.rmtree('yolov5/runs', ignore_errors=True)
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    

if __name__ == "__main__":
    clientApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)