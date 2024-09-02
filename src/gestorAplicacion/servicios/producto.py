from datetime import date
from copy import deepcopy

class Producto:
    IVA = 0.19
    fecha_actual = date.today()


    def __init__(self, nombre, marca=None, precio=0.0, tamano=None, edad_valida=None, id=None,
                 categoria=None, descripcion="", fecha_perecer=None, pasillo=None, tienda=None):
        from gestorAplicacion.servicios.enums import EstadoProducto
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.tamano = tamano
        self.edad_valida = edad_valida
        self.id = id
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha_perecer = fecha_perecer
        self.pasillo = pasillo
        self.tienda = tienda
        self.estado = EstadoProducto.ACTIVO

    def get_precio(self):
        return self.precio + (self.precio * self.IVA)

    def cantidad_producto(self):
        cantidad = 0
        if self.tienda:
            for pasillo in self.tienda.get_pasillos():
                for producto in pasillo.get_productos():
                    if producto == self:
                        cantidad += 1
        return cantidad

    def asignar_pasillo_y_poner_en_tienda(self, pasillo):
        self.pasillo = pasillo
        pasillo.get_productos().append(self)

    def asignar_tienda(self, tienda):
        self.tienda = tienda

    @staticmethod
    def filtrar_por_edad(productos, cliente):
        from gestorAplicacion.servicios.enums import Edades
        productos_adecuados = []
        for producto in productos:
            if cliente.mayor_edad() and producto.edad_valida == Edades.ADULTOS:
                productos_adecuados.append(producto)
            elif not cliente.mayor_edad() and producto.edad_valida == Edades.MENORES:
                productos_adecuados.append(producto)
        return productos_adecuados

    @staticmethod
    def filtrar_por_edad_y_categoria(productos, cliente, categoria):
        from gestorAplicacion.servicios.enums import Edades
        productos_adecuados = []
        for producto in productos:
            if producto.categoria == categoria:
                if cliente.mayor_edad() and (producto.edad_valida == Edades.ADULTOS or producto.edad_valida == Edades.MENORES):
                    productos_adecuados.append(producto)
                elif not cliente.mayor_edad() and producto.edad_valida == Edades.MENORES:
                    productos_adecuados.append(producto)
        return productos_adecuados

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.nombre}\t{self.marca}\t{self.tamano}\t{self.precio}"

    def clone(self):
        return deepcopy(self)