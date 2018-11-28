#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.trivia import Categoria , Pregunta, db

db.drop_all()
db.create_all()

#categorias

c_geogra = Categoria(name="Geografía")
c_historia = Categoria(name="Historia")
c_deportes = Categoria(name="Deportes")
c_artes = Categoria(name="Arte y Cultura")
c_ciencia = Categoria(name="Ciencia")

db.session.add(c_geogra)
db.session.add(c_historia)
db.session.add(c_deportes)
db.session.add(c_artes)
db.session.add(c_ciencia)

db.session.commit()

#preguntas categoria geografia

p_Laos = Pregunta(texto="¿Cuál es la capital de Laos?", categoria_id=c_geogra.id)
p_Armenia = Pregunta(texto="¿Cuál es la población aproximada de Armenia?",categoria_id=c_geogra.id)
p_capital_Amazonas = Pregunta(texto="¿Cuánl es la capital del estado brasilero Amazonas?", categoria_id=c_geogra.id)

# agregamos todo a la sesión y luego commmiteamos

db.session.add(p_Laos)
db.session.add(p_Armenia)
db.session.add(p_capital_Amazonas)
db.session.commit()

