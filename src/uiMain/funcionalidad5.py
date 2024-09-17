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
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Crear un FieldFrame con el título y descripción correspondiente
        zona2Fun1 = FieldFrame(window, "", [None], "", [],
                               [None], "Personalización de tiendas",
                               "La Funcionalidad 5, permite a los usuarios realizar compras de múltiples tiendas. El sistema filtra tiendas según su estado de actividad, permite reorganizar pasillos, contratar empleados y llamar al proveedor."
                               , False, 25, 15, "#243340", "white", "black", "#F2F2F2", 0, 800)

        # Crear un Frame para los botones y añadirlo al `FieldFrame`
        boton_frame = Frame(zona2Fun1.campos, bg="#F2F2F2")
        boton_frame.grid(row=0, column=1, columnspan=2, pady=20, padx=10, sticky='nsew')

        # Configurar las columnas y filas del `boton_frame` para que se expandan
        boton_frame.columnconfigure(0, weight=1)
        boton_frame.rowconfigure(0, weight=1)
        boton_frame.rowconfigure(1, weight=1)
        boton_frame.rowconfigure(2, weight=1)
        boton_frame.rowconfigure(3, weight=1)

        # Texto Opciones
        texto_label = Label(boton_frame, text="Ha seleccionado Ecosistema de Consultas Personalizadas",
                            font=("Arial", 20), bg="#F2F2F2")
        texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

        # Botón 1: Consulta general de productos
        boton1 = Button(boton_frame, text="Llamar Proveedor",
                        font=("Arial", 15) )
        boton1.grid(row=1, column=0, sticky='ew', padx=50, pady=10)

        # Botón 2: Consulta de productos por categoría
        boton2 = Button(boton_frame, text="Reorganizar Pasillos",
                        font=("Arial", 15))
        boton2.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

        # Botón 3: Consulta de membresías
        boton3 = Button(boton_frame, text="Contratar Empleados",
                        font=("Arial", 15))
        boton3.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
        zona2Fun1.campos.columnconfigure(1, weight=1)
        zona2Fun1.campos.rowconfigure(1, weight=1)

        # Mostrar el frame con los botones
        zona2Fun1.pack(fill=BOTH, expand=True)

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
