#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.trivia import Categoria , Pregunta, db

db.drop_all()
db.create_all()

#categorias

c_geogra = Categoria(name="Geografía")
db.session.add(c_geogra)
db.session.commit()
#preguntas categoria geografia

q_Laos = Pregunta(texto="¿Cuál es la capital de Laos?", categoria_id=c_geogra.id)
q_Armenia = Pregunta(texto="¿Cuál es la población aproximada de Armenia?",categoria_id=c_geogra.id)
q_capital_Amazonas = Pregunta(texto="¿Cuánl es la capital del estado brasilero Amazonas?", categoria_id=c_geogra.id)

# agregamos todo a la sesión y luego commmiteamos

db.session.add(q_Laos)
db.session.add(q_Armenia)
db.session.add(q_capital_Amazonas)
db.session.commit()
