from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trivia.db'

db = SQLAlchemy(app)

class Usuario(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    def __repr__(self):
        return '<User %s>' % self.username 
    
class Categoria(db.Model):
    
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False,unique=True)
    peguntas = db.relationship('Pregunta', backref='pregunta',lazy='dynamic')
    def __repr__(self):
        return '<Categoria %s>' % self.name

class Pregunta(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255),nullable=False,unique=True)
    categoria_id = db.Column(db.Integer,db.ForeignKey('categoria.id'))
    repuestas = db.relationship('Respuesta', backref='respuesta',lazy='dynamic')
    def __repr__(self):
        return '<Pregunta %s>' % self.texto

class Respuesta(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255),nullable=False,unique=True)
    es_correcta = db.Column(db.Boolean)
    pregunta_id = db.Column(db.Integer,db.ForeignKey('pregunta.id'))
    def __repr__(self):
        return '<Respuesta %s>' % self.texto