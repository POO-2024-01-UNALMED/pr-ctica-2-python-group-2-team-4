

class Funcionalidad5:

    @classmethod
    def personalizar_tienda(cls,admin):
        from uiMain.main import Main
        from gestorAplicacion.servicios.tienda import Tienda
        Main.lineas()
        print("Ha seleccionado Personalizar y modificar tiendas.")
        print("Selecciona una de las tiendas disponibles para ti:")

        print("+-----------------------------------+----------+")
        print("| No.|     Nombre de Tienda         |  Precio  |")
        print("+-----------------------------------+----------+")

        tiendas = Tienda.get_tiendas()

        for i in range(0,1,len(tiendas) - 1):
            if tiendas[i].get_dueno() is not None or tiendas[i].get_estado() == "cerrado":
                tiendas.pop(i)

        for i, tienda in enumerate(tiendas):
            nombre_tienda = tienda.get_nombre()
            precio_tienda = f"${tienda.get_saldo():,.2f}"
            print(f"| {i+1:2d} | {nombre_tienda:<28} | {precio_tienda:>8} |")

        print("+----+------------------------------+----------+")
        eleccion = Main.escaner()-1
        tien = tiendas[eleccion]

        diferencia = admin.get_dinero() - tien.get_saldo()
        if diferencia >= 0:
            tien.set_dueno(admin)
            admin.get_tiendas().append(tien)
            print(f"Has seleccionado la tienda: {tien.get_nombre()}")
            print(f"Se te restó ${tien.get_saldo():.2f} de tu saldo")
            print(f"Ahora eres el dueño de la tienda: \"{tien.get_nombre()}\"")
            admin.set_dinero(diferencia)
            print(f"Tu saldo ahora es de: ${diferencia:.2f}")

        iterar = True
        while iterar:
            Main.lineas()
            print("1. ¿Desea reorganizar pasillos?")
            print("2. ¿Desea llamar al proveedor?")
            print("3. ¿Desea contratar empleados?")
            print("4. Salir de personalizar tienda")
            decision = Main.escaner_con_rango(4)
            if decision == 1:
                cls.reorganizar_pasillos(tien)
            elif decision == 2:
                cls.llamar_proveedor(tien, admin)
            elif decision == 3:
                cls.contratar(tien)
            elif decision == 4:
                iterar = False
                print("Ha salido de personalizar tienda")
            else:
                print("Ese número está fuera del rango")
                print("Introduzca otro número: ")

    @staticmethod
    def reorganizar_pasillos(tien):
        from gestorAplicacion.servicios.enums import Categoria
        from uiMain.main import Main
        tien.get_pasillos().clear()
        Main.lineas()
        i = 1
        while True:
            Main.lineas()
            print(f"¿Qué categorías tendrá el pasillo {i}?")
            for n, categoria in enumerate(list(Categoria), 1):
                print(f"{n}. {categoria}")
            x2 = Main.escaner()
            Main.lineas()
            print(f"Nombre del pasillo número {i}:")
            nom = input()
            tien.anadir_pasillo(x2, nom)
            print("Pasillo añadido")
            Main.lineas()
            print(tien.mostrar_pasillos())
            i += 1
            Main.lineas()
            print("1. Continuar\n2. Terminar")
            x3 = Main.escaner_con_rango(2)
            if x3 != 1:
                break

    @staticmethod
    def llamar_proveedor(tien, admin):
        from uiMain.main import Main
        from gestorAplicacion.servicios.proveedor import Proveedor
        Main.lineas()
        if not tien.disponibilidad_productos():
            print(f"{tien.get_dueno().get_nombre()} de la tienda: \"{tien.get_nombre()}\", algunos pasillos están vacíos")
            print("He aquí nuestros proveedores:")
            print(Proveedor.listar_proveedores())
            k = Main.escaner_con_rango(6)
            Main.lineas()
            prov = Proveedor.get_seis_proveedores()[k-1]
            entrega = prov.get_entrega()
            s = ""
            for p in entrega:
                iter =True
                while iter:
                    diferencia = tien.get_saldo() - p.get_precio()
                    if diferencia >= 0:
                        tien.set_saldo(diferencia)
                        tien.agregar_producto(p)
                        print("Producto agregado")
                    elif admin.get_dinero() > 0:
                        print("La tienda no tiene suficiente saldo")
                        print("¿Desea transferir su dinero a su tienda?\n1. Sí\n2. No")
                        l = Main.escaner_con_rango(2)
                        if l == 1:
                            tien.set_saldo(admin.get_dinero())
                            admin.set_dinero(0)
                        elif l == 2:
                            print("Se terminó el pedido al proveedor")
                        else:
                            print("Entrada inválida")
                    else:
                        s = "Dinero insuficiente\nTerminando pedido"
                        break
            print(s)

    @staticmethod
    def contratar(tien):
        from gestorAplicacion.servicios.tienda import Tienda
        from uiMain.main import Main
        Main.lineas()
        j = 1
        iterar = True
        while iterar:
            Main.lineas()
            print("Estos son los candidatos:")
            print(Tienda.mostrar_desempleados())
            Main.lineas()
            print(f"¿Qué tipo de empleado necesita que sea el empleado número {j}?")
            ems = ["Domiciliario", "Concerje", "Cajero"]
            for n, e in enumerate(ems, 1):
                print(f"{n}. {e}")
            x5 = Main.escaner_con_rango(3)
            tien.contratar_empleados(x5)
            print(tien.mostrar_empleados())
            j += 1
            i = True
            while i:
                Main.lineas()
                print("1. Continuar\n2. Terminar")
                x6 = Main.escaner_con_rango(2)
                if x6 == 1:
                    i = False
                elif x6 == 2:
                    i = False
                    iterar = False
                else:
                    print("Entrada inválida")