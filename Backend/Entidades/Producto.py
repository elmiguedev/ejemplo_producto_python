class Producto():
    def __init__(self, id, nombre, stock, categoria, precio ):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio
   
    def getStock(self):
        return self.stock   
    
    def setStock(self, stock):
        self.stock = stock
    
    def getCategoria(self):
        return self.categoria
    
    def setCategoria(self, categoria):
        self.categoria = categoria
