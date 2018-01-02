#!/usr/bin/env python3
import os.path
from flask import Flask,render_template
import json
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from pymongo import MongoClient
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/Lab'
db = SQLAlchemy(app)
client = MongoClient('127.0.0.1',27017)
db1 = client.shiyanlou
#collection = db1.filetag

@app.route('/')
def index():
    files = File.query.all()
    return render_template('index.html',files=files)




@app.route('/files/<file_id>')
def file(file_id):
    a = File.query.filter_by(id=file_id).first()
    if a != None:
       a = File.query.filter_by(id=file_id).first()
       num2 = int(a.category_id)
       b = Category.query.filter_by(id=num2).first()
        
       return render_template('file.html',a=a,b=b)
    else:
       return render_template('404.html'),505

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404



class File(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(80))
      content = db.Column(db.Text)
      Created_time = db.Column(db.DateTime)
      category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
      category = db.relationship('Category', backref=db.backref('Files',lazy='dynamic'))
      def __repr__(self):    
          return '<File %r>' % self.title
      
      def add_tag(self,tag_name):
          file_exist = db1.filetag.find_one({'file_id':self.id})
          if file_exist:
              tags = file_exist['tags']
              if tag_name not in tags:
                  tags.append(tag_name)
                  db1.filetag.update_one({"file_id":self.id},{'$set': {'tags':tags}})
          else:
              tags = [ tag_name ]
              db1.filetag.insert_one({'file_id': self.id, 'tags': tags})

      def remove_tag(self,tag_name):
          file_exist = db1.filetag.find_one({"file_id":self.id})
          if file_exist:
             tags = file_exist['tags']
             if tag_name in tags:
                tags.remove(tag_name)
                db1.filetag.update_one({"file_id":self.id},{'$set':{"tags":tags}})
          else:
              pass
      
      def __init__(self):
          self._tags = []


      @property
      def tags(self):
          file_exist = db1.filetag.find_one({'file_id':self.id})
          return file_exist['tags']
      
      @tags.setter
      def tags(self,id):
          file_exist = db1.filetag.find_one({"file_id":id})
          self._tags=file_exist['tags']

class Category(db.Model):
          id  = db.Column(db.Integer,primary_key=True)
          name = db.Column(db.String(80))
          def __repr__(self):
              return '<Category %r>' % self.name
