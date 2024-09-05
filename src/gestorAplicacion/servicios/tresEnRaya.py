from gestorAplicacion.servicios.juego import Juego
import random
import random


class TresEnRaya(Juego):
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador = 'X'
        self.maquina = 'O'

    def iniciar(self):
        # Inicializa el tablero y establece el jugador inicial
        pass

    def jugar(self, posicion):
        # Convertir la posición de 1-9 a índices de fila y columna (0-2)
        posicion -= 1
        fila = posicion // 3
        columna = posicion % 3

        if 0 <= fila < 3 and 0 <= columna < 3 and self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.jugador
            if not self.ha_ganado():
                self.jugar_maquina()
            return True
        return False

    def jugar_maquina(self):
        espacios_libres = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == ' ']
        fila, columna = random.choice(espacios_libres)
        self.tablero[fila][columna] = self.maquina

    def ha_ganado(self):
        return self.check_win(self.jugador) or self.check_win(self.maquina)

    def check_win(self, jugador):
        # Verificar filas y columnas
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)):
                return True
            if all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        # Verificar diagonales
        if all(self.tablero[i][i] == jugador for i in range(3)):
            return True
        if all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    def ha_perdido(self):
        return not self.ha_ganado() and not self.hay_espacios()

    def hay_espacios(self):
        return any(self.tablero[i][j] == ' ' for i in range(3) for j in range(3))

    def obtener_estado(self):
        lines = []
        for i in range(3):
            row = ' | '.join(self.tablero[i])
            lines.append(row)
            if i < 2:
                lines.append('---------')
        return '\n'.join(lines)
