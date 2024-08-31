from gestorAplicacion.servicios.juego import Juego
import random
class TresEnRaya(Juego):
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador = 'X'
        self.maquina = 'O'

    def iniciar(self):
        # Inicializa el tablero y establece el jugador inicial
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        print("¡El juego de Tres en Raya ha comenzado!")

    def jugar(self, posicion: int) -> bool:
        fila = posicion // 3
        columna = posicion % 3
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.jugador
            if not self.ha_ganado():
                self.jugar_maquina()
            return True
        return False

    def jugar_maquina(self):
        fila, columna = 0, 0
        while True:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            if self.tablero[fila][columna] == ' ':
                break
        self.tablero[fila][columna] = self.maquina

    def ha_ganado(self) -> bool:
        return self.check_win(self.jugador) or self.check_win(self.maquina)

    def check_win(self, jugador: str) -> bool:
        # Verifica las filas y columnas
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)) or \
                all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        # Verifica las diagonales
        if self.tablero[0][0] == jugador and self.tablero[1][1] == jugador and self.tablero[2][2] == jugador:
            return True
        if self.tablero[0][2] == jugador and self.tablero[1][1] == jugador and self.tablero[2][0] == jugador:
            return True
        return False

    def ha_perdido(self) -> bool:
        return self.ha_ganado() and not self.hay_espacios()

    def hay_espacios(self) -> bool:
        return any(self.tablero[i][j] == ' ' for i in range(3) for j in range(3))

    def obtener_estado(self) -> str:
        sb = []
        for i in range(3):
            sb.append(" | ".join(self.tablero[i]))
            if i < 2:
                sb.append("\n---------\n")
        return "".join(sb)
