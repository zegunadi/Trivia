class PreguntaVO:
    
    def __init__(self,id,texto,categoria_id):
        self.id=id
        self.texto=texto
        self.categoria_id=categoria_id
        self.repuestas=[]
        self.resultado=""
        
    def add_repuesta(self,repuesta):
        self.repuestas.append(repuesta)
        
    def add_resultado(self,resultado):
        self.resultado=resultado