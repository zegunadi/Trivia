from flask import Flask, render_template
from models.trivia import Categoria,Pregunta
from vo.categoriavo import CategoriaVO

from flask_sqlalchemy import SQLAlchemy
from random import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/trivia.db'

db = SQLAlchemy(app)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World! Flaskeando!"

@app.route('/', methods=['GET'])
def inicio():
    return render_template('inicio.html')

@app.route('/comenzar', methods=['GET'])
def comenzar():
    return render_template('comenzar.html')

@app.route('/trivia/categorias', methods=['GET'])
def trivia_categorias():
    """muestra todas las categorias"""
    to_return = []
    for cat in Categoria.query.all():
        vo = CategoriaVO(cat.id,cat.name)
        to_return.append(vo)
    return render_template('comenzar.html',categorias=to_return)

@app.route('/trivia/<int:categoria_id>/pregunta', methods=['GET'])
def trivia_pregunta_por_categoria(categoria_id):
    """muestra una pregunta asociada a una categoria"""
    
    cantidad_preguntas = Pregunta.query.filter_by(categoria_id==categoria_id).count()
    id_pregunta_elegida = random.randint(1,cantidad_preguntas)
    to_return = []
    for resp in Pregunta.query.filter_by(pregunta_id==id_pregunta_elegida) :
        vo = CategoriaVO(cat.id,cat.name)
        to_return.append(vo)
    return render_template('comenzar.html',categorias=to_return)
