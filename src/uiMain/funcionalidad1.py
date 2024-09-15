import math
from tkinter import *
from tkinter import messagebox, simpledialog

from gestorAplicacion.servicios.tienda import Tienda
from uiMain.fieldFrame import FieldFrame


class Funcionalidad1:
    def __init__(self):
        pass

    cliente = None

    def consultasEco(self, cliente, window):
        from gestorAplicacion.servicios.tienda import Tienda
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Crear un FieldFrame con el título y descripción correspondiente
        zona2Fun1 = FieldFrame(window, "", [None], "", [],
                               [None], "Sistema de Consultas Personalizadas",
                               "La Funcionalidad 1, permite a los usuarios realizar búsquedas de tiendas y productos en una tienda simulada, ya sea de manera general o por categoría. El sistema filtra tiendas según la disponibilidad de productos y trabajadores, y ajusta el acceso y presupuesto del usuario según su edad. Además, gestiona las membresías, permitiendo actualizar o adquirir una nueva, ofreciendo beneficios adicionales según la categoría de membresía (Básico, Premium, VIP)."
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
        boton1 = Button(boton_frame, text="Consulta general de productos",
                        font=("Arial", 15), command=lambda: self.consulta_general_productos(cliente, window))
        boton1.grid(row=1, column=0, sticky='ew', padx=50, pady=10)

        # Botón 2: Consulta de productos por categoría
        boton2 = Button(boton_frame, text="Consulta de productos por categoría",
                        font=("Arial", 15),command=print(Tienda.buscar_tienda()))
        boton2.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

        # Botón 3: Consulta de membresías
        boton3 = Button(boton_frame, text="Consulta de membresías",
                        font=("Arial", 15))
        boton3.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

        # Botón 4: Volver al menú principal
        boton4 = Button(boton_frame, text="Volver", font=("Arial", 15))
        boton4.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
        zona2Fun1.campos.columnconfigure(1, weight=1)
        zona2Fun1.campos.rowconfigure(1, weight=1)

        # Mostrar el frame con los botones
        zona2Fun1.pack(fill=BOTH, expand=True)

    def consulta_general_productos(self, cliente, window):
        from gestorAplicacion.sujetos.cliente import Cliente
        from uiMain.main import Main
        from gestorAplicacion.servicios.tienda import Tienda
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Crear el marco para las Tiendas
        tiendasGeneral_frame = Frame(window, bg="#243340")
        tiendasGeneral_frame.pack(pady=10, fill=BOTH, expand=True)

        # Crear el marco para las Tiendas
        tiendas_frame = Frame(tiendasGeneral_frame, bg="light blue")
        tiendas_frame.pack(pady=10, fill=BOTH, expand=True)

        if Tienda.buscar_tienda():
            tiendas = Tienda.revision_tienda(Tienda.get_tiendas())
            Label(tiendas_frame, text="Selecciona una de las tiendas que tenemos disponibles para ti:",
                  font=("Arial", 16), bg="#F2F2F2", fg="black").pack(pady=10)




            # Crear un marco adicional para centrar los botones
            botones_frame = Frame(tiendas_frame, bg="#F2F2F2")
            botones_frame.pack(pady=10, fill=BOTH, expand=True)

            indice = 1

            for tienda in tiendas:
                Button(botones_frame, text=f"{indice}. {tienda.get_nombre()}",
                       font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                       width=35,
                       #   command=lambda cat=tipo: self.mostrar_productos_por_categoria(cliente, cat, window)
                       ).pack(
                    pady=5, anchor=CENTER)
                indice += 1

                # Añadir la opción de buscar por nombre
                Button(botones_frame, text=f"{indice}. Volver",
                       font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                       width=35, command=lambda: self.consultasEco(cliente, window)).pack(pady=5, anchor=CENTER)



"""
    @classmethod
    def consultas_eco(cls):
        from uiMain.identidad import Identidad
        from gestorAplicacion.sujetos.cliente import Cliente
        from gestorAplicacion.sujetos.administrador import Administrador
        from uiMain.main import Main
        cliente = None

        while cliente is None:
            persona = Identidad.identificar_persona()

            if isinstance(persona, Cliente):
                cliente = persona
            elif isinstance(persona, Administrador):
                print("Error: Se identificó un administrador. Por favor, ingrese un número de cliente válido.")
            else:
                print("Error: Tipo de persona no reconocido. Por favor, ingrese un número de cliente válido.")

        Main.lineas()
        print("Ha seleccionado Ecosistema de Consultas Personalizadas. Elija una opción:")
        print("1. Consulta general de productos")
        print("2. Consulta de productos por categoría")
        print("3. Consulta de membresías")
        print("4. Volver")
        print("")
        consulta = Main.escaner_con_rango(4)

        print(f"Opción seleccionada: {consulta}")

        if consulta == 1:
            Funcionalidad1.consulta_general_productos(cliente)
        elif consulta == 2:
            Funcionalidad1.consulta_por_categoria(cliente)
        elif consulta == 3:
            Funcionalidad1.consulta_membresias(cliente)
        elif consulta == 4:
            Main.escoger_funcionalidad()
        else:
            print("Opción no válida")

    @staticmethod
    def consulta_general_productos(cliente):
        from gestorAplicacion.sujetos.cliente import Cliente
        from uiMain.main import Main
        from gestorAplicacion.servicios.tienda import Tienda
        if Tienda.buscar_tienda():
            print("Selecciona una de las tiendas que tenemos disponibles para ti")
            tiendas = Tienda.revision_tienda(Tienda.get_tiendas())
            Main.print_tabla_tiendas(tiendas)
            print("Selecciona una tienda:")
            tienda_seleccionada = Main.escaner(len(tiendas) + 1)

            if tienda_seleccionada == len(tiendas) + 1:
                Funcionalidad1.consultas_eco()
            else:
                tienda = tiendas[tienda_seleccionada - 1]
                print("¿Deseas usar un presupuesto por defecto o ingresar uno personalizado?")
                print("1. Presupuesto por defecto")
                print("2. Presupuesto personalizado")

                opcion_presupuesto = Main.escaner(2)
                if opcion_presupuesto == 1:
                    Cliente.asignaciones(cliente, tienda)
                elif opcion_presupuesto == 2:
                    print("Ingresa la cantidad de dinero que deseas asignar:")
                    cantidad_personalizada = float(input())  # Se obtiene la cantidad de dinero del usuario
                    Cliente.asignaciones(cliente, tienda, cantidad_personalizada)

                print(f"Has seleccionado la tienda: {tienda.get_nombre()}")
                print("Esta servirá para escoger productos en la funcionalidad 2")
                print("1. Desea chismosear la descripción de productos en la tienda")
                print("2. Desea ir al menú principal para empezar a hacer sus compras")
                print("3. Volver a escoger tienda")
                print("")
                decision = Main.escaner(3)
                if decision == 1:
                    Funcionalidad1.seleccionar_producto(Funcionalidad1.lista_productos(tienda, cliente, None), cliente)
                elif decision == 2:
                    Main.escoger_funcionalidad()
                elif decision == 3:
                    Funcionalidad1.consultas_eco()

        else:
            print("Lo sentimos, no hay tiendas disponibles en este momento.")

    @staticmethod
    def consulta_por_categoria(cliente):
        from gestorAplicacion.sujetos.cliente import Cliente
        from uiMain.main import Main
        from gestorAplicacion.servicios.tienda import Tienda
        from gestorAplicacion.servicios.enums import Categoria
        if Tienda.buscar_tienda():
            print("Selecciona una de las categorías disponibles en nuestras tiendas:")
            Main.print_tabla_categorias()

            categoria_seleccionada = Main.escaner(len(Categoria))

            tiendas = Funcionalidad1.busqueda_categoria(categoria_seleccionada)
            if tiendas:
                Main.print_tabla_tiendas(tiendas)
                print("Selecciona una tienda:")
                tienda_seleccionada = Main.escaner(len(tiendas) + 1)

                if tienda_seleccionada == len(tiendas) + 1:
                    Funcionalidad1.consultas_eco()
                else:
                    tienda = tiendas[tienda_seleccionada - 1]
                    print("¿Deseas usar un presupuesto por defecto o ingresar uno personalizado?")
                    print("1. Presupuesto por defecto")
                    print("2. Presupuesto personalizado")

                    opcion_presupuesto = Main.escaner(2)
                    if opcion_presupuesto == 1:
                        Cliente.asignaciones(cliente, tienda)
                    elif opcion_presupuesto == 2:
                        print("Ingresa la cantidad de dinero que deseas asignar:")
                        cantidad_personalizada = float(input())
                        Cliente.asignaciones(cliente, tienda, cantidad_personalizada)

                    print(f"Has seleccionado la tienda: {tienda.get_nombre()}")
                    print("Esta servirá para escoger productos en la funcionalidad 2")
                    print("1. Desea chismosear la descripción de productos en la tienda")
                    print("2. Desea ir al menú principal para empezar a hacer sus compras")
                    print("3. Volver a escoger tienda")
                    print("")
                    decision = Main.escaner(3)
                    if decision == 1:
                        Funcionalidad1.seleccionar_producto(Funcionalidad1.lista_productos(tienda, cliente, Categoria(categoria_seleccionada - 1)), cliente)
                    elif decision == 2:
                        Main.escoger_funcionalidad()
                    elif decision == 3:
                        Funcionalidad1.consultas_eco()
            else:
                print("No hay tiendas disponibles para la categoría seleccionada.")
        else:
            print("Lo sentimos, no hay tiendas disponibles en este momento.")

    @staticmethod
    def consulta_membresias(cliente):
        from gestorAplicacion.servicios.enums import Membresia
        from gestorAplicacion.sujetos.cliente import Cliente
        from uiMain.main import Main
        from gestorAplicacion.servicios.tienda import Tienda
        if Tienda.buscar_tienda():
            if cliente.mayor_edad():
                if cliente.get_membresia():
                    perfil_demografico = Cliente.perfil_demografico(cliente)
                    beneficios = Cliente.get_mensaje_por_perfil(perfil_demografico, cliente.get_membresia())

                    print(f"Tu membresía actual es: {cliente.get_membresia()}")
                    print(f"Beneficios: {beneficios}")

                    if cliente.get_membresia() == Membresia.VIP:
                        print("¡Gracias por ser un cliente VIP! Disfruta de todos los beneficios exclusivos.")
                        print("Recuerda ir a revisar alguna tienda, esto servirá para escoger productos en la funcionalidad 2")
                        print("")
                        print("1. Desea ir al menú principal")
                        print("2. Volver al menú de consulta")
                        print("")
                        decision = Main.escaner(2)
                        if decision == 1:
                            Main.escoger_funcionalidad()
                        elif decision == 2:
                            Funcionalidad1.consultas_eco()

                    else:
                        print("¿Te gustaría mejorar tu membresía?")
                        print("1. Sí")
                        print("2. No")
                        print("")
                        decision = Main.escaner(2)
                        if decision == 1:
                            print("Puedes mejorar tu membresía a:")
                            nueva_membresia = Main.print_tabla_membresias(cliente)
                            costo_evolucion = Cliente.calcular_costo_evolucion(cliente.get_membresia(), nueva_membresia)
                            print(f"Esto costará {costo_evolucion} y tu saldo actual es {cliente.get_dinero()}")
                            print("1. Sí")
                            print("2. No")
                            print("")
                            decisionest = Main.escaner(2)
                            if decisionest == 1:
                                print(Cliente.evolucionar_membresia(cliente, nueva_membresia))
                                print("")
                                print("1. Desea ir al menú principal")
                                print("2. Volver al menú de consulta")
                                print("")
                                decisiones = Main.escaner(2)
                                if decisiones == 1:
                                    Main.escoger_funcionalidad()
                                elif decisiones == 2:
                                    Funcionalidad1.consultas_eco()
                            elif decisionest == 2:
                                Main.escoger_funcionalidad()
                        elif decision == 2:
                            Main.escoger_funcionalidad()
                else:
                    print("No tienes una membresía. ¿Te gustaría elegir una?")
                    Main.print_tabla_membresias()
                    print("")
                    print("Escoja un número:")
                    decision = Main.escaner(4)
                    if decision == 1:
                        Funcionalidad1.primera_membresia(cliente, Membresia.BASICO)
                    elif decision == 2:
                        Funcionalidad1.primera_membresia(cliente, Membresia.PREMIUM)
                    elif decision == 3:
                        Funcionalidad1.primera_membresia(cliente, Membresia.VIP)
                    elif decision == 4:
                        Funcionalidad1.consultas_eco()
            else:
                print("Lo sentimos, no puedes obtener una membresía ya que eres menor de edad.")
                print("")
                print("Recuerda ir a revisar alguna tienda, esto servirá para escoger productos en la funcionalidad 2")
                print("")
                print("1. Desea ir al menú principal")
                print("2. Volver al menú de consulta")
                print("")
                decision = Main.escaner(2)
                if decision == 1:
                    Main.escoger_funcionalidad()
                elif decision == 2:
                    Funcionalidad1.consultas_eco()
        else:
            print("Lo sentimos, no hay tiendas disponibles en este momento.")

    @staticmethod
    def primera_membresia(cliente, membresia):
        from gestorAplicacion.sujetos.cliente import Cliente
        from uiMain.main import Main
        if cliente.get_membresia() is None:
            cliente.set_membresia(membresia)
            Cliente.registrar_membresia(cliente, membresia)
            print(f"Has obtenido la membresía {membresia}. ¡Disfruta de los beneficios!")
            Main.escoger_funcionalidad()
        else:
            print("Ya tienes una membresía activa.")

    @staticmethod
    def lista_productos(tienda, cliente, categoria):
        # Lógica para obtener la lista de productos basada en la tienda, cliente y categoría
        return []

    @staticmethod
    def seleccionar_producto(productos, cliente):
        # Lógica para seleccionar un producto
        pass

    @staticmethod
    def busqueda_categoria(categoria):
        # Lógica para buscar tiendas basadas en la categoría
        return []

    @staticmethod
    def print_tabla_tiendas(tiendas):
        print("+------------------------------------+")
        print("| No. |       Nombre de Tienda       |")
        print("+------------------------------------+")
        ancho_celda = 28

        for i, tienda in enumerate(tiendas):
            nombre_tienda = tienda.get_nombre()
            espacios = (ancho_celda - len(nombre_tienda)) // 2
            padding_izquierdo = " " * max(0, espacios)
            padding_derecho = " " * max(0, espacios + (ancho_celda - len(nombre_tienda)) % 2)
            print(f"| {i + 1:<3} |{padding_izquierdo}{nombre_tienda}{padding_derecho}|")

        numero_volver = len(tiendas) + 1
        opcion_volver = "Volver"
        espacios_volver = (ancho_celda - len(opcion_volver)) // 2
        padding_izquierdo_volver = " " * max(0, espacios_volver)
        padding_derecho_volver = " " * max(0, espacios_volver + (ancho_celda - len(opcion_volver)) % 2)
        print(f"| {numero_volver:<3} |{padding_izquierdo_volver}{opcion_volver}{padding_derecho_volver}|")
        print("+------------------------------------+")

    @staticmethod
    def print_tabla_productos(productos):
        print("+------------------------------------+")
        print("| No. |      Nombre de Producto      |")
        print("+------------------------------------+")
        ancho_celda = 28

        for i, producto in enumerate(productos):
            nombre_producto = producto.get_nombre()
            espacios = (ancho_celda - len(nombre_producto)) // 2
            padding_izquierdo = " " * max(0, espacios)
            padding_derecho = " " * max(0, espacios + (ancho_celda - len(nombre_producto)) % 2)
            print(f"| {i + 1:<3} |{padding_izquierdo}{nombre_producto}{padding_derecho}|")

        numero_volver = len(productos) + 1
        opcion_volver = "Volver"
        espacios_volver = (ancho_celda - len(opcion_volver)) // 2
        padding_izquierdo_volver = " " * max(0, espacios_volver)
        padding_derecho_volver = " " * max(0, espacios_volver + (ancho_celda - len(opcion_volver)) % 2)
        print(f"| {numero_volver:<3} |{padding_izquierdo_volver}{opcion_volver}{padding_derecho_volver}|")
        print("+------------------------------------+")

    @staticmethod
    def print_tabla_categorias(categorias):
        print("+--------------------------+")
        print("| No. |      Categoría      |")
        print("+--------------------------+")
        ancho_celda = 20

        for i, categoria in enumerate(categorias, start=1):
            categoria_texto = str(categoria)
            espacios = (ancho_celda - len(categoria_texto)) // 2
            padding_izquierdo = " " * max(0, espacios)
            padding_derecho = " " * max(0, espacios + (ancho_celda - len(categoria_texto)) % 2)
            print(f"| {i:<3} |{padding_izquierdo}{categoria_texto}{padding_derecho}|")
        print("+--------------------------+")

    @staticmethod
    def print_detalles_producto(producto):
        ancho_tabla = 44

        print("+--------------------------------------------+")
        print("|            Detalles del Producto           |")
        print("+--------------------------------------------+")
        print(f"  Nombre:        {Printer.ajustar_texto(producto.get_nombre(), ancho_tabla)}")
        print(f"  Marca:         {Printer.ajustar_texto(producto.get_marca(), ancho_tabla)}")
        print(f"  Precio:        ${producto.get_precio():.2f}")
        print(f"  Descripción:   {Printer.ajustar_texto(producto.get_descripcion(), ancho_tabla)}")
        print(f"  Tamaño:        {Printer.ajustar_texto(str(producto.get_tamaño()), ancho_tabla)}")
        print("+--------------------------------------------+")

    @staticmethod
    def ajustar_texto(texto, ancho):
        if len(texto) > ancho:
            return texto[:ancho - 3] + "..."
        else:
            return texto + " " * (ancho - len(texto))

    @staticmethod
    def print_tabla_membresias(membresias, cliente):
        print("+--------------------------+")
        print("| No. |  Tipo de Membresía  |")
        print("+--------------------------+")
        ancho_celda = 20
        contador = 1
        opciones = {}

        orden_membresias = ['BASICO', 'PREMIUM', 'VIP']
        indice_membresia_actual = orden_membresias.index(cliente.get_membresia())

        for i in range(indice_membresia_actual + 1, len(orden_membresias)):
            membresia = orden_membresias[i]
            espacios = (ancho_celda - len(membresia)) // 2
            padding_izquierdo = " " * max(0, espacios)
            padding_derecho = " " * max(0, espacios + (ancho_celda - len(membresia)) % 2)
            print(f"| {contador:<3} |{padding_izquierdo}{membresia}{padding_derecho}|")
            opciones[contador] = membresia
            contador += 1

        numero_volver = contador
        opcion_volver = "Volver"
        espacios_volver = (ancho_celda - len(opcion_volver)) // 2
        padding_izquierdo_volver = " " * max(0, espacios_volver)
        padding_derecho_volver = " " * max(0, espacios_volver + (ancho_celda - len(opcion_volver)) % 2)
        print(f"| {numero_volver:<3} |{padding_izquierdo_volver}{opcion_volver}{padding_derecho_volver}|")
        print("+--------------------------+")

        seleccion = int(input("Seleccione una opción: "))

        if seleccion == numero_volver:
            print("Volviendo al menú anterior...")
            return None

        return opciones.get(seleccion)

"""