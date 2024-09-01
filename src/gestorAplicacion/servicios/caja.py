from typing import List

from gestorAplicacion.servicios.enums import TipoCaja
#from gestorAplicacion.sujetos.cajero import Persona
#from gestorAplicacion.sujetos.cliente import Tienda


class Caja:
    # Atributos
    def __init__(self, nombre=None, tipo=None, tienda=None):
        self._nombre = nombre
        self._estado = 2
        self._tipo = tipo
        self._tienda = tienda
        self._cajero = None
        self._cliente = None

        # Si la tienda no es None, añade esta caja a la lista de cajas de la tienda
        if tienda is not None:
            tienda.get_cajas().append(self)

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def tienda(self):
        return self._tienda

    @tienda.setter
    def tienda(self, tienda):
        self._tienda = tienda

    @property
    def cajero(self):
        return self._cajero

    @cajero.setter
    def cajero(self, cajero):
        self._cajero = cajero

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

   