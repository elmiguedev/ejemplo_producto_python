# 1- creo el controlador de producto
from Backend.Controladores.ControladorProducto import ControladorProductos


controlador_producto = ControladorProductos()

# 2- pruebo el caso de uso OBTENER PRODUCTOS
productos = controlador_producto.obtener_productos()
print(productos)

# 3- pruebo el caso de uso MODIFICAR PRODUCTO
producto_a_modificar = productos[0]
producto_a_modificar.setNombre("Raton")
controlador_producto.modificar_producto(producto_a_modificar)



# Ejemplo de un caso de uso de modificar
# -----------------------------------------
# El caso de uso comienza cuando el usuario selecciona de la lista de productos el producto a producto_a_modificar
# el sistema muestra los datos del proudcto seleccionado
# el sistema solicita se modfique el nombre
# el usuario modifica el nombre 
# el sistema solicita se guarden los cambios
# el usuario sleleciona la opcion guardar cambio
# el sistema modifica el producto con los nuevos vlaores
# fin caso de uso