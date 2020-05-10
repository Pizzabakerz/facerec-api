#!/usr/bin/python3
from flask import Flask,request,jsonify,render_template
from face import facecheck
import base64
import os

app = Flask(__name__)

@app.route('/')
def document():
    return render_template('index.html')

@app.route('/login',methods=['post'])
def login():        
    data = request.get_json()
    name = data['username']    
    image_data = data['image']
    
    with open('/home/jacksonjegadheeson/facerec-api/captured/'+name+'.jpg', "wb") as fh:
        fh.write(base64.b64decode(image_data))
    
    rec = facecheck('/home/jacksonjegadheeson/facerec-api/captured/'+name+'.jpg')
    os.remove('/home/jacksonjegadheeson/facerec-api/captured/'+name+'.jpg')    
    return jsonify({
        'response':"works",
        "facesetup":str(rec)})

@app.route('/signup',methods=['post'])
def signup():        
    data = request.get_json()
    name = data['username']    
    image_data = data['image']
    
    with open('/home/jacksonjegadheeson/facerec-api/captured/'+name+'.jpg', "wb") as fh:
        fh.write(base64.b64decode(image_data))

    rec = facecheck('/home/jacksonjegadheeson/facerec-api/captured/'+name+'.jpg')
    
    if rec['status'] == "True":
        return jsonify({
        'response':"works",
        "facesetup":str("already_registered")})
    
    elif rec['status'] == "False":
        with open('/home/jacksonjegadheeson/facerec-api/registerdface/'+name+'.jpg', "wb") as fh:
            fh.write(base64.b64decode(image_data))
            
    os.remove('/home/jacksonjegadheeson/facerec-api/captured/'+name+'.jpg')  
    return jsonify({
        'response':"works",
        "facesetup":str("successfully_registered")})


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')