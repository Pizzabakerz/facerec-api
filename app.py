from flask import Flask,request,jsonify
from face import facecheck
import base64
import os

app = Flask(__name__)

@app.route('/login',methods=['post'])
def login():        
    data = request.get_json()
    name = data['username']
    password = data['password']
    image_data = data['image']
    with open('registerdface/'+name+'.jpg', "wb") as fh:
        fh.write(base64.b64decode(image_data))
    rec = facecheck('registerdface/'+name+'.jpg','registerdface/'+name+'.jpg')
    return jsonify({'response':"works","facesetup":str(rec)})

@app.route('/signup',methods=['post'])
def signup():        
    data = request.get_json()
    name = data['username']
    password = data['password']
    image_data = data['image']
    with open('registerdface/'+name+'.jpg', "wb") as fh:
        fh.write(base64.b64decode(image_data))
    return jsonify({'response':"works"})

if __name__ == "__main__":
    app.run(debug=True)