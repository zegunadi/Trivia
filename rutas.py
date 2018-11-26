from flask import Flask, render_template
from models.trivia import Categoria


app = Flask(__name__)

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
    # Inicializacion de sesion
    """muestra todas las categorias"""
    to_return = ""
    Categoria.query.all()
    #for cate in Categoria.query.all():
    to_return= "MIO"
# print(str(cat.name))
# to_return += "<a href=\"/trivia/"+ str(cat.id) +"/pregunta\">" + cat.name + "</a><br>"
#    print(to_return)
# hacer una template seria optimo!!
    return render_template('comenzar.html',cat=to_return)