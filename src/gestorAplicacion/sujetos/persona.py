from typing import List, Optional


class Persona:
    from gestorAplicacion.servicios.enums import Genero
    from gestorAplicacion.servicios.tienda import Tienda
    personas: List['Persona'] = []

    def __init__(self, nombre: str = "", id: int = 0, edad: int = 0, genero: Genero = None):
        self.nombre = nombre
        self.id = id
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

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

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

    def get_facturas(self, tienda_seleccionada: 'Tienda') -> Optional[List['Carrito']]:
        return None

    def mostrar_facturas(self):
        pass
