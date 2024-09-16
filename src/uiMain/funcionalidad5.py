from uiMain.fieldFrame import FieldFrame
from gestorAplicacion.sujetos.administrador import Administrador
from tkinter import*
class Funcionalidad5:
    @classmethod
    def ingresar(self, window):
        # Limpiar los widgets de la ventana
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Proceso de identificación del usuario
        def ingresa():
            from uiMain.identidad import Identidad2
            identidad = Identidad2(window)
            identidad.identificar_persona()

            # Usamos un after para esperar y verificar hasta que identidad.resultado esté definido
            def check_identificacion():
                if identidad.resultado is not None:
                    usuario = identidad.resultado
                    # Llama al frame de usuario solo si el usuario ha sido identificado
                    self.personalizar_tienda(usuario,window)
                else:
                    # Si aún no se ha identificado, verificar de nuevo
                    window.after(100, check_identificacion)

            # Iniciar la espera para que el resultado se procese
            window.after(100, check_identificacion)

        ingresa()
    @classmethod
    def personalizar_tienda(cls, admin,window):
        from gestorAplicacion.servicios.tienda import Tienda
        tiendas = Tienda.get_tiendas()

        # Corregido: bucle invertido y pop durante la iteración
        for i in reversed(range(len(tiendas))):
            if tiendas[i].get_dueno() is not None or tiendas[i].get_estado() == "cerrado":
                tiendas.pop(i)
        criterios = ["tienda"]
        valores = [""]
        habilitado = [True]
        func5=FieldFrame(
            master=window,
            tituloCriterios="tiendas",
            criterios=criterios,
            tituloValores="Valores",
            valores=valores,
            habilitado=habilitado,
            titulo="Personalizar Tienda",
            descripcion="Para adaptar tu tienda a tu diseño"
            )
        func5.pack(fill="both", expand=True)
        from gestorAplicacion.servicios.tienda import Tienda
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Crear el marco para las Tiendas
        tiendasGeneral_frame = Frame(window, bg="#243340")
        tiendasGeneral_frame.pack(pady=10, fill=BOTH, expand=True)

        # Crear el marco para las Tiendas
        tiendas_frame = Frame(tiendasGeneral_frame, bg="#243340")
        tiendas_frame.pack(pady=10, fill=BOTH, expand=True)

        tiendas = Tienda.revision_tienda(Tienda.get_tiendas())
        Label(tiendas_frame, text="Selecciona una de las tiendas que tenemos disponibles para ti:",font=("Arial", 16), bg="#F2F2F2", fg="black").pack(pady=10)
            # Crear un marco adicional para centrar los botones
        botones_frame = Frame(tiendas_frame, bg="#243340")
        botones_frame.pack(padx=100, pady=20, fill=BOTH, expand=True)

            # Mostrar las tiendas en la página actual
            #indice = 1 + (page - 1) * tiendas_por_pagina

            # Controles de paginación
        paginacion_frame = Frame(tiendas_frame, bg="#243340")
        paginacion_frame.pack(pady=10)
        if Tienda.get_tiendas()==0:
            Label(tiendas_frame,
                  text="No hay tiendas disponibles en el momento.",
                  font=("Arial", 44), bg="#F2F2F2").pack(pady=10)
        eleccion=0
        

        # Validación de entrada del usuario
        if eleccion < 0 or eleccion >= len(tiendas):
            print("Selección inválida. Por favor, intenta de nuevo.")
            return

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
        else:
            print("No tienes suficiente dinero para comprar esta tienda.")
            return

        iterar = True
        while iterar:
            print("1. ¿Desea reorganizar pasillos?")
            print("2. ¿Desea llamar al proveedor?")
            print("3. ¿Desea contratar empleados?")
            print("4. Salir de personalizar tienda")
            #decision = Main.escaner_con_rango(4)
            decision = 1
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
                iter = True
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
                            iter = False
                        else:
                            print("Entrada inválida")
                    else:
                        s = "Dinero insuficiente\nTerminando pedido"
                        iter = False
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
            ems = ["Domiciliario", "Conserje", "Cajero"]  # Corregido "Conserje"
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
