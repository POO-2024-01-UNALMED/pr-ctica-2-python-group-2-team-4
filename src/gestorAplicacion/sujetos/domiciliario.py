
from gestorAplicacion.servicios.enums import Genero, TipoEmpleado
from gestorAplicacion.servicios.tienda import Tienda
from gestorAplicacion.sujetos.empleado import Empleado

class Domiciliario(Empleado):
    def __init__(self, nombre=None, id=None, edad=None, genero=None, liquidacion=0, tienda=None, prestacion_salud=False, prestacion_pension=False, licencia=False, vehiculo=None):
        super().__init__(nombre, id, edad, genero, liquidacion, tienda, prestacion_salud, prestacion_pension, TipoEmpleado.DOMICILIARIO)
        self.vehiculo = vehiculo
        self.licencia = licencia
        if tienda is not None:
            Tienda.get_desempleados().append(self)

    def busco_chamba(self):
        # Método que debe ser implementado
        pass

    def cantidad_pago(self):
        # Método que debe ser implementado
        return 0

    def validar_criterios(self):
        return self.licencia and self.vehiculo is not None
