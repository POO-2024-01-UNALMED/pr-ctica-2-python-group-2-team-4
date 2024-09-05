from gestorAplicacion.servicios.juego import Juego
from typing import Set
class Ahorcado(Juego):
    def __init__(self, palabra: str):
        self.palabra = palabra.lower()
        self.letras_adivinadas: Set[str] = set()
        self.letras_incorrectas: Set[str] = set()
        self.errores = 0

    def iniciar(self):
        # Inicializa el juego, puedes agregar lógica si lo necesitas
        self.letras_adivinadas.clear()
        self.letras_incorrectas.clear()
        self.errores = 0
        print("¡El juego ha comenzado!")

    def jugar(self, letra):
        if letra in self.palabra:
            self.letras_adivinadas.add(letra)
            return True
        else:
            self.letras_incorrectas.add(letra)
            self.errores += 1
            return False

    def ha_ganado(self) -> bool:
        return all(letra in self.letras_adivinadas for letra in self.palabra)

    def ha_perdido(self) -> bool:
        return self.errores >= 6

    def obtener_estado(self) -> str:
        estado = ''.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])
        estado += f"\nLetras incorrectas: {', '.join(self.letras_incorrectas)}"
        estado += f"\nErrores: {self.errores}"
        return estado
