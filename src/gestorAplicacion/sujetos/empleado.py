from gestorAplicacion.sujetos.persona import Persona
#from gestorAplicacion.servicios.enums import Genero, TipoEmpleado
#from gestorAplicacion.servicios.tienda import Tienda

class Empleado(Persona):
    # Atributos----------------------------------------------------------------------------------------------------
    
    def __init__(self, nombre=None, id=None, edad=None, genero=None, liquidacion=0.0, tienda=None,prestacion_salud=False, prestacion_pension=False, tipo=None, experiencia=0):
        super().__init__(nombre, id, edad, genero)
        self._liquidacion = liquidacion
        self._prestacion_salud = prestacion_salud
        self._prestacion_pension = prestacion_pension
        self._experiencia = experiencia
        self._tienda = tienda
        self._tipo = tipo

    # Métodos------------------------------------------------------------------------------------------------------
    
    def get_tipo(self):
        return self.tipo

    def get_liquidacion(self):
        return self.liquidacion

    def set_liquidacion(self, liquidacion):
        self.liquidacion = liquidacion

    def get_tienda(self):
        return self.tienda

    def set_tienda(self, tienda):
        self.tienda = tienda

    def is_prestacion_salud(self):
        return self.prestacionSalud

    def set_prestacion_salud(self, prestacion_salud):
        self.prestacionSalud = prestacion_salud

    def is_prestacion_pension(self):
        return self.prestacionPension

    def set_prestacion_pension(self, prestacion_pension):
        self.prestacionPension = prestacion_pension

    def get_experiencia(self):
        return self.experiencia

    def set_experiencia(self, experiencia):
        self.experiencia = experiencia

    def set_tipo(self, tipo):
        self.tipo = tipo

    # Métodos abstractos------------------------------------------------------------------------------------------------------

    def busco_chamba(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def cantidad_pago(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def validar_criterios(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
