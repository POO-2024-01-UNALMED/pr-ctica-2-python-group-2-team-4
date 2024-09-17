from typing import List, Optional




class Persona:
    from gestorAplicacion.servicios.enums import Genero
    from gestorAplicacion.servicios.tienda import Tienda
    from gestorAplicacion.servicios.carrito import Carrito
    personas = []

    def __init__(self, nombre="", numero= 0, edad= 0, genero= None):
        self.nombre = nombre
        self.numero = numero
        self.edad = edad
        self.genero = genero
        Persona.personas.append(self)

    @classmethod
    def get_personas(cls) -> List['Persona']:
        return cls.personas

    @classmethod
    def set_personas(cls, personas: List['Persona']):
        cls.personas = personas

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_numero(self) -> int:
        return self.numero

    def set_id(self, id1):
        self.numero = id1

    def get_edad(self) -> int:
        return self.edad

    def set_edad(self, edad: int):
        self.edad = edad

    def get_genero(self) -> Optional[Genero]:
        return self.genero

    def set_genero(self, genero: Genero):
        self.genero = genero

    def mayor_edad(self) -> bool:
        return self.edad >= 18

    def get_tiendas_con_facturas(self) -> Optional[List['Tienda']]:
        return None

    def get_facturas1(self, tienda_seleccionada: 'Tienda') -> Optional[List['Carrito']]:
        return None

    def mostrar_facturas(self):
        pass
