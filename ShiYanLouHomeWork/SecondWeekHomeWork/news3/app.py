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
collection = db1.filetag

@app.route('/')
def index():
    a = File()
    t = a.title
    h = a.query.all()
    tags = a.tags
    return render_template('index.html',t=t,h=h,tags=tags)




@app.route('/files/<file_id>')
def file(file_id):
    a = File.query.filter_by(id=file_id).first()
    if a != None:
       a = File.query.filter_by(id=file_id).first()
       num2 = int(a.category_id)
       b = Category.query.filter_by(id=num2).first()
       tags = File().tags
       return render_template('file.html',a=a,b=b,tags=tags)
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
          file_exist = collection.distinct({"file_id":self.id},'file_tag')
          if file_exist.count(tag_name) == 0:
             file_exist.append(tag_name)
             collection.update({"file_id":self.id},{"file_id":self.id,"file_tag":file_exist})
          else:
              pass

      def remove_tag(self,tag_name):
          file_exist = collection.distinct({"file_id":self.id},'file_tag')
          if file_exist.count(tag_name) == 1:
             file_exist.remove(tag_name)
             collection.update({"file_id":self.id},{"file_id":self.id,"file_tag":file_exist})
          else:
              pass

      @property
      def tags(self):
          file_exist = collection.distinct({"file_id":self.id},'file_tag')
          return file_exist        

class Category(db.Model):
          id  = db.Column(db.Integer,primary_key=True)
          name = db.Column(db.String(80))
          def __repr__(self):
              return '<Category %r>' % self.name
