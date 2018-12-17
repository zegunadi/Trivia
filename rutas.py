import sys
from random import randint
from flask import Flask, render_template, session
from models.trivia import Categoria,Pregunta,Respuesta
from vo.categoriavo import CategoriaVO
from vo.preguntavo import PreguntaVO
from vo.repuestavo import RepuestaVO
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 

app = Flask(__name__, static_folder='static')
app.secret_key = 'No te lo voy a decir'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/trivia.db'
db = SQLAlchemy(app)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World! Flaskeando!"

@app.route('/', methods=['GET'])
def inicio():
    init()
    return render_template('inicio.html')

@app.route('/comenzar', methods=['GET'])
def comenzar():   
    return render_template('comenzar.html')

@app.route('/trivia/categorias', methods=['GET'])
def trivia_categorias():
    """muestra todas las categorias""" 
    if not 'usuario' in session:
        init()
    to_return = []
    for cat in Categoria.query.all():
        vo = CategoriaVO(cat.id,cat.name,session[str(cat.id)])
        to_return.append(vo)
    return render_template('comenzar.html',categorias=to_return)

@app.route('/trivia/<int:categoria>/pregunta', methods=['GET'])
def trivia_pregunta_por_categoria(categoria):
    """muestra una pregunta asociada a una categoria"""
    
    print('Categoria seleccionada : ' + str(categoria), file=sys.stderr) 
    cantidad_preguntas = Pregunta.query.filter_by(categoria_id=categoria).count()
    print('Categoria cantidad : ' + str(cantidad_preguntas), file=sys.stderr) 
    preguntas = Pregunta.query.filter_by(categoria_id=categoria).order_by(Pregunta.id)
    for preg in preguntas :
        print('Pregunta : ' + preg.texto , file=sys.stderr) 
    
    id_pregunta_elegida =randint(preguntas[0].id,preguntas[0].id + cantidad_preguntas-1)
    print('IDELEGIDA ' + str(id_pregunta_elegida), file=sys.stderr) 
    pregunta = Pregunta.query.get(id_pregunta_elegida)
   
    vopreg = PreguntaVO(pregunta.id,pregunta.texto,pregunta.categoria_id)
    
    for resp in Respuesta.query.filter_by(pregunta_id=id_pregunta_elegida) :
        voresp = RepuestaVO(resp.id,resp.texto,resp.es_correcta,resp.pregunta_id)
        vopreg.add_repuesta(voresp)
    return render_template('pregunta.html',pregunta=vopreg)

@app.route('/trivia/<int:idpregunta>/resultado/<int:idrespuesta>', methods=['GET'])
def trivia_validar_pregunta(idpregunta,idrespuesta):
    
    respuesta = Respuesta.query.get(idrespuesta) 
    pregunta = Pregunta.query.get(idpregunta)
    
    vopreg = PreguntaVO(pregunta.id,pregunta.texto,pregunta.categoria_id)
    for resp in Respuesta.query.filter_by(pregunta_id=idpregunta):
        voresp = RepuestaVO(resp.id,resp.texto,resp.es_correcta,resp.pregunta_id)
        vopreg.add_repuesta(voresp)
    
    if respuesta.es_correcta:
        vopreg.add_resultado("Repuesta Correcta")
        session[str(pregunta.categoria_id)]=False
    else:
        vopreg.add_resultado("Repuesta Incorrecta")
    
    return render_template('resultado.html',pregunta=vopreg,fin=eselfin(),respondido=idrespuesta)  

@app.route('/trivia/fin', methods=['GET'])
def trivia_fin():
    session.pop('usuario', None)
    time = datetime.now() - session['inicio']
    prueba = datetime.now() - session['inicio2']
    print('TIEMPO2 FINAL' + str( datetime.now().microsecond), file=sys.stderr)
    print('TIEMPO2 FIN' + str(prueba), file=sys.stderr) 
    
    session.pop('inicio',None)
    for cat in Categoria.query.all():
        session.pop(str(cat.id),None)
    
    return render_template('fin.html',tiempo=time,tiempo2=prueba) 

def init():
    categ = Categoria.query.all()
    session['usuario']='trivia'
    session['inicio']= datetime.now()
    session['inicio2']= datetime.now().microsecond
    print('TIEMPO2 ' + str(datetime.now().microsecond), file=sys.stderr)
    print('segundosssssssssss ' + str(datetime.now().second), file=sys.stderr) 
    for cat in categ:  
        session[str(cat.id)]= True

def eselfin():
    salida = True
    for cat in Categoria.query.all(): 
        if session[str(cat.id)]:
            salida = False
            break
    return salida 
