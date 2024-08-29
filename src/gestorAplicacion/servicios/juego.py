from abc import ABC, abstractmethod

class Juego(ABC):

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jugar(self, posicion: int) -> bool:
        pass

    @abstractmethod
    def ha_ganado(self) -> bool:
        pass

    @abstractmethod
    def ha_perdido(self) -> bool:
        pass

    @abstractmethod
    def obtener_estado(self) -> str:
        pass
