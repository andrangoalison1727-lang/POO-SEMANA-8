from .producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, codigo: str, precio: float, tamano: str):
        super().__init__(nombre, codigo, precio, "Bebida")
        self.tamano = tamano

    def mostrar_informacion(self) -> None:
        print(
            f"Producto: {self.nombre}, "
            f"Código: {self.codigo}, "
            f"Precio: ${self.precio:.2f}, "
            f"Categoría: {self.categoria}, "
            f"Tamano: {self.tamano}"
        )