import sys

import pickle
from gestorAplicacion.sujetos.administrador import Administrador
from uiMain.identidad import Identidad

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

    @classmethod
    def escoger_funcionalidad(cls):
        from uiMain.funcionalidad1 import Funcionalidad1
        from uiMain.funcionalidad2 import Funcionalidad2
        from uiMain.funcionalidad3 import Funcionalidad3
        from uiMain.funcionalidad4 import Funcionalidad4
        from uiMain.funcionalidad5 import Funcionalidad5
        while True:
            numeros = [1, 2, 3, 4, 5, 6,7]
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
                    cliente = Main.identificar_persona()
                    funcionalidad2obj=Funcionalidad2()
                    funcionalidad2obj.elegir_tipo_busqueda(cliente)
                case 3:
                    persona = Main.identificar_persona()
                    Funcionalidad3.impresion_facturas(persona)
                case 4:
                    Funcionalidad4.seleccion_tienda()
                case 5:
                    admin = cls.identificar_persona()
                    Funcionalidad5.personalizar_tienda(admin)
                case 6:
                    EscritorLector.serializarTodo()
                    print("Ha salido del programa")
                    sys.exit(0)
                case 7:
                    from gestorAplicacion.servicios.enums import Edades
                    from gestorAplicacion.servicios.carrito import Carrito
                    carrito7 = Carrito(None, False, Edades.ADULTOS)
                    cliente1.set_carrito(carrito7)
                    carrito7.set_cliente(cliente1)
                    carrito7.set_tienda(cliente1.get_tienda())
                    cliente1.set_tienda(tienda)
                    Main.escoger_funcionalidad()


if __name__ == "__main__":
    from gestorAplicacion.sujetos.cajero import Cajero
    from gestorAplicacion.sujetos.cliente import Cliente
    from gestorAplicacion.servicios.producto import Producto
    from gestorAplicacion.servicios.caja import Caja
    from gestorAplicacion.servicios.carrito import Carrito
    from gestorAplicacion.servicios.enums import Genero, TipoCaja, Edades, Tamano, Categoria
    from gestorAplicacion.servicios.pasillo import Pasillo
    from gestorAplicacion.servicios.tienda import Tienda
    from baseDatos.escritorLector import EscritorLector
    main=Main()
    EscritorLector.deserializarTodo()

    """  admin1 = Administrador("Beatriz Gómez", 201, 40, Genero.M, 12000.0)
    admin2 = Administrador("Ricardo Díaz", 202, 45, Genero.H, 15000.0)
    admin3 = Administrador("Sofía Sánchez", 203, 38, Genero.M, 11000.0)
    admin4 = Administrador("Miguel Ramírez", 204, 50, Genero.H, 16000.0)

    #print(admin1.__dict__)

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
    cajero15 = Cajero("Antonio Salazar", 315, 32, Genero.H, 8500.0, tienda16, True, False, 6, caja15)"""

    producto1 = Producto(
    "Leche Entera", "La Vaquita", 1.50, Tamano.GRANDE, Edades.MENORES, Categoria.ALIMENTO,
    "Leche entera de vaca, fortificada con vitaminas A y D.", "15/10/2024", 101
    )

    producto2 = Producto(
    "Pan Integral", "PanRico", 2.00, Tamano.MEDIANO, Edades.MENORES, Categoria.ALIMENTO,
    "Pan integral alto en fibra, ideal para una dieta saludable.", "22/08/2024", 102
    )

    producto3 = Producto(
    "Yogur Natural", "BioLácteos", 3.25, Tamano.MEDIANO, Edades.ADULTOS, Categoria.ALIMENTO,
    "Yogur natural sin azúcar añadido, fuente de probióticos.", "10/09/2024", 103
    )

    producto4 = Producto(
    "Queso Cheddar", "La Gran Quesería", 4.50, Tamano.MEDIANO, Edades.ADULTOS, Categoria.ALIMENTO,
    "Queso cheddar madurado, ideal para sandwiches y gratinados.", "30/09/2024", 104
    )

    producto5 = Producto(
    "Galletas de Avena", "Cerealia", 2.75, Tamano.PEQUENO, Edades.MENORES, Categoria.ALIMENTO,
    "Galletas de avena y miel, perfectas para un snack saludable.", "05/11/2024", 105
    )

    producto6 = Producto(
    "Jugo de Manzana", "Frutas del Valle", 2.50, Tamano.MEDIANO, Edades.MENORES, Categoria.BEBIDA,
    "Jugo de manzana natural, sin azúcares añadidos.", "01/12/2024", 106
    )

    producto7 = Producto(
    "Agua Mineral", "Pureza Total", 1.00, Tamano.GRANDE, Edades.MENORES, Categoria.BEBIDA,
    "Agua mineral natural, embotellada en origen.", "15/11/2024", 107
    )

    producto8 = Producto(
    "Refresco de Cola", "SodaFresca", 1.75, Tamano.MEDIANO, Edades.ADULTOS, Categoria.BEBIDA,
    "Refresco de cola con gas, sabor intenso y refrescante.", "20/11/2024", 108
    )

    producto9 = Producto(
    "Bebida Energética", "PowerUp", 3.00, Tamano.PEQUENO, Edades.ADULTOS, Categoria.BEBIDA,
    "Bebida energética con vitaminas y cafeína para un impulso rápido.", "10/12/2024", 109
    )

    producto10 = Producto(
    "Té Helado", "TeaTime", 2.00, Tamano.MEDIANO, Edades.MENORES, Categoria.BEBIDA,
    "Té helado con sabor a limón, refrescante y sin calorías.", "30/12/2024", 110
    )

    producto11 = Producto(
    "Desodorante Aerosol", "FreshUp", 2.50, Tamano.MEDIANO, Edades.ADULTOS, Categoria.PERSONAL,
    "Desodorante en aerosol con fragancia duradera y protección antitranspirante.", "01/01/2025", 111
    )

    producto12 = Producto(
    "Crema Dental", "WhiteSmile", 1.80, Tamano.PEQUENO, Edades.MENORES, Categoria.PERSONAL,
    "Crema dental con flúor, para una limpieza completa y protección contra caries.", "15/02/2025", 112
    )

    producto13 = Producto(
    "Jabón Líquido", "CleanTouch", 2.00, Tamano.MEDIANO, Edades.ADULTOS, Categoria.PERSONAL,
    "Jabón líquido para manos con ingredientes naturales y fragancia fresca.", "10/03/2025", 113
    )

    producto14 = Producto(
    "Acondicionador Hidratante", "HydraSoft", 3.50, Tamano.MEDIANO, Edades.ADULTOS, Categoria.PERSONAL,
    "Acondicionador hidratante para cabello seco, con extracto de coco.", "25/04/2025", 114
    )

    producto15 = Producto(
    "Gel Antibacterial", "SafeHands", 1.50, Tamano.PEQUENO, Edades.MENORES, Categoria.PERSONAL,
    "Gel antibacteriano para manos, con un 70% de alcohol y fragancia ligera.", "05/05/2025", 115
    )

    producto16 = Producto(
    "Detergente en Polvo", "LimpiaFacil", 4.00, Tamano.GRANDE, Edades.ADULTOS, Categoria.LIMPIEZA,
    "Detergente en polvo para ropa, eficaz en manchas difíciles.", "01/06/2025", 116
    )

    producto17 = Producto(
    "Limpiador Multiusos", "Sparkle", 3.50, Tamano.MEDIANO, Edades.ADULTOS, Categoria.LIMPIEZA,
    "Limpiador multiusos para superficies, con fragancia cítrica.", "15/07/2025", 117
    )

    producto18 = Producto(
    "Desinfectante de Baño", "Sanitex", 2.75, Tamano.PEQUENO, Edades.ADULTOS, Categoria.LIMPIEZA,
    "Desinfectante para baño, elimina bacterias y malos olores.", "30/08/2025", 118
    )

    producto19 = Producto(
    "Esponjas de Cocina", "ScrubPlus", 1.50, Tamano.PEQUENO, Edades.MENORES, Categoria.LIMPIEZA,
    "Esponjas de cocina, resistentes y eficaces para limpiar utensilios.", "10/09/2025", 119
    )

    producto20 = Producto(
    "Toallas de Papel", "CleanTowel", 2.00, Tamano.MEDIANO, Edades.MENORES, Categoria.LIMPIEZA,
    "Toallas de papel absorbentes, ideales para la limpieza de superficies.", "25/10/2025", 120
    )

    pasilloBebidas = Pasillo(
    "Pasillo de Bebidas",
    [producto6, producto7, producto8, producto9, producto10],
    Categoria.BEBIDA,
    None
    )

    pasilloPersonal = Pasillo(
    "Pasillo de Personal",
    [producto11, producto12, producto13, producto14, producto15],
    Categoria.PERSONAL,
    None
    )

    pasilloLimpieza = Pasillo(
    "Pasillo de Limpieza",
    [producto16, producto17, producto18, producto19, producto20],
    Categoria.LIMPIEZA,
    None
    )

    producto6.set_pasillo(pasilloBebidas)
    producto7.set_pasillo(pasilloBebidas)
    producto8.set_pasillo(pasilloBebidas)
    producto9.set_pasillo(pasilloBebidas)
    producto10.set_pasillo(pasilloBebidas)

    producto11.set_pasillo(pasilloPersonal)
    producto12.set_pasillo(pasilloPersonal)
    producto13.set_pasillo(pasilloPersonal)
    producto14.set_pasillo(pasilloPersonal)
    producto15.set_pasillo(pasilloPersonal)

    producto16.set_pasillo(pasilloLimpieza)
    producto17.set_pasillo(pasilloLimpieza)
    producto18.set_pasillo(pasilloLimpieza)
    producto19.set_pasillo(pasilloLimpieza)
    producto20.set_pasillo(pasilloLimpieza)

    cliente2 = Cliente("Ana", 22002, 25, Genero.M, 60000, None)
    cliente3 = Cliente("Luis", 33003, 35, Genero.H, 70000, None)
    cliente4 = Cliente("Maria", 44004, 28, Genero.M, 80000, None)
    cliente5 = Cliente("Jorge", 55005, 40, Genero.H, 90000, None)

    caja1 = Caja("Caja Principal", TipoCaja.NORMAL, None)
    caja2 = Caja("Caja 2", TipoCaja.RAPIDA, None)
    caja3 = Caja("Caja Express", TipoCaja.RAPIDA, None)
    caja4 = Caja("Caja 4", TipoCaja.NORMAL, None)
    caja5 = Caja("Caja VIP", TipoCaja.RAPIDA, None)

    cajero1 = Cajero("Javier", 4040, 25, Genero.H, 30000, None, True, False, 5, None)
    cajero2 = Cajero("Elena", 5050, 26, Genero.M, 28000, None, False, True, 6, None)
    cajero3 = Cajero("Fernando", 6060, 24, Genero.H, 29000, None, True, True, 4, None)
    cajero4 = Cajero("Sofía", 7070, 27, Genero.M, 31000, None, True, False, 7, None)
    cajero5 = Cajero("Miguel", 8080, 28, Genero.H, 32000, None, False, True, 8, None)

    cajero1.caja = caja1
    cajero2.caja = caja2
    cajero3.caja = caja3
    cajero4.caja = caja4
    cajero5.caja = caja5

    caja1.set_cajero(cajero1)
    caja2.set_cajero(cajero2)
    caja3.set_cajero(cajero3)
    caja4.set_cajero(cajero4)
    caja5.set_cajero(cajero5)

    tienda = Tienda("Tienda Principal", [pasilloBebidas, pasilloPersonal, pasilloLimpieza])

    tienda.set_cajas([caja1, caja2, caja3, caja4, caja5])

    for c in [caja1, caja2, caja3, caja4, caja5]:
        c.set_tienda(tienda)
    admin=Administrador("pp",23)
    tienda34 = Tienda("Tienda Principal", [pasilloBebidas, pasilloPersonal, pasilloLimpieza],None,admin,0,"abierto")

    cliente1 = Cliente("Carlos", 11001, 30, Genero.H, 50000, None, tienda)
    #carrito1 = Carrito(cliente1, False, Edades.MENORES, tienda)
    #carrito2 = Carrito(cliente2, True, Edades.ADULTOS, tienda)
    #carrito3 = Carrito(cliente3, False, Edades.ADULTOS, tienda)
    #carrito4 = Carrito(cliente4, True, Edades.MENORES, tienda)
    #carrito5 = Carrito(cliente5, False, Edades.MENORES, tienda)
    carrito6=Carrito(None,False,Edades.ADULTOS)
    cliente1.set_carrito(carrito6)
    carrito6.set_cliente(cliente1)
    carrito6.set_tienda(cliente1.get_tienda())

    producto16.set_tienda(pasilloLimpieza.get_tienda())
    producto17.set_tienda(pasilloLimpieza.get_tienda())
    producto18.set_tienda(pasilloLimpieza.get_tienda())
    producto19.set_tienda(pasilloLimpieza.get_tienda())
    producto20.set_tienda(pasilloLimpieza.get_tienda())

    producto11.set_tienda(pasilloPersonal.get_tienda())
    producto12.set_tienda(pasilloPersonal.get_tienda())
    producto13.set_tienda(pasilloPersonal.get_tienda())
    producto14.set_tienda(pasilloPersonal.get_tienda())
    producto15.set_tienda(pasilloPersonal.get_tienda())

    producto6.set_tienda(pasilloBebidas.get_tienda())
    producto7.set_tienda(pasilloBebidas.get_tienda())
    producto8.set_tienda(pasilloBebidas.get_tienda())
    producto9.set_tienda(pasilloBebidas.get_tienda())
    producto10.set_tienda(pasilloBebidas.get_tienda())
    main.escoger_funcionalidad()
    
