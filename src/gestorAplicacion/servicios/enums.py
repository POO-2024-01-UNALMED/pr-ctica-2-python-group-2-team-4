from enum import Enum

class Categoria(Enum):
    ALIMENTO = (1, "Alimento")
    BEBIDA = (2, "Bebida")
    LIMPIEZA = (3, "Limpieza")
    PERSONAL = (4, "Personal")
    HOGAR = (5, "Hogar")
    ELECTRONICO = (6, "Electrónico")
    
    def __init__(self, identificador, texto):
        self.identificador = identificador
        self.texto = texto

    def get_texto(self):
        return self.texto

    @staticmethod
    def resolver_enum(decision):
        for categoria in Categoria:
            if decision == categoria.identificador:
                return categoria
        return None

class Edades(Enum):
    MENORES = "-18"
    ADULTOS = "+18"

class EstadoProducto(Enum):
    VENCIDO = "Vencido"
    DEFECTUOSO = "Defectuoso"
    ACTIVO = "Activo"

class TipoCaja(Enum):
    NORMAL = "Normal"
    RAPIDA = "Rápida"
    
    def __init__(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo
    @staticmethod
    def resolver_tipo_caja(tipo):
        for caja in TipoCaja:
            if tipo == caja.tipo:
                return caja
        return None

class Tamano(Enum):
    GRANDE = "Grande"
    MEDIANO = "Mediano"
    PEQUENO = "Pequeno"
    
    def __init__(self, tamano):
        self._tamano = tamano

    def get_tamano(self):
        return self._tamano

class Genero(Enum):
    H = "H"
    M = "M"

class TipoEmpleado(Enum):
    CAJERO = "Cajero"
    CONSERJE = "Conserje"
    DOMICILIARIO = "Domiciliario"
    
    def __init__(self, tipo):
        self.tipo = tipo

class RazonDevolucion(Enum):
    DEFECTUOSO = "Defectuoso"
    INCONFORME = "Inconforme"

class Membresia(Enum):
    BASICO = 10000.0
    PREMIUM = 25000.0
    VIP = 50000.0
    
    def __init__(self, precio):
        self.precio = precio
    
    def get_precio(self):
        return self.precio
