class Producto:
    def __init__(self, nombre: str, codigo: str, precio: float, categoria: str):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.categoria = categoria


    def mostrar_informacion(self) -> None:
        print (f"Producto: {self.nombre}, Código: {self.codigo}, Precio: ${self.precio:.2f}, Categoría: {self.categoria}")