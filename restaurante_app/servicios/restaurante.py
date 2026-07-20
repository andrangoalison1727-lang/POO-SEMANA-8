from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            return False
        
        self.productos.append(producto)
        return True
    
    def registrar_cliente(self, cliente: Cliente) -> bool:
        if self._existe_identificacion_cliente(cliente.identificacion):
            return False

        self.clientes.append(cliente)
        return True
    
    def listar_productos(self) -> None:
        for producto in self.productos:
            producto.mostrar_informacion()

    def listar_clientes(self) -> None:
        for cliente in self.clientes:
            cliente.mostrar_informacion()
    
    def _existe_codigo_producto(self, codigo: str) -> bool:
        for producto in self.productos:
            if producto.codigo == codigo:
                return True
        return False

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return True
        return False

