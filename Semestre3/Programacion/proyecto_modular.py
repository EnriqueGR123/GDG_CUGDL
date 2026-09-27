class Tienda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio >= 0:
            self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        return f"{self.nombre} - ${self.__precio} - Cantidad: {self.__cantidad}"


class Bebida(Tienda):
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.tamaño = tamaño

    def mostrar(self):
        return f"Bebida: {self.nombre}, ${self.precio}, {self.tamaño}"


class Fritura(Tienda):
    def __init__(self, nombre, precio, cantidad, gramos):
        super().__init__(nombre, precio, cantidad)
        self.gramos = gramos

    def mostrar(self):
        return f"Fritura: {self.nombre}, ${self.precio}, {self.gramos}g"


class Dulce(Tienda):
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre, precio, cantidad)
        self.tipo = tipo

    def mostrar(self):
        return f"Dulce: {self.nombre}, ${self.precio}, Tipo: {self.tipo}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar_todos(self):
        for producto in self.productos:
            print(f'{producto.mostrar()}')



inventario = Inventario()

while True:
    print("1. Agregar bebida\n2. Agregar fritura\n3. Agregar dulce\n4. Mostrar productos\n5. Salir")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        tamaño = input("Tamaño: ")
        inventario.agregar(Bebida(nombre, precio, cantidad, tamaño))
    elif opcion == "2":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        gramos = int(input("Gramos: "))
        inventario.agregar(Fritura(nombre, precio, cantidad, gramos))
    elif opcion == "3":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        tipo = input("Tipo: ")
        inventario.agregar(Dulce(nombre, precio, cantidad, tipo))
    elif opcion == "4":
        inventario.mostrar_todos()
    elif opcion == "5":
        print("aidos")
        break
    else:
        print('Opcion no existe ')