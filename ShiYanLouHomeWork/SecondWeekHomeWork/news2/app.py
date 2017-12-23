#!/usr/bin/env python3
import os.path
from flask import Flask,render_template
import json
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/Lab'
db = SQLAlchemy(app)

@app.route('/')
def index():
    a = File()
    t = a.title
    h = a.query.all()
    return render_template('index.html',t=t,h=h)




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



class Category(db.Model):
          id  = db.Column(db.Integer,primary_key=True)
          name = db.Column(db.String(80))
          def __repr__(self):
              return '<Category %r>' % self.name
