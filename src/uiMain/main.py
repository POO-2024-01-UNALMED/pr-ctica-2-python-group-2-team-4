import sys

import json
from gestorAplicacion.servicios.caja import Caja
from gestorAplicacion.servicios.enums import Genero, TipoCaja
from gestorAplicacion.servicios.tienda import Tienda
from gestorAplicacion.sujetos.administrador import Administrador
from gestorAplicacion.sujetos.cajero import Cajero
from uiMain.identidad import Identidad

admin1 = Administrador("Beatriz Gómez", 201, 40, Genero.M, 12000.0)
admin2 = Administrador("Ricardo Díaz", 202, 45, Genero.H, 15000.0)
admin3 = Administrador("Sofía Sánchez", 203, 38, Genero.M, 11000.0)
admin4 = Administrador("Miguel Ramírez", 204, 50, Genero.H, 16000.0)

print(admin1.__dict__)
print(json.dumps(admin1.__dict__))
with open("baseDatos/temp/administradores.json","w") as write:
    json.dump(admin1.__dict__,write)
data=open("administradores.json",)
print(json.load(data))

# Crear tiendas
tienda9 = Tienda("1234567890", admin1, "Tienda Digital", 25000.0, "abierto")
tienda10 = Tienda("0987654321", admin2, "Tienda Elegante", 30000.0, "cerrado")
tienda11 = Tienda("1122334455", admin3, "Tienda Económica", 18000.0, "abierto")
tienda12 = Tienda("5544332211", admin4, "Tienda Familiar", 22000.0, "cerrado")
tienda13 = Tienda("6677889900", None, "Tienda Retro", 27000.0, "abierto")
tienda14 = Tienda("8899001122", None, "Tienda Gourmet", 35000.0, "abierto")
tienda15 = Tienda("2233445566", None, "Tienda de Lujo", 40000.0, "cerrado")
tienda16 = Tienda("5566778899", None, "Tienda Outlet", 15000.0, "abierto")

# Crear cajas
caja1 = Caja("Caja 1", TipoCaja.RAPIDA, tienda9)
caja2 = Caja("Caja 2", TipoCaja.NORMAL, tienda9)
caja3 = Caja("Caja 3", TipoCaja.RAPIDA, tienda10)
caja4 = Caja("Caja 4", TipoCaja.NORMAL, tienda10)
caja5 = Caja("Caja 5", TipoCaja.RAPIDA, tienda11)
caja6 = Caja("Caja 6", TipoCaja.RAPIDA, tienda12)
caja7 = Caja("Caja 7", TipoCaja.NORMAL, tienda12)
caja8 = Caja("Caja 8", TipoCaja.RAPIDA, tienda13)
caja9 = Caja("Caja 9", TipoCaja.NORMAL, tienda13)
caja10 = Caja("Caja 10", TipoCaja.RAPIDA, tienda14)
caja11 = Caja("Caja 11", TipoCaja.NORMAL, tienda14)
caja12 = Caja("Caja 12", TipoCaja.RAPIDA, tienda15)
caja13 = Caja("Caja 13", TipoCaja.NORMAL, tienda15)
caja14 = Caja("Caja 14", TipoCaja.RAPIDA, tienda16)
caja15 = Caja("Caja 15", TipoCaja.NORMAL, tienda16)

# Crear cajeros
cajero1 = Cajero("Miguel Ángel", 301, 28, Genero.H, 8000.0, tienda9, True, False, 5, caja1)
cajero2 = Cajero("Paola Ruiz", 302, 32, Genero.M, 8500.0, tienda9, True, False, 3, caja2)
cajero3 = Cajero("Luis Gómez", 303, 26, Genero.H, 7800.0, tienda10, True, False, 2, caja3)
cajero4 = Cajero("Elena Martínez", 304, 29, Genero.M, 8200.0, tienda10, True, False, 4, caja4)
cajero5 = Cajero("Javier Fernández", 305, 35, Genero.H, 8300.0, tienda11, True, False, 6, caja5)
cajero6 = Cajero("Sofía Sánchez", 306, 30, Genero.M, 8600.0, tienda12, True, False, 5, caja6)
cajero7 = Cajero("Andrés Vargas", 307, 33, Genero.H, 8800.0, tienda12, True, False, 3, caja7)
cajero8 = Cajero("Camila Ramírez", 308, 27, Genero.M, 7900.0, tienda13, True, False, 2, caja8)
cajero9 = Cajero("Roberto Mendoza", 309, 31, Genero.H, 8200.0, tienda13, True, False, 4, caja9)
cajero10 = Cajero("Isabel Fernández", 310, 29, Genero.M, 8400.0, tienda14, True, False, 6, caja10)
cajero11 = Cajero("Felipe Torres", 311, 34, Genero.H, 8700.0, tienda14, True, False, 7, caja11)
cajero12 = Cajero("Laura Jiménez", 312, 28, Genero.M, 8000.0, tienda15, True, False, 3, caja12)
cajero13 = Cajero("David López", 313, 36, Genero.H, 8300.0, tienda15, True, False, 5, caja13)
cajero14 = Cajero("Natalia Morales", 314, 25, Genero.M, 7800.0, tienda16, True, False, 4, caja14)
cajero15 = Cajero("Antonio Salazar", 315, 32, Genero.H, 8500.0, tienda16, True, False, 6, caja15)
class Main(Identidad):
    def __init__(self):
        super().__init__()

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

    def escoger_funcionalidad(self):
        from uiMain.funcionalidad1 import Funcionalidad1
        from uiMain.funcionalidad2 import Funcionalidad2
        from uiMain.funcionalidad3 import Funcionalidad3
        from uiMain.funcionalidad4 import Funcionalidad4
        from uiMain.funcionalidad5 import Funcionalidad5
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
                    cliente = self.identificar_persona()
                    Funcionalidad2.elegir_tipo_busqueda(cliente)
                case 3:
                    Funcionalidad3.impresion_facturas()
                case 4:
                    Funcionalidad4.seleccion_tienda()
                case 5:
                    admin = self.identificar_persona()
                    Funcionalidad5.personalizar_tienda(admin)
                case 6:
                    # Serializador.serializar_todo()
                    print("Ha salido del programa")
                    sys.exit(0)

if __name__ == "__main__":
    main=Main()
    main.escoger_funcionalidad()
