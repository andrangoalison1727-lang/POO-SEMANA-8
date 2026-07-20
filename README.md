# Sistema de Gestión de Restaurante - restaurante_app

## Nombre del estudiante

Alison Dayana Andrango Nieto

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema básico de gestión para un restaurante utilizando Programación Orientada a Objetos en Python.

El sistema permite registrar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola. Además, se aplican principios SOLID como responsabilidad única, abierto/cerrado y sustitución de Liskov, con el objetivo de mantener una estructura organizada, modular y fácil de ampliar.

## Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py

Responsabilidad de las clases
Producto
Representa los datos generales de un producto del restaurante, como nombre, código, precio y categoría. Contiene el método mostrar_informacion() para mostrar sus datos.

Bebida
Hereda de la clase Producto e incorpora información específica como el tamaño de la bebida. Sobrescribe el método mostrar_informacion() para mostrar sus características.

Cliente
Representa la información de los clientes registrados, como nombre, correo e identificación.

Restaurante
Es la clase encargada de administrar los productos y clientes. Permite registrar, listar y validar que no existan códigos o identificaciones repetidas.

main.py
Es el punto de inicio del programa. Se encarga del menú interactivo, solicitar datos mediante input(), crear objetos y comunicarse con la clase Restaurante.

Aplicación de principios SOLID
Responsabilidad única (SRP)
Cada clase cumple una función específica: Producto y Bebida representan productos, Cliente representa clientes, Restaurante administra las operaciones y main.py controla la interacción con el usuario.

Abierto/Cerrado (OCP)
La clase Bebida permite ampliar el sistema agregando un nuevo tipo de producto sin modificar la lógica principal de Restaurante.

Sustitución de Liskov (LSP)
Los objetos Producto y Bebida pueden almacenarse en la misma lista y utilizar el método mostrar_informacion() sin necesidad de diferenciarlos mediante condiciones.

Funcionamiento del sistema
El sistema permite:


Registrar productos.

Registrar bebidas.

Registrar clientes.

Listar productos y bebidas.

Listar clientes.

Validar códigos de productos repetidos.

Validar identificaciones de clientes repetidas.
Los objetos son creados a partir de los datos ingresados por el usuario mediante consola.

Ejecución del proyecto
Para ejecutar el programa se utiliza:


python main.py


El sistema mostrará un menú interactivo donde el usuario podrá seleccionar las opciones disponibles.

Relación entre Producto y Bebida
La clase Bebida utiliza herencia porque representa un tipo específico de Producto. Esto permite reutilizar atributos y aplicar polimorfismo, ya que ambas clases pueden utilizar el método común mostrar_informacion().

Pruebas realizadas
Se comprobó el funcionamiento del sistema mediante:


Registro de productos, bebidas y clientes.

Listado de información registrada.

Validación de códigos duplicados.

Validación de identificaciones duplicadas.

Ejecución correcta desde main.py.
Reflexión
La organización modular permite crear programas más ordenados, donde cada clase tiene una responsabilidad definida. La aplicación de principios SOLID facilita mantener y ampliar el sistema sin afectar las funcionalidades existentes.