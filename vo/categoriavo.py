class CategoriaVO:
    
    
    def __init__(self,id,nombre,visible):
        self.id=id
        self.nombre=nombre
        self.visible= visible
    
    
    def add_visible(self,visible):
        self.visible=visible