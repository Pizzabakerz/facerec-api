from flask import Flask,request,jsonify,render_template
from face import facecheck
import base64
import os
from auth import auth

app = Flask(__name__)

@app.route('/')
def document():
    return render_template('index.html')

@app.route('/login',methods=['post'])
def login():        
    data = request.get_json()
    name = data['username']
    password = data['password']
    image_data = data['image']
    with open('captured/'+name+'.jpg', "wb") as fh:
        fh.write(base64.b64decode(image_data))
    rec = facecheck('registerdface/'+name+'.jpg','captured/'+name+'.jpg')
    os.remove('captured/'+name+'.jpg')
    auth_object = auth()
    authentication = auth_object.authentication(name,password,"login")
    return jsonify({
        'response':"works",
        "facesetup":str(rec),
        "auth-status":str(authentication)})

@app.route('/signup',methods=['post'])
def signup():        
    data = request.get_json()
    name = data['username']
    password = data['password']
    image_data = data['image']
    with open('registerdface/'+name+'.jpg', "wb") as fh:
        fh.write(base64.b64decode(image_data))
    rec = facecheck(known_image_path='registerdface/'+name+'.jpg',unknown_image_path='registerdface/'+name+'.jpg')
    auth_object = auth()
    authentication = auth_object.authentication(name,password,"signup")
    return jsonify({
        'response':"works",
        "facesetup":str(rec),
        "auth-status":str(authentication)})


if __name__ == "__main__":
    app.run(debug=True)