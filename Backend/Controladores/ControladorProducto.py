from Entidades.Producto import Producto
from Utils.conexion import connection

class ControladorProductos():

    def obtener_productos(_self_):
        consulta = "SELECT * FROM Producto p"
        query = connection.cursor().execute(consulta)
        productos = []
        
        for row in query:
            producto = Producto(row[0], row[1], row[2], row[3], row[4])
            productos.append(producto)
            
        return productos
    
    def modificar_producto(_self_, producto):
        consulta = "UPDATE Producto SET nombre = ?, stock = ?, categoria = ?, precio = ? WHERE id = ?"
        connection.cursor().execute(consulta, (producto.getNombre(), producto.getStock(), producto.getCategoria(), producto.getPrecio(), producto.getId()))
        connection.commit()
        
            

    