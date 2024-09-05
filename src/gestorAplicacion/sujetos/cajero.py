#from gestorAplicacion.servicios.caja import Caja, Tienda
from gestorAplicacion.servicios.enums import TipoEmpleado#,Genero 
from gestorAplicacion.sujetos.empleado import Empleado

class Cajero(Empleado):
    def __init__(self, nombre=None, id=None, edad=None, genero=None, liquidacion=0, tienda=None, prestacion_salud=False,
                 prestacion_pension=False, experiencia=0, caja=None):
        # Inicializar atributos de la superclase
        super().__init__(nombre, id, edad, genero, liquidacion, tienda, prestacion_salud, prestacion_pension,
                         TipoEmpleado.CAJERO, experiencia)

        # Inicializar atributos específicos de la clase Cajero
        self._caja = caja

        # Establecer relaciones
        if tienda is not None:
            tienda.get_empleados().append(self)

        if caja is not None:
            caja.set_cajero(self)

    def get_caja(self):
        return self._caja

    def set_caja(self, caja):
        self._caja = caja
        if caja is not None:
            caja.set_cajero(self)
        else:
            if self._caja is not None:
                self._caja.set_cajero(None)

    # Métodos get y set para otros atributos si es necesario
    # (Ejemplo)
    def get_liquidacion(self):
        return self._liquidacion

    def set_liquidacion(self, liquidacion):
        self._liquidacion = liquidacion

    def get_prestacion_salud(self):
        return self._prestacion_salud

    def set_prestacion_salud(self, prestacion_salud):
        self._prestacion_salud = prestacion_salud

    def get_prestacion_pension(self):
        return self._prestacion_pension

    def set_prestacion_pension(self, prestacion_pension):
        self._prestacion_pension = prestacion_pension

    def get_experiencia(self):
        return self._experiencia

    def set_experiencia(self, experiencia):
        self._experiencia = experiencia

    def busco_chamba(self):
        # Método que debe ser implementado
        pass

    def cantidad_pago(self):
        # Método que debe ser implementado
        return 0

    def validar_criterios(self):
        return self.experiencia >= 2 and self.edad <= 25
