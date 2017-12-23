#!/usr/bin/env python3
import os.path
from flask import Flask,render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('../files/helloshiyanlou.json','r') as file:
           new_hsyl = json.loads(file.read())
    with open('/home/shiyanlou/files/helloworld.json','r') as file:
           new_hwld = json.loads(file.read())
    return render_template('index.html',syl=new_hsyl,wld=new_hwld)




@app.route('/files/<filename>')
def file(filename):
    if os.path.exists('/home/shiyanlou/files/{}.json'.format(filename)):
          with open('/home/shiyanlou/files/{}.json'.format(filename),'r') as file:
                new_dict  = json.loads(file.read())
          return render_template('file.html',new_dict=new_dict)
    else:
          return render_template('404.html'),404

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404
