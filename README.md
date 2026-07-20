# Sistema de Gestión de Restaurante - restaurante_app

## Nombre del estudiante

Alison Dayana Andrango Nieto

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema básico de gestión para un restaurante utilizando Programación Orientada a Objetos en Python.

El sistema permite registrar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola. Además, se aplican principios SOLID como responsabilidad única, abierto/cerrado y sustitución de Liskov, con la finalidad de mantener una estructura organizada, modular y fácil de ampliar.

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
```

## Responsabilidad de las clases

### Producto

Representa los datos generales de un producto del restaurante, como nombre, código, precio y categoría. Además, contiene el método `mostrar_informacion()` para mostrar sus datos.

### Bebida

Hereda de la clase Producto porque una bebida representa un tipo específico de producto dentro del restaurante. Esta clase agrega información propia como el tamaño y sobrescribe el método `mostrar_informacion()` para mostrar sus características.

### Cliente

Representa la información de los clientes registrados en el restaurante, como nombre, correo e identificación.

### Restaurante

Es la clase encargada de administrar los productos y clientes. Permite registrar nuevos elementos, listar la información y validar que no existan códigos de productos o identificaciones repetidas.

### main.py

Es el punto de inicio del programa. Se encarga de mostrar el menú interactivo, solicitar los datos mediante `input()`, crear los objetos y comunicarse con la clase Restaurante.

## Aplicación de principios SOLID

### Responsabilidad única (SRP)

Cada clase cumple una función específica dentro del sistema:

- Producto y Bebida representan los productos del restaurante.
- Cliente representa la información de los clientes.
- Restaurante administra las operaciones y colecciones.
- `main.py` controla la interacción con el usuario.

Esto permite mantener el código más organizado y fácil de modificar.

### Abierto/Cerrado (OCP)

La clase Bebida permite ampliar el sistema agregando un nuevo tipo de producto sin modificar la lógica principal de la clase Restaurante.

### Sustitución de Liskov (LSP)

Los objetos Producto y Bebida pueden almacenarse dentro de la misma lista y utilizar el método común `mostrar_informacion()` sin necesidad de utilizar condiciones para diferenciarlos.

## Funcionamiento del sistema

El sistema permite:

- Registrar productos.
- Registrar bebidas.
- Registrar clientes.
- Listar productos y bebidas.
- Listar clientes.
- Validar códigos de productos repetidos.
- Validar identificaciones de clientes repetidas.

Los objetos son creados a partir de los datos ingresados por el usuario mediante consola.

## Relación entre Producto y Bebida

La relación entre Producto y Bebida se basa en la herencia.

Una Bebida es un tipo específico de Producto, por lo que puede utilizar los atributos generales como nombre, código, precio y categoría, pero también puede agregar características propias como el tamaño.

Esto permite aplicar polimorfismo, ya que ambas clases pueden utilizar el método común `mostrar_informacion()`.

## Ejecución del proyecto

Para ejecutar el programa se utiliza:

```bash
python main.py
```

Al iniciar el programa aparecerá un menú interactivo donde el usuario podrá seleccionar las diferentes opciones disponibles.

## Pruebas realizadas

Se comprobó el funcionamiento del sistema mediante:

- Registro de productos, bebidas y clientes.
- Listado de información registrada.
- Validación de códigos duplicados.
- Validación de identificaciones duplicadas.
- Ejecución correcta desde `main.py`.

## Reflexión

La organización modular permite crear programas más ordenados, donde cada clase tiene una responsabilidad definida. La aplicación de principios SOLID ayuda a mantener y ampliar el sistema de una manera más sencilla, evitando afectar las funcionalidades que ya existen.