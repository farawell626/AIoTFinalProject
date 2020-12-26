from flask import Flask,request,jsonify
from keras.models import load_model
import json
from PIL import Image
import base64
import cv2
from io import BytesIO
import numpy as np

app = Flask(__name__)
model = load_model('Mnist_mlp_model.h5')

@app.route('/')
def home():
    return '1'

def base64toImage(imageStr):
    imgdata = base64.b64decode(imageStr)
    image = Image.open(BytesIO(imgdata))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    return img

def predictAction(test_feature):
    test_feature = np.array(test_feature)
    test_feature_vector = test_feature.reshape(len(test_feature), 784).astype('float32')
    test_feature_normalize = test_feature_vector / 255
    predictions = model.predict_classes(test_feature_normalize)
    return predictions

@app.route('/predict', methods = ['POST'])
def predict():
    body = request.data.decode('utf-8')
    images = json.loads(body)['images']
    test_feature = []
    for imageStr in images:
        test_feature.append(base64toImage(imageStr))
    predictions = predictAction(test_feature)
    resp = {}
    resp['predictions'] = predictions.tolist()
    return jsonify(resp)

if __name__ == "__main__":
    app.debug = True
    app.run()