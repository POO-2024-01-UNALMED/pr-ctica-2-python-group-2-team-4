import funcionalidad1
import funcionalidad2
import funcionalidad3
import funcionalidad4
from uiMain.funcionalidad5 import funcionalidad5
from uiMain.identidad import Identidad
import sys

def lineas():
    print("-" * 160)

def escaner():
    try:
        p = int(input())
    except ValueError:
        print("Este no es un número válido")
        print("Introduzca otro número: ", end="")
        p = escaner()
    return p

def escaner_con_rango(rango):
    try:
        p = int(input())
    except ValueError:
        print("Este no es un número válido")
        print("Introduzca otro número: ", end="")
        p = escaner_con_rango(rango)
    
    if p < 1 or p > rango:
        print("Este número está fuera del rango")
        print("Introduzca otro número: ", end="")
        p = escaner_con_rango(rango)
    
    return p

class Main(Identidad):
    @staticmethod
    def main():
        # Deserializador.deserializar_listas()
        Main.escoger_funcionalidad()

    @staticmethod
    def escoger_funcionalidad():
        while True:
            numeros = [1, 2, 3, 4, 5, 6]
            boleano = False
            
            lineas()
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
            lineas()
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
                    funcionalidad1.consultas_eco()
                case 2:
                    cliente = Identidad.identificar_persona()
                    funcionalidad2.elegir_tipo_busqueda(cliente)
                case 3:
                    funcionalidad3.impresion_facturas()
                case 4:
                    funcionalidad4.seleccion_tienda()
                case 5:
                    admin = Identidad.identificar_persona()
                    funcionalidad5.personalizar_tienda(admin)
                case 6:
                    # Serializador.serializar_todo()
                    print("Ha salido del programa")
                    sys.exit(0)

if __name__ == "__main__":
    Main.main()
