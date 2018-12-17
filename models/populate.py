#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.trivia import Categoria,Pregunta,Respuesta,db

db.drop_all()
db.create_all()

#categorias

c_geogra = Categoria(name="Geografía")
c_historia = Categoria(name="Historia")
c_deporte = Categoria(name="Deporte")
c_arte = Categoria(name="Arte y Literatura")
c_ciencia = Categoria(name="Ciencia")
c_entre = Categoria(name="Entretenimiento")

db.session.add(c_geogra)
db.session.add(c_historia)
db.session.add(c_deporte)
db.session.add(c_arte)
db.session.add(c_ciencia)
db.session.add(c_entre)

db.session.commit()

#preguntas categoria geografia

p_c_geogra_1 = Pregunta(texto="¿Cuánto se extiende la costa uruguaya de este a oeste?", categoria_id=c_geogra.id)
p_c_geogra_2 = Pregunta(texto="¿A la altura de qué departamento queda la Isla de Lobos?", categoria_id=c_geogra.id)
p_c_geogra_3 = Pregunta(texto="¿Entre qué dos balnearios se ubica Las Toscas?", categoria_id=c_geogra.id)
p_c_geogra_4 = Pregunta(texto="¿Cuál es el cerro más alto del Uruguay?", categoria_id=c_geogra.id)
p_c_geogra_5 = Pregunta(texto="¿Cuál de los siguientes departamentos no se situan sobre el margen del Río Negro?", categoria_id=c_geogra.id)


#preguntas categoria historia

p_c_historia_1 = Pregunta(texto="¿En qué fecha fue fundado Montevideo?", categoria_id=c_historia.id)
p_c_historia_2 = Pregunta(texto="¿La primera constitución nacional fue adoptada el?", categoria_id=c_historia.id)
p_c_historia_3 = Pregunta(texto="¿Quién fue el primer presidente en el Uruguay electo bajo la constitución de 1830?", categoria_id=c_historia.id)
p_c_historia_4 = Pregunta(texto="¿En qué batalla surgen las divisas blanca y colorada?", categoria_id=c_historia.id)
p_c_historia_5 = Pregunta(texto="¿Cuál de los siguientes presidentes no fue electo en más de una oportunidad?", categoria_id=c_historia.id)


#preguntas categoria deportes

p_c_deporte_1 = Pregunta(texto="¿En qué país se hizo el mundial de fútbol del 2010?", categoria_id=c_deporte.id)
p_c_deporte_2 = Pregunta(texto="¿Cuántos jugadores componen un equipo de rugby?", categoria_id=c_deporte.id)
p_c_deporte_3 = Pregunta(texto="¿Con qué apodo es conocido Enzo Francescoli?", categoria_id=c_deporte.id)
p_c_deporte_4 = Pregunta(texto="¿Con cuál de los siguientes deportes Uruguay no obtuvo una medalla olimpica?", categoria_id=c_deporte.id)
p_c_deporte_5 = Pregunta(texto="¿En qué deporte se destacaron César Bernal y Néstor Iroldi?", categoria_id=c_deporte.id)


#preguntas categoria arte y literatura

p_c_arte_1 = Pregunta(texto="Cuál de los siguientes escritores uruguayos ganó el premio Cervantes?", categoria_id=c_arte.id)
p_c_arte_2 = Pregunta(texto="¿Cuál de los siguientes pintores es conocido como el pintor de la patria?", categoria_id=c_arte.id)
p_c_arte_3 = Pregunta(texto="¿De quién es la obra América invertida?", categoria_id=c_arte.id)
p_c_arte_4 = Pregunta(texto="¿Quién creó al sapo Ruperto?", categoria_id=c_arte.id)
p_c_arte_5 = Pregunta(texto="¿Quién pintó El juramento de los Treinta y Tres Orientales?", categoria_id=c_arte.id)


#preguntas categoria ciencia

p_c_ciencia_1 = Pregunta(texto="¿Qué son las várices?", categoria_id=c_ciencia.id)
p_c_ciencia_2 = Pregunta(texto="¿Cuáles son los huesos del oído?", categoria_id=c_ciencia.id)
p_c_ciencia_3 = Pregunta(texto="¿Cuál es el símbolo químico del oro?", categoria_id=c_ciencia.id)
p_c_ciencia_4 = Pregunta(texto="¿Cuál es la función de la insulina en la sangre?", categoria_id=c_ciencia.id)
p_c_ciencia_5 = Pregunta(texto="¿Qué registra un sismógrafo?", categoria_id=c_ciencia.id)

#preguntas categoria entretenimiento

p_c_entre_1 = Pregunta(texto="¿Qué película de Disney trata sobre un perro que cree tener superpoderes?", categoria_id=c_entre.id)
p_c_entre_2 = Pregunta(texto="¿A qué película de Disney pertenece la canción Hakuna Matata?", categoria_id=c_entre.id)
p_c_entre_3 = Pregunta(texto="¿Cuál es el motivo por el que Peter Parker se convirtió en Spider-Man?", categoria_id=c_entre.id)
p_c_entre_4 = Pregunta(texto="En la película La era del hielo, ¿qué personaje es Manny?", categoria_id=c_entre.id)
p_c_entre_5 = Pregunta(texto="¿Cómo se llama la canción escrita por Shakira para el Mundial del 2010?", categoria_id=c_entre.id)


db.session.add(p_c_geogra_1)
db.session.add(p_c_geogra_2)
db.session.add(p_c_geogra_3)
db.session.add(p_c_geogra_4)
db.session.add(p_c_geogra_5)

db.session.add(p_c_historia_1)
db.session.add(p_c_historia_2)
db.session.add(p_c_historia_3)
db.session.add(p_c_historia_4)
db.session.add(p_c_historia_5)

db.session.add(p_c_deporte_1)
db.session.add(p_c_deporte_2)
db.session.add(p_c_deporte_3)
db.session.add(p_c_deporte_4)
db.session.add(p_c_deporte_5)

db.session.add(p_c_arte_1)
db.session.add(p_c_arte_2)
db.session.add(p_c_arte_3)
db.session.add(p_c_arte_4)
db.session.add(p_c_arte_5)

db.session.add(p_c_ciencia_1)
db.session.add(p_c_ciencia_2)
db.session.add(p_c_ciencia_3)
db.session.add(p_c_ciencia_4)
db.session.add(p_c_ciencia_5)

db.session.add(p_c_entre_1)
db.session.add(p_c_entre_2)
db.session.add(p_c_entre_3)
db.session.add(p_c_entre_4)
db.session.add(p_c_entre_5)



db.session.commit()

#repuestas categotia geografia

rp_c_geogra_1_1 = Respuesta(texto="500 kilometros",es_correcta=True,pregunta_id=p_c_geogra_1.id)
rp_c_geogra_1_2 = Respuesta(texto="550 kilometros",es_correcta=False,pregunta_id=p_c_geogra_1.id)
rp_c_geogra_1_3 = Respuesta(texto="450 kilometros",es_correcta=False,pregunta_id=p_c_geogra_1.id)
rp_c_geogra_1_4 = Respuesta(texto="400 kilometros",es_correcta=False,pregunta_id=p_c_geogra_1.id)

rp_c_geogra_2_1 = Respuesta(texto="Canelones",es_correcta=False,pregunta_id=p_c_geogra_2.id)
rp_c_geogra_2_2 = Respuesta(texto="Rocha",es_correcta=False,pregunta_id=p_c_geogra_2.id)
rp_c_geogra_2_3 = Respuesta(texto="Maldonado",es_correcta=True,pregunta_id=p_c_geogra_2.id)
rp_c_geogra_2_4 = Respuesta(texto="Colonia",es_correcta=False,pregunta_id=p_c_geogra_2.id)

rp_c_geogra_3_1 = Respuesta(texto="Villa Argentina y El Fortín",es_correcta=False,pregunta_id=p_c_geogra_3.id)
rp_c_geogra_3_2 = Respuesta(texto="Atlántida y Parque del Plata",es_correcta=True,pregunta_id=p_c_geogra_3.id)
rp_c_geogra_3_3 = Respuesta(texto="Las Vegas y Parque del Plata",es_correcta=False,pregunta_id=p_c_geogra_3.id)
rp_c_geogra_3_4 = Respuesta(texto="Medanos de Solymar y El Pinar",es_correcta=False,pregunta_id=p_c_geogra_3.id)

rp_c_geogra_4_1 = Respuesta(texto="Cerro Pan de Azúcar",es_correcta=False,pregunta_id=p_c_geogra_4.id)
rp_c_geogra_4_2 = Respuesta(texto="Cerro San Antonio",es_correcta=False,pregunta_id=p_c_geogra_4.id)
rp_c_geogra_4_3 = Respuesta(texto="Cerro de las Ánimas",es_correcta=False,pregunta_id=p_c_geogra_4.id)
rp_c_geogra_4_4 = Respuesta(texto="Cerro Catedral",es_correcta=True,pregunta_id=p_c_geogra_4.id)

rp_c_geogra_5_1 = Respuesta(texto="Soriano",es_correcta=False,pregunta_id=p_c_geogra_5.id)
rp_c_geogra_5_2 = Respuesta(texto="Treinta y Tres",es_correcta=True,pregunta_id=p_c_geogra_5.id)
rp_c_geogra_5_3 = Respuesta(texto="Rivera",es_correcta=False,pregunta_id=p_c_geogra_5.id)
rp_c_geogra_5_4 = Respuesta(texto="Florida",es_correcta=False,pregunta_id=p_c_geogra_5.id)


#repuestas categotia historia

rp_c_historia_1_1 = Respuesta(texto="24 de diciembre de 1724",es_correcta=True,pregunta_id=p_c_historia_1.id)
rp_c_historia_1_2 = Respuesta(texto="24 de octubre de 1720",es_correcta=False,pregunta_id=p_c_historia_1.id)
rp_c_historia_1_3 = Respuesta(texto="20 de diciembre de 1725",es_correcta=False,pregunta_id=p_c_historia_1.id)
rp_c_historia_1_4 = Respuesta(texto="20 de octubre de 1726",es_correcta=False,pregunta_id=p_c_historia_1.id)

rp_c_historia_2_1 = Respuesta(texto="19 de Abril de 1830",es_correcta=False,pregunta_id=p_c_historia_2.id)
rp_c_historia_2_2 = Respuesta(texto="25 de Agosto de 1830",es_correcta=False,pregunta_id=p_c_historia_2.id)
rp_c_historia_2_3 = Respuesta(texto="18 de Julio de 1830",es_correcta=True,pregunta_id=p_c_historia_2.id)
rp_c_historia_2_4 = Respuesta(texto="18 de Junio de 1830",es_correcta=False,pregunta_id=p_c_historia_2.id)

rp_c_historia_3_1 = Respuesta(texto="Manuel Oribe",es_correcta=False,pregunta_id=p_c_historia_3.id)
rp_c_historia_3_2 = Respuesta(texto="Fructoso Rivera",es_correcta=True,pregunta_id=p_c_historia_3.id)
rp_c_historia_3_3 = Respuesta(texto="Antonio Lavalleja",es_correcta=False,pregunta_id=p_c_historia_3.id)
rp_c_historia_3_4 = Respuesta(texto="Venancio Flores",es_correcta=False,pregunta_id=p_c_historia_3.id)

rp_c_historia_4_1 = Respuesta(texto="Batalla de las Piedras",es_correcta=False,pregunta_id=p_c_historia_4.id)
rp_c_historia_4_2 = Respuesta(texto="Batalla de Masoller",es_correcta=False,pregunta_id=p_c_historia_4.id)
rp_c_historia_4_3 = Respuesta(texto="Batalla del Rincón",es_correcta=False,pregunta_id=p_c_historia_4.id)
rp_c_historia_4_4 = Respuesta(texto="Batalla de Carpintería",es_correcta=True,pregunta_id=p_c_historia_4.id)

rp_c_historia_5_1 = Respuesta(texto="José Batlle y Ordóñez",es_correcta=False,pregunta_id=p_c_historia_5.id)
rp_c_historia_5_2 = Respuesta(texto="Julio Herrera y Obes",es_correcta=True,pregunta_id=p_c_historia_5.id)
rp_c_historia_5_3 = Respuesta(texto="Julio María Sanguinetti",es_correcta=False,pregunta_id=p_c_historia_5.id)
rp_c_historia_5_4 = Respuesta(texto="Fructuoso Rivera",es_correcta=False,pregunta_id=p_c_historia_5.id)

#repuestas categotia deporte

rp_c_deporte_1_1 = Respuesta(texto="Sudáfrica",es_correcta=True,pregunta_id=p_c_deporte_1.id)
rp_c_deporte_1_2 = Respuesta(texto="Francia",es_correcta=False,pregunta_id=p_c_deporte_1.id)
rp_c_deporte_1_3 = Respuesta(texto="Brasil",es_correcta=False,pregunta_id=p_c_deporte_1.id)
rp_c_deporte_1_4 = Respuesta(texto="Alemania",es_correcta=False,pregunta_id=p_c_deporte_1.id)

rp_c_deporte_2_1 = Respuesta(texto="12",es_correcta=False,pregunta_id=p_c_deporte_2.id)
rp_c_deporte_2_2 = Respuesta(texto="11",es_correcta=False,pregunta_id=p_c_deporte_2.id)
rp_c_deporte_2_3 = Respuesta(texto="15",es_correcta=True,pregunta_id=p_c_deporte_2.id)
rp_c_deporte_2_4 = Respuesta(texto="17",es_correcta=False,pregunta_id=p_c_deporte_2.id)

rp_c_deporte_3_1 = Respuesta(texto="El rey",es_correcta=False,pregunta_id=p_c_deporte_3.id)
rp_c_deporte_3_2 = Respuesta(texto="El príncipe",es_correcta=True,pregunta_id=p_c_deporte_3.id)
rp_c_deporte_3_3 = Respuesta(texto="La saeta",es_correcta=False,pregunta_id=p_c_deporte_3.id)
rp_c_deporte_3_4 = Respuesta(texto="La brujita",es_correcta=False,pregunta_id=p_c_deporte_3.id)

rp_c_deporte_4_1 = Respuesta(texto="Fútbol",es_correcta=False,pregunta_id=p_c_deporte_4.id)
rp_c_deporte_4_2 = Respuesta(texto="Remo",es_correcta=False,pregunta_id=p_c_deporte_4.id)
rp_c_deporte_4_3 = Respuesta(texto="Boxeo",es_correcta=False,pregunta_id=p_c_deporte_4.id)
rp_c_deporte_4_4 = Respuesta(texto="Waterpolo",es_correcta=True,pregunta_id=p_c_deporte_4.id)

rp_c_deporte_5_1 = Respuesta(texto="Remo",es_correcta=False,pregunta_id=p_c_deporte_5.id)
rp_c_deporte_5_2 = Respuesta(texto="Paleta",es_correcta=True,pregunta_id=p_c_deporte_5.id)
rp_c_deporte_5_3 = Respuesta(texto="Tenis",es_correcta=False,pregunta_id=p_c_deporte_5.id)
rp_c_deporte_5_4 = Respuesta(texto="Boxeo",es_correcta=False,pregunta_id=p_c_deporte_5.id)

#repuestas categotia arte

rp_c_arte_1_1 = Respuesta(texto="Ida Vitale",es_correcta=True,pregunta_id=p_c_arte_1.id)
rp_c_arte_1_2 = Respuesta(texto="Idea Vilariño",es_correcta=False,pregunta_id=p_c_arte_1.id)
rp_c_arte_1_3 = Respuesta(texto="Juana de Ibarbourou",es_correcta=False,pregunta_id=p_c_arte_1.id)
rp_c_arte_1_4 = Respuesta(texto="Delmira Agustini",es_correcta=False,pregunta_id=p_c_arte_1.id)

rp_c_arte_2_1 = Respuesta(texto="Pedro Blanes Viale",es_correcta=False,pregunta_id=p_c_arte_2.id)
rp_c_arte_2_2 = Respuesta(texto="Pedro Figari",es_correcta=False,pregunta_id=p_c_arte_2.id)
rp_c_arte_2_3 = Respuesta(texto="Juan Manuel Blanes",es_correcta=True,pregunta_id=p_c_arte_2.id)
rp_c_arte_2_4 = Respuesta(texto="Joaquín Torres García",es_correcta=False,pregunta_id=p_c_arte_2.id)

rp_c_arte_3_1 = Respuesta(texto="Juan Manuel Blanes",es_correcta=False,pregunta_id=p_c_arte_3.id)
rp_c_arte_3_2 = Respuesta(texto="Joaquín Torres García",es_correcta=True,pregunta_id=p_c_arte_3.id)
rp_c_arte_3_3 = Respuesta(texto="Pedro Figari",es_correcta=False,pregunta_id=p_c_arte_3.id)
rp_c_arte_3_4 = Respuesta(texto="Rafael Barradas",es_correcta=False,pregunta_id=p_c_arte_3.id)

rp_c_arte_4_1 = Respuesta(texto="Gerardo Caetano",es_correcta=False,pregunta_id=p_c_arte_4.id)
rp_c_arte_4_2 = Respuesta(texto="Helen Velando",es_correcta=False,pregunta_id=p_c_arte_4.id)
rp_c_arte_4_3 = Respuesta(texto="Susana Olaondo",es_correcta=False,pregunta_id=p_c_arte_4.id)
rp_c_arte_4_4 = Respuesta(texto="Roy Berocay",es_correcta=True,pregunta_id=p_c_arte_4.id)

rp_c_arte_5_1 = Respuesta(texto="Pedro Figari",es_correcta=False,pregunta_id=p_c_arte_5.id)
rp_c_arte_5_2 = Respuesta(texto="Juan Manuel Blanes",es_correcta=True,pregunta_id=p_c_arte_5.id)
rp_c_arte_5_3 = Respuesta(texto="Rafael Barradas",es_correcta=False,pregunta_id=p_c_arte_5.id)
rp_c_arte_5_4 = Respuesta(texto="Joaquín Torres García",es_correcta=False,pregunta_id=p_c_arte_5.id)

#repuestas categotia ciencia

rp_c_ciencia_1_1 = Respuesta(texto="Dilatación de las venas",es_correcta=True,pregunta_id=p_c_ciencia_1.id)
rp_c_ciencia_1_2 = Respuesta(texto="Dilatación de los nervios",es_correcta=False,pregunta_id=p_c_ciencia_1.id)
rp_c_ciencia_1_3 = Respuesta(texto="Dilatación de los músculos",es_correcta=False,pregunta_id=p_c_ciencia_1.id)
rp_c_ciencia_1_4 = Respuesta(texto="Dilatación de los tendones",es_correcta=False,pregunta_id=p_c_ciencia_1.id)

rp_c_ciencia_2_1 = Respuesta(texto="Esfenoides y estribo",es_correcta=False,pregunta_id=p_c_ciencia_2.id)
rp_c_ciencia_2_2 = Respuesta(texto="Metacarpo y yunque",es_correcta=False,pregunta_id=p_c_ciencia_2.id)
rp_c_ciencia_2_3 = Respuesta(texto="Yunque, martillo y estribo",es_correcta=True,pregunta_id=p_c_ciencia_2.id)
rp_c_ciencia_2_4 = Respuesta(texto="Martillo, estribo y esfenoides",es_correcta=False,pregunta_id=p_c_ciencia_2.id)

rp_c_ciencia_3_1 = Respuesta(texto="Pb",es_correcta=False,pregunta_id=p_c_ciencia_3.id)
rp_c_ciencia_3_2 = Respuesta(texto="Au",es_correcta=True,pregunta_id=p_c_ciencia_3.id)
rp_c_ciencia_3_3 = Respuesta(texto="P",es_correcta=False,pregunta_id=p_c_ciencia_3.id)
rp_c_ciencia_3_4 = Respuesta(texto="Na",es_correcta=False,pregunta_id=p_c_ciencia_3.id)

rp_c_ciencia_4_1 = Respuesta(texto="Reguladora de testosterona",es_correcta=False,pregunta_id=p_c_ciencia_4.id)
rp_c_ciencia_4_2 = Respuesta(texto="Reguladora de plaquetas",es_correcta=False,pregunta_id=p_c_ciencia_4.id)
rp_c_ciencia_4_3 = Respuesta(texto="Reguladora de glóbulos rojos",es_correcta=False,pregunta_id=p_c_ciencia_4.id)
rp_c_ciencia_4_4 = Respuesta(texto="Reguladora de azúcar",es_correcta=True,pregunta_id=p_c_ciencia_4.id)

rp_c_ciencia_5_1 = Respuesta(texto="Intensidad del viento",es_correcta=False,pregunta_id=p_c_ciencia_5.id)
rp_c_ciencia_5_2 = Respuesta(texto="Temblores de la tierra",es_correcta=True,pregunta_id=p_c_ciencia_5.id)
rp_c_ciencia_5_3 = Respuesta(texto="Radiación ultravioleta (UV)",es_correcta=False,pregunta_id=p_c_ciencia_5.id)
rp_c_ciencia_5_4 = Respuesta(texto="Cantidad de lluvia que cae en un lugar",es_correcta=False,pregunta_id=p_c_ciencia_5.id)

#repuestas categotia entretenimiento

rp_c_entre_1_1 = Respuesta(texto="Bolt",es_correcta=True,pregunta_id=p_c_entre_1.id)
rp_c_entre_1_2 = Respuesta(texto="Shrek",es_correcta=False,pregunta_id=p_c_entre_1.id)
rp_c_entre_1_3 = Respuesta(texto="El zorro y el sabueso",es_correcta=False,pregunta_id=p_c_entre_1.id)
rp_c_entre_1_4 = Respuesta(texto="Valiente",es_correcta=False,pregunta_id=p_c_entre_1.id)

rp_c_entre_2_1 = Respuesta(texto="Aladino",es_correcta=False,pregunta_id=p_c_entre_2.id)
rp_c_entre_2_2 = Respuesta(texto="La bella y la bestia",es_correcta=False,pregunta_id=p_c_entre_2.id)
rp_c_entre_2_3 = Respuesta(texto="El rey león",es_correcta=True,pregunta_id=p_c_entre_2.id)
rp_c_entre_2_4 = Respuesta(texto="La Cenicienta",es_correcta=False,pregunta_id=p_c_entre_2.id)

rp_c_entre_3_1 = Respuesta(texto="Rayos gamma",es_correcta=False,pregunta_id=p_c_entre_3.id)
rp_c_entre_3_2 = Respuesta(texto="Lo picó una araña",es_correcta=True,pregunta_id=p_c_entre_3.id)
rp_c_entre_3_3 = Respuesta(texto="Lo picó un escorpión",es_correcta=False,pregunta_id=p_c_entre_3.id)
rp_c_entre_3_4 = Respuesta(texto="Ninguna de las anteriores es correcta",es_correcta=False,pregunta_id=p_c_entre_3.id)

rp_c_entre_4_1 = Respuesta(texto="Dientes de sable",es_correcta=False,pregunta_id=p_c_entre_4.id)
rp_c_entre_4_2 = Respuesta(texto="Tortuga",es_correcta=False,pregunta_id=p_c_entre_4.id)
rp_c_entre_4_3 = Respuesta(texto="Suricata",es_correcta=False,pregunta_id=p_c_entre_4.id)
rp_c_entre_4_4 = Respuesta(texto="Mamut",es_correcta=True,pregunta_id=p_c_entre_4.id)

rp_c_entre_5_1 = Respuesta(texto="Gol",es_correcta=False,pregunta_id=p_c_entre_5.id)
rp_c_entre_5_2 = Respuesta(texto="Waka waka",es_correcta=True,pregunta_id=p_c_entre_5.id)
rp_c_entre_5_3 = Respuesta(texto="Banderas al viento",es_correcta=False,pregunta_id=p_c_entre_5.id)
rp_c_entre_5_4 = Respuesta(texto="Dare (la la la)",es_correcta=False,pregunta_id=p_c_entre_5.id)

db.session.add(rp_c_geogra_1_1)
db.session.add(rp_c_geogra_1_2)
db.session.add(rp_c_geogra_1_3)
db.session.add(rp_c_geogra_1_4)

db.session.add(rp_c_geogra_2_1)
db.session.add(rp_c_geogra_2_2)
db.session.add(rp_c_geogra_2_3)
db.session.add(rp_c_geogra_2_4)

db.session.add(rp_c_geogra_3_1)
db.session.add(rp_c_geogra_3_2)
db.session.add(rp_c_geogra_3_3)
db.session.add(rp_c_geogra_3_4)

db.session.add(rp_c_geogra_4_1)
db.session.add(rp_c_geogra_4_2)
db.session.add(rp_c_geogra_4_3)
db.session.add(rp_c_geogra_4_4)

db.session.add(rp_c_geogra_5_1)
db.session.add(rp_c_geogra_5_2)
db.session.add(rp_c_geogra_5_3)
db.session.add(rp_c_geogra_5_4)

db.session.add(rp_c_historia_1_1)
db.session.add(rp_c_historia_1_2)
db.session.add(rp_c_historia_1_3)
db.session.add(rp_c_historia_1_4)

db.session.add(rp_c_historia_2_1)
db.session.add(rp_c_historia_2_2)
db.session.add(rp_c_historia_2_3)
db.session.add(rp_c_historia_2_4)

db.session.add(rp_c_historia_3_1)
db.session.add(rp_c_historia_3_2)
db.session.add(rp_c_historia_3_3)
db.session.add(rp_c_historia_3_4)

db.session.add(rp_c_historia_4_1)
db.session.add(rp_c_historia_4_2)
db.session.add(rp_c_historia_4_3)
db.session.add(rp_c_historia_4_4)

db.session.add(rp_c_historia_5_1)
db.session.add(rp_c_historia_5_2)
db.session.add(rp_c_historia_5_3)
db.session.add(rp_c_historia_5_4)


db.session.add(rp_c_deporte_1_1)
db.session.add(rp_c_deporte_1_2)
db.session.add(rp_c_deporte_1_3)
db.session.add(rp_c_deporte_1_4)

db.session.add(rp_c_deporte_2_1)
db.session.add(rp_c_deporte_2_2)
db.session.add(rp_c_deporte_2_3)
db.session.add(rp_c_deporte_2_4)

db.session.add(rp_c_deporte_3_1)
db.session.add(rp_c_deporte_3_2)
db.session.add(rp_c_deporte_3_3)
db.session.add(rp_c_deporte_3_4)

db.session.add(rp_c_deporte_4_1)
db.session.add(rp_c_deporte_4_2)
db.session.add(rp_c_deporte_4_3)
db.session.add(rp_c_deporte_4_4)


db.session.add(rp_c_deporte_5_1)
db.session.commit()
db.session.add(rp_c_deporte_5_2)
db.session.add(rp_c_deporte_5_3)
db.session.add(rp_c_deporte_5_4)


db.session.add(rp_c_arte_1_1)
db.session.add(rp_c_arte_1_2)
db.session.add(rp_c_arte_1_3)
db.session.add(rp_c_arte_1_4)

db.session.add(rp_c_arte_2_1)
db.session.add(rp_c_arte_2_2)
db.session.add(rp_c_arte_2_3)
db.session.add(rp_c_arte_2_4)

db.session.add(rp_c_arte_3_1)
db.session.add(rp_c_arte_3_2)
db.session.add(rp_c_arte_3_3)
db.session.add(rp_c_arte_3_4)

db.session.add(rp_c_arte_4_1)
db.session.add(rp_c_arte_4_2)
db.session.add(rp_c_arte_4_3)
db.session.add(rp_c_arte_4_4)

db.session.add(rp_c_arte_5_1)
db.session.add(rp_c_arte_5_2)
db.session.add(rp_c_arte_5_3)
db.session.add(rp_c_arte_5_4)


db.session.add(rp_c_ciencia_1_1)
db.session.add(rp_c_ciencia_1_2)
db.session.add(rp_c_ciencia_1_3)
db.session.add(rp_c_ciencia_1_4)

db.session.add(rp_c_ciencia_2_1)
db.session.add(rp_c_ciencia_2_2)
db.session.add(rp_c_ciencia_2_3)
db.session.add(rp_c_ciencia_2_4)

db.session.add(rp_c_ciencia_3_1)
db.session.add(rp_c_ciencia_3_2)
db.session.add(rp_c_ciencia_3_3)
db.session.add(rp_c_ciencia_3_4)

db.session.add(rp_c_ciencia_4_1)
db.session.add(rp_c_ciencia_4_2)
db.session.add(rp_c_ciencia_4_3)
db.session.add(rp_c_ciencia_4_4)

db.session.add(rp_c_ciencia_5_1)
db.session.add(rp_c_ciencia_5_2)
db.session.add(rp_c_ciencia_5_3)
db.session.add(rp_c_ciencia_5_4)


db.session.add(rp_c_entre_1_1)
db.session.add(rp_c_entre_1_2)
db.session.add(rp_c_entre_1_3)
db.session.add(rp_c_entre_1_4)

db.session.add(rp_c_entre_2_1)
db.session.add(rp_c_entre_2_2)
db.session.add(rp_c_entre_2_3)
db.session.add(rp_c_entre_2_4)

db.session.add(rp_c_entre_3_1)
db.session.add(rp_c_entre_3_2)
db.session.add(rp_c_entre_3_3)
db.session.add(rp_c_entre_3_4)

db.session.add(rp_c_entre_4_1)
db.session.add(rp_c_entre_4_2)
db.session.add(rp_c_entre_4_3)
db.session.add(rp_c_entre_4_4)

db.session.add(rp_c_entre_5_1)
db.session.add(rp_c_entre_5_2)
db.session.add(rp_c_entre_5_3)
db.session.add(rp_c_entre_5_4)

db.session.commit()





