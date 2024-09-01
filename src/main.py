import sys

import importlib

from uiMain.funcionalidad1 import Funcionalidad1
from uiMain.funcionalidad2 import Funcionalidad2
from uiMain.funcionalidad3 import Funcionalidad3
from uiMain.funcionalidad4 import Funcionalidad4
from uiMain.funcionalidad5 import Funcionalidad5
from uiMain.identidad import Identidad

class Main(Identidad):
    @classmethod
    def lineas(cls):
        print("-" * 160)

    @classmethod
    def escaner(cls):
        try:
            p = int(input())
        except ValueError:
            print("Este no es un número válido")
            print("Introduzca otro número: ", end="")
            p = Main.escaner()
        return p

    @classmethod
    def escaner_con_rango(cls,rango):
        try:
            p = int(input())
        except ValueError:
            print("Este no es un número válido")
            print("Introduzca otro número: ", end="")
            p = Main.escaner_con_rango(rango)
        if p < 1 or p > rango:
            print("Este número está fuera del rango")
            print("Introduzca otro número: ", end="")
            p = Main.escaner_con_rango(rango)
        return p

    @staticmethod
    def main():
        # Deserializador.deserializar_listas()
        Main.escoger_funcionalidad()

    @staticmethod
    def escoger_funcionalidad():
        while True:
            numeros = [1, 2, 3, 4, 5, 6]
            boleano = False
            
            Main.lineas()
            print("""
                ______________________________
               /  /  /   /   /   /   /   /   /|
              /  /  /   /   /   /   /   /   / |
             /__/__/___/___/___/___/___/___/__| 
             |  ______            ______  |   | 
             | |      |          |      | |   |
             | |      |          |      | |   |     My_Tiendita
             | |______|          |______| |   |
             |            ____            |   |
             |           |    |           |   |
             |           |    |           |   /
             |___________|____|___________|__/
                """)
            Main.lineas()
            print("Bienvenido a My_Tiendita, ¿qué desea hacer?")
            print("")
            print(" 1. Ecosistema de Consultas Personalizadas\n"
                " 2. Escoger productos\n"
                " 3. Pagar recibos pendientes\n"
                " 4. Revisar tienda\n"
                " 5. Personalizar y modificar tiendas\n"
                " 6. Terminar")
            print("")
            decision = None
            
            while not boleano:
                try:
                    decision = int(input("Escoja un número: "))
                except ValueError:
                    print("Este no es un número válido")
                    continue

                if decision in numeros:
                    boleano = True
                else:
                    print("El número está fuera del rango")
            
            match decision:
                case 1:
                    Funcionalidad1.consultas_eco()
                case 2:
                    cliente = Identidad.identificar_persona()
                    Funcionalidad2.elegir_tipo_busqueda(cliente)
                case 3:
                    Funcionalidad3.impresion_facturas()
                case 4:
                    Funcionalidad4.seleccion_tienda()
                case 5:
                    admin = Identidad.identificar_persona()
                    Funcionalidad5.personalizar_tienda(admin)
                case 6:
                    # Serializador.serializar_todo()
                    print("Ha salido del programa")
                    sys.exit(0)

if __name__ == "__main__":
    Main.main()
