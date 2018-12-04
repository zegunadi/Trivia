import sys
from random import randint
from flask import Flask, render_template
from models.trivia import Categoria,Pregunta,Respuesta
from vo.categoriavo import CategoriaVO
from vo.preguntavo import PreguntaVO
from vo.repuestavo import RepuestaVO
from flask_sqlalchemy import SQLAlchemy

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

@app.route('/trivia/<int:categoria>/pregunta', methods=['GET'])
def trivia_pregunta_por_categoria(categoria):
    """muestra una pregunta asociada a una categoria"""
    
   # cantidad_preguntas = Pregunta.query.filter_by(categoria_id=categoria).count()
    preguntas = Pregunta.query.filter_by(categoria_id=categoria).all()   
    preguntas
    cantidad_preguntas = preguntas.size()
    id_pregunta_elegida =randint(1,cantidad_preguntas)
   
    print('This is error output IDELEGIDA ' + str(id_pregunta_elegida), file=sys.stderr) 
    pregunta = Pregunta.query.get(categoria*id_pregunta_elegida)
   
    vopreg = PreguntaVO(pregunta.id,pregunta.texto,pregunta.categoria_id)
    
    for resp in Respuesta.query.filter_by(pregunta_id=id_pregunta_elegida) :
        voresp = RepuestaVO(resp.id,resp.texto,resp.es_correcta,resp.pregunta_id)
        vopreg.add_repuesta(voresp)
    return render_template('pregunta.html',pregunta=vopreg)

@app.route('/trivia/{<int:idpregunta>}/resultado/{<int:idrespuesta>}', methods=['GET'])
def trivia_validar_pregunta(idpregunta,idrespuesta):
    
    respuesta = Respuesta.query.get(idrespuesta) 
    pregunta = Pregunta.query.get(idpregunta)
    
    vopreg = PreguntaVO(pregunta.id,pregunta.texto,pregunta.categoria_id)
    
    for resp in Respuesta.query.filter_by(pregunta_id=idpregunta):
        voresp = RepuestaVO(resp.id,resp.texto,resp.es_correcta,resp.pregunta_id)
        vopreg.add_repuesta(voresp)
    
    if respuesta.es_correcta:
        vopreg.add_resultado("Repuesta Correcta")
    else:
        vopreg.add_resultado("Repuesta Incorrecta")
    
    return render_template('resultado.html',pregunta=vopreg)  