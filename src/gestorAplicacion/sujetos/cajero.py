from gestorAplicacion.servicios import Caja, Tienda
from gestorAplicacion.servicios.enums import Genero, TipoEmpleado
from gestorAplicacion.sujetos.empleado import Empleado

class Cajero(Empleado):
    def __init__(self, nombre=None, id=None, edad=None, genero=None, liquidacion=0, tienda=None, prestacion_salud=False, prestacion_pension=False, experiencia=0, caja=None):
        super().__init__(nombre, id, edad, genero, liquidacion, tienda, prestacion_salud, prestacion_pension, TipoEmpleado.CAJERO, experiencia)
        self.caja = caja
        if tienda is not None:
            tienda.get_empleados().append(self)
        if caja is not None:
            caja.set_cajero(self)

    def get_caja(self):
        return self.caja

    def set_caja(self, caja):
        self.caja = caja

    def busco_chamba(self):
        # Método que debe ser implementado
        pass

    def cantidad_pago(self):
        # Método que debe ser implementado
        return 0

    def validar_criterios(self):
        return self.experiencia >= 2 and self.edad <= 25
