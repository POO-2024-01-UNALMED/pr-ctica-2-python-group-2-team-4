from datetime import date
from copy import deepcopy

class Producto:
    IVA = 0.19
    fecha_actual = date.today()


    def __init__(self, nombre, marca=None, precio=0.0, tamano=None, edad_valida=None,
                 categoria=None, descripcion="", fecha_perecer=None, id=None, pasillo=None, tienda=None):
        from gestorAplicacion.servicios.enums import EstadoProducto
        self._nombre = nombre
        self._marca = marca
        self._precio = precio
        self._tamano = tamano
        self._edad_valida = edad_valida
        self._id = id
        self._categoria = categoria
        self._descripcion = descripcion
        self._fecha_perecer = fecha_perecer
        self._pasillo = pasillo
        self._tienda = tienda
        self._estado = EstadoProducto.ACTIVO

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def set_precio(self, precio):
        self._precio = precio

    def get_tamano(self):
        return self._tamano

    def set_tamano(self, tamano):
        self._tamano = tamano

    def get_edad_valida(self):
        return self._edad_valida

    def set_edad_valida(self, edad_valida):
        self._edad_valida = edad_valida

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def get_fecha_perecer(self):
        return self._fecha_perecer

    def set_fecha_perecer(self, fecha_perecer):
        self._fecha_perecer = fecha_perecer

    def get_pasillo(self):
        return self._pasillo

    def set_pasillo(self, pasillo):
        self._pasillo = pasillo

    def get_tienda(self):
        return self._tienda

    def set_tienda(self, tienda):
        self._tienda = tienda

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_precio(self):
        return self._precio + (self._precio * self.IVA)

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
            return self._id == other.get_id()
        return False

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"{self._nombre}\t{self._marca}\t{self._tamano}\t{self._precio}"

    def clone(self):
        return deepcopy(self)