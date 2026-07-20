class Cliente:
    def __init__(self, nombre: str, email: str, identificacion: str):
        self.nombre = nombre
        self.email = email
        self.identificacion = identificacion

    def mostrar_informacion(self) -> None:
        print (f"Cliente: {self.nombre}, Email: {self.email}, Identificacion: {self.identificacion}")