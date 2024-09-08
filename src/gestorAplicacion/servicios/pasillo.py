class Pasillo:
    # Atributos
    def __init__(self, nombre=None,productos=None, categoria=None, tienda=None):
        self.nombre = nombre
        self.categoria = categoria
        self.tienda = tienda
        self.productos = productos if productos is not None else []

        if tienda is not None:
            tienda.get_pasillos().append(self)

    # Getters y Setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_productos(self):
        return self.productos

    def set_productos(self, productos):
        self.productos = productos

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_tienda(self):
        return self.tienda

    def set_tienda(self, tienda):
        self.tienda = tienda

    # Métodos estáticos
    @staticmethod
    def cantidad_producto(productos, id_producto):
        contador = 0
        for producto in productos:
            if producto.get_id() == id_producto:
                contador += 1
        return contador

    @staticmethod
    def verificar_disponibilidad(lista_productos, id_producto, cantidad_solicitada):
        cantidad = Pasillo.cantidad_producto(lista_productos, id_producto)
        return cantidad_solicitada <= cantidad

    # Otros métodos
    def asignar_tienda(self, tienda):
        self.tienda = tienda
        tienda.get_pasillos().append(self)

    def agregar_producto(self, producto):
        self.get_productos().append(producto)
        producto.set_pasillo(self)

