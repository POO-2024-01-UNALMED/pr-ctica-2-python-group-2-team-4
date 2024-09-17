import math
from codeop import compile_command
from idlelib.editor import keynames
from math import trunc
from tkinter import *
from tkinter import messagebox, simpledialog


from gestorAplicacion.servicios.enums import Membresia
from gestorAplicacion.servicios.tienda import Tienda
from gestorAplicacion.sujetos.cliente import Cliente
from uiMain import interfaz
from uiMain.fieldFrame import FieldFrame


class Funcionalidad1:
    def __init__(self):
        pass


    cliente = None
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def funcion2(self,cliente,window):
        from uiMain.funcionalidad2 import Funcionalidad2
        from gestorAplicacion.sujetos.cliente import Cliente
        from gestorAplicacion.servicios.enums import Genero
        from gestorAplicacion.sujetos.persona import Persona
        funcionalidad2 = Funcionalidad2()
        funcionalidad2.elegir_tipo_busqueda(cliente, window)
    #--------------------------------------------------------------------------------------------------------------------------------------------

    """"
    def ingresar(self, window):
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()


        from .identidad import Identidad2
        persona = Identidad2(window).identificar_persona()
        if isinstance(persona, Cliente):
            self.consultasEco(persona, window)
        else:
            self.ingresar(window)
    """
    #--------------------------------------------------------------------------------------------------------------------------------------------
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
                        font=("Arial", 15),command=lambda:self.categoria(cliente,window))
        boton2.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

        # Botón 3: Consulta de membresías
        boton3 = Button(boton_frame, text="Consulta de membresías",
                        font=("Arial", 15),command=lambda:self.consulta_membresia(cliente,window))
        boton3.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
        zona2Fun1.campos.columnconfigure(1, weight=1)
        zona2Fun1.campos.rowconfigure(1, weight=1)

        # Mostrar el frame con los botones
        zona2Fun1.pack(fill=BOTH, expand=True)
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def consulta_general_productos(self, cliente, window,page=1):
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
        tiendas_frame = Frame(tiendasGeneral_frame, bg="#243340")
        tiendas_frame.pack(pady=10, fill=BOTH, expand=True)

        if Tienda.buscar_tienda():
            for t in Tienda.get_tiendas()[0].get_cajas():
                Tienda.get_tiendas()[0].get_empleados().append(t.get_cajero())
            tiendas = Tienda.revision_tienda(Tienda.get_tiendas())
            Label(tiendas_frame, text="Selecciona una de las tiendas que tenemos disponibles para ti:",
                  font=("Arial", 16), bg="#F2F2F2", fg="black").pack(pady=10)
            # Definir número de tiendas por página
            tiendas_por_pagina = 4
            total_paginas = math.ceil(len(tiendas) / tiendas_por_pagina)
            tiendas_pagina = tiendas[(page - 1) * tiendas_por_pagina: page * tiendas_por_pagina]

            # Crear un marco adicional para centrar los botones
            botones_frame = Frame(tiendas_frame, bg="#243340")
            botones_frame.pack(padx=100, pady=20, fill=BOTH, expand=True)

            # Mostrar las tiendas en la página actual
            indice = 1 + (page - 1) * tiendas_por_pagina

            for tienda in tiendas_pagina:
                Button(botones_frame, text=f"{indice}. {tienda.get_nombre()}",
                       font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                       width=35,
                       command=lambda t=tienda: self.aplicar_presupuesto(cliente, t, window)
                       ).pack(pady=5, anchor=CENTER)
                indice += 1

            # Controles de paginación
            paginacion_frame = Frame(tiendas_frame, bg="#243340")
            paginacion_frame.pack(pady=10)

            # Botón "Anterior" para ir a la página anterior
            if page > 1:
                Button(paginacion_frame, text="Anterior", font=("Arial", 12), bg="#F2F2F2", fg="black",
                       command=lambda: self.consulta_general_productos(cliente, window, page - 1)).pack(side="left",
                                                                                                        padx=5)

            # Botón "Siguiente" para ir a la página siguiente
            if page < total_paginas:
                Button(paginacion_frame, text="Siguiente", font=("Arial", 12), bg="#F2F2F2", fg="black",
                       command=lambda: self.consulta_general_productos(cliente, window, page + 1)).pack(side="right",
                                                                                                        padx=5)

            # Botón "Volver" para regresar a la pantalla anterior
            Button(botones_frame, text=f"{indice}. Volver",
                   font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35, command=lambda: self.consultasEco(cliente, window)).pack(pady=5, anchor=CENTER)
        else:
            Label(tiendas_frame,
                  text="No hay tiendas disponibles en el momento.",
                  font=("Arial", 44), bg="#F2F2F2").pack(pady=10)
            Button(tiendas_frame, text="Volver a Consultas",
                   font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35, command=lambda: self.consultasEco(cliente,window)).pack(pady=10, anchor=CENTER)
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def aplicar_presupuesto(self, cliente, tienda, window, cat=None):
        # Limpiar los widgets existentes en la ventana
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Crear el frame principal con color de fondo
        presupuesto_frame = Frame(window, bg="#243340")
        presupuesto_frame.pack(pady=20, fill=BOTH, expand=True)

        # Crear el marco interno con mayor padding
        presu_frame = Frame(presupuesto_frame, bg="#1C2833", padx=30, pady=30, relief="raised", bd=5)
        presu_frame.pack(pady=20, fill=BOTH, expand=True)

        # Título principal estilizado
        label_titulo = Label(presu_frame, text="Selecciona un presupuesto", font=("Arial", 14, "bold"), fg="white",
                             bg="#1C2833")
        label_titulo.pack(pady=10)

        # Pregunta con un estilo visual más atractivo
        label_pregunta = Label(presu_frame,
                               text="¿Deseas usar un presupuesto por defecto o ingresar uno personalizado?",
                               font=("Arial", 12), fg="white", bg="#1C2833", wraplength=400, justify="center")
        label_pregunta.pack(pady=15)

        # Botón para presupuesto por defecto, con color mejorado
        button_defecto = Button(presu_frame, text="Usar presupuesto por defecto", font=("Arial", 12, "bold"),
                                bg="#2874A6", fg="white", padx=20, pady=10,
                                command=lambda: self.enlace(cliente, tienda, None, window, cat))
        button_defecto.pack(pady=10, fill=X)

        # Etiqueta para presupuesto personalizado
        label_personalizado = Label(presu_frame, text="Ingresar presupuesto personalizado",
                                    font=("Arial", 12, "italic"),
                                    fg="white", bg="#1C2833")
        label_personalizado.pack(pady=10)

        # Entrada de texto para el presupuesto personalizado
        self.entry_presupuesto = Entry(presu_frame, font=("Arial", 12), justify="center", relief="sunken", bd=3)
        self.entry_presupuesto.pack(pady=10, ipadx=5, ipady=5)

        # Botón para aplicar el presupuesto personalizado con colores llamativos
        button_personalizado = Button(presu_frame, text="Aplicar presupuesto personalizado", font=("Arial", 12, "bold"),
                                      bg="#28B463", fg="white", padx=20, pady=10,
                                      command=lambda: self.enlace(cliente, tienda, self.entry_presupuesto.get(), window,
                                                                  cat))
        button_personalizado.pack(pady=20, fill=X)

    #--------------------------------------------------------------------------------------------------------------------------------------------
    def enlace(self, cliente, tienda, presupuesto, window,cat=None):


        numero = presupuesto
        if presupuesto == None:
            # Presupuesto por defecto
            cliente.asignaciones(cliente, tienda, 100000, 50000)
            print(cliente.get_dinero())
            print(cliente.get_tienda().get_nombre())
            self.presupuestoAsignado(cliente, tienda, window,cat)
        else:
            try:
                numero = float(numero)  # Intentamos convertir el valor a float
            except ValueError:
                messagebox.showerror("Error", "Debes ingresar un numero.")
            if float(presupuesto) > 0 and isinstance(float(presupuesto),float):
                cliente.asignaciones(cliente, tienda, 100000, 50000, float(presupuesto))
                print(cliente.get_dinero())
                print(cliente.get_tienda().get_nombre())
                self.presupuestoAsignado(cliente, tienda, window,cat)
            else:
                messagebox.showinfo("No se asigno el presupuesto","Vuelve a intentarlo")
                self.entry_presupuesto.delete(0,last=END)
                self.aplicar_presupuesto(cliente, tienda, window)
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def presupuestoAsignado(self,cliente,tienda,window,cat=None):
        from gestorAplicacion.servicios.carrito import Carrito
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        cliente.set_tienda(tienda)
        carrito=Carrito(cliente)
        cliente.set_carrito(carrito)

        # Crear un FieldFrame con el título y descripción correspondiente
        zona2Fun1 = FieldFrame(window, "", [None], "", [],
                               [None], f"Has seleccionado la tienda: {tienda.get_nombre()}",
                               "Esta servira para escoger productos en la funcionalidad 2",
                               False, 25, 15, "#243340", "white", "black", "#F2F2F2", 0, 800)

        # Crear un Frame para los botones y añadirlo al `FieldFrame`
        boton_frame = Frame(zona2Fun1.campos, bg="#F2F2F2")
        boton_frame.grid(row=0, column=1, columnspan=2, pady=20, padx=10, sticky='nsew')

        # Configurar las columnas y filas del `boton_frame` para que se expandan
        boton_frame.columnconfigure(0, weight=1)
        boton_frame.rowconfigure(0, weight=1)
        boton_frame.rowconfigure(1, weight=1)
        boton_frame.rowconfigure(2, weight=1)
        boton_frame.rowconfigure(3, weight=1)

        if cat==None:
            # Botón 1: Consulta general de productos
            boton1 = Button(boton_frame, text="Desea ver la descripcion de productos en la tienda",
                            font=("Arial", 15),command=lambda:self.mostrar_productos_general(cliente,tienda,window))
            boton1.grid(row=1, column=0, sticky='ew', padx=50, pady=10)
        else:
            # Botón 1: Consulta general de productos
            boton1 = Button(boton_frame, text="Desea ver la descripcion de productos en la tienda",
                            font=("Arial", 15), command=lambda: self.mostrar_productos_por_categoria(cliente, tienda,cat, window))
            boton1.grid(row=1, column=0, sticky='ew', padx=50, pady=10)

        # Botón 2: Consulta de productos por categoría
        boton2 = Button(boton_frame, text="Desea ir a la fun2 para empezar a hacer sus compras",
                        font=("Arial", 15), command=lambda:self.funcion2(cliente,window))
        boton2.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

        # Botón 3: Consulta de membresías
        boton3 = Button(boton_frame, text="Volver a escoger tienda",
                        font=("Arial", 15), command=lambda: self.consulta_general_productos(cliente, window))
        boton3.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

        # Botón 4: Consulta de membresías
        boton3 = Button(boton_frame, text="Volver al menu principal",
                        font=("Arial", 15), command=lambda: self.consultasEco(cliente, window))
        boton3.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
        zona2Fun1.campos.columnconfigure(1, weight=1)
        zona2Fun1.campos.rowconfigure(1, weight=1)

        # Mostrar el frame con los botones
        zona2Fun1.pack(fill=BOTH, expand=True)
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def mostrar_productos_general(self, cliente, tienda, window, page=1):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()


        productos = tienda.buscar_productos1()

        # Mostrar productos encontrados
        productos_frame = Frame(window, bg="#243340")
        productos_frame.pack(pady=10, fill=BOTH, expand=True)

        if not productos:
            Label(productos_frame,
                  text="No hay productos disponibles",
                  font=("Arial", 12), bg="F2F2F2").pack(pady=10)
            Button(productos_frame, text="Volver a Consulta",
                   font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35, command=lambda: self.consultasEco(cliente, window)).pack(pady=10, anchor=CENTER)
            return

        Label(productos_frame, text=f"Productos de  {tienda.get_nombre()}:",
              font=("Arial", 16), bg="#F2F2F2").pack(pady=10)

        # Definir número de productos por página
        productos_por_pagina = 4
        total_paginas = math.ceil(len(productos) / productos_por_pagina)
        productos = productos[(page - 1) * productos_por_pagina: page * productos_por_pagina]

        botones_frame = Frame(productos_frame, bg="#F2F2F2")
        botones_frame.pack(pady=10, fill=BOTH, expand=True)

        for i, producto in enumerate(productos):
            Button(botones_frame,
                   text=f"{producto.get_nombre()} ",
                   font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35, command=lambda prod=producto: self.detalles(cliente,tienda,producto, window)).pack(pady=5,
                                                                                                             anchor=CENTER)

        # Controles de paginación
        paginacion_frame = Frame(productos_frame, bg="#243340")
        paginacion_frame.pack(pady=10)

        # Botones de paginación
        if page > 1:
            Button(paginacion_frame, text="Anterior", font=("Arial", 12), bg="#243340", fg="white",
                   command=lambda: self.mostrar_productos_general(cliente, tienda, window, page - 1)).pack(
                side="left", padx=5)

        if page < total_paginas:
            Button(paginacion_frame, text="Siguiente", font=("Arial", 12), bg="#243340", fg="white",
                   command=lambda: self.mostrar_productos_general(cliente, tienda, window, page + 1)).pack(
                side="right", padx=5)

        Button(productos_frame, text="Volver", font=("Arial", 12), bg="#243340", padx=30, pady=15,fg="white",
               width=35, command=lambda: self.consultasEco(cliente, window)).pack(pady=10, anchor=CENTER)
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def detalles(self,cliente,tienda,producto, window,cat=None):
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Crear un FieldFrame con el título y descripción correspondiente
        zona2Fun1 = FieldFrame(window, "Caracteristicas", ["Marca","Precio","Tamano"], "", [f"{producto.get_marca()}",f"$ {producto.get_precio()}",f"{producto.get_tamano().value}"],
                               [None, None, None], f"{producto.get_nombre()}",
                               f"{producto.get_descripcion()}"
                               , False, 25, 15, "#243340", "white", "black", "#F2F2F2", 0, 800)


        # Crear un Frame para los botones y añadirlo al `FieldFrame`
        boton_frame = Frame(zona2Fun1.campos, bg="#F2F2F2")
        boton_frame.grid(row=4, column=1, columnspan=2, pady=20, padx=10, sticky='nsew')

        # Configurar las columnas y filas del `boton_frame` para que se expandan
        boton_frame.columnconfigure(0, weight=1)
        boton_frame.rowconfigure(0, weight=1)
        boton_frame.rowconfigure(1, weight=1)
        boton_frame.rowconfigure(2, weight=1)
        boton_frame.rowconfigure(3, weight=1)
        if cat==None:
            # Botón 3: Consulta de membresías
            boton3 = Button(boton_frame, text="Mirar otro Producto", font=("Arial", 15),command=lambda:self.mostrar_productos_general(cliente,tienda,window))
            boton3.grid(row=3, column=0, sticky='ew', padx=50, pady=10)
        else:
            # Botón 3: Consulta de membresías
            boton3 = Button(boton_frame, text="Mirar otro Producto", font=("Arial", 15),command=lambda: self.mostrar_productos_por_categoria(cliente,tienda,cat,window))
            boton3.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

        # Botón 4: Volver al menú principal
        boton4 = Button(boton_frame, text="Volver al Ecosistema de consultas", font=("Arial", 15),command=lambda:self.consultasEco(cliente,window))
        boton4.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
        zona2Fun1.campos.columnconfigure(1, weight=1)
        zona2Fun1.campos.rowconfigure(1, weight=1)

        # Mostrar el frame con los botones
        zona2Fun1.pack(fill=BOTH, expand=True)
    #--------------------------------------------------------------------------------------------------------------------------------------------
    def categoria(self, cliente, window):
            # Limpieza de cualquier mensaje previo en la ventana
            widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
            for i, widget in enumerate(widgets):
                if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                    widget.destroy()

            # Recolectar y mostrar las categorías disponibles
            from gestorAplicacion.servicios.enums import Categoria

            # Crear el marco para las categorías
            categorias_frame = Frame(window, bg="#243340")
            categorias_frame.pack(pady=10, fill=BOTH, expand=True)

            Label(categorias_frame, text="Estas son las categorías de los productos de nuestras tiendas:",
                  font=("Arial", 16), bg="#F2F2F2").pack(pady=10)

            # Crear un marco adicional para centrar los botones
            botones_frame = Frame(categorias_frame, bg="#243340")
            botones_frame.pack(pady=10, fill=BOTH, expand=True)

            enumerado = 1
            categoria_dict = {}
            for tipo in Categoria:
                categoria_dict[enumerado] = tipo
                Button(botones_frame, text=f"{enumerado}. {tipo.get_texto()}",
                       font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                       width=35,
                       command=lambda cat=tipo: self.consulta_categoria(cliente, cat, window)).pack(
                    pady=5, anchor=CENTER)
                enumerado += 1
            Button(botones_frame, text=f"Volver",font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35,command=lambda:self.consultasEco(cliente,window)).pack(
                pady=5, anchor=CENTER)

    #--------------------------------------------------------------------------------------------------------------------------------------------
    def consulta_categoria(self, cliente,cat, window,page=1):
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
        tiendas_frame = Frame(tiendasGeneral_frame, bg="#243340")
        tiendas_frame.pack(pady=10, fill=BOTH, expand=True)

        if Tienda.buscar_tienda_categoria(cat):
            tiendas = Tienda.categoria_tienda(cat)
            Label(tiendas_frame, text=f"Selecciona una de las tiendas que tenemos disponibles para ti en la categoria {cat.get_texto()}:",
                  font=("Arial", 16), bg="#F2F2F2", fg="black").pack(pady=10)
            # Definir número de tiendas por página
            tiendas_por_pagina = 4
            total_paginas = math.ceil(len(tiendas) / tiendas_por_pagina)
            tiendas_pagina = tiendas[(page - 1) * tiendas_por_pagina: page * tiendas_por_pagina]

            # Crear un marco adicional para centrar los botones
            botones_frame = Frame(tiendas_frame, bg="#243340")
            botones_frame.pack(padx=100, pady=20, fill=BOTH, expand=True)

            # Mostrar las tiendas en la página actual
            indice = 1 + (page - 1) * tiendas_por_pagina

            for tienda in tiendas_pagina:
                Button(botones_frame, text=f"{indice}. {tienda.get_nombre()}",
                       font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                       width=35,
                       command=lambda t=tienda: self.aplicar_presupuesto(cliente, t, window,cat)
                       ).pack(pady=5, anchor=CENTER)
                indice += 1

            # Controles de paginación
            paginacion_frame = Frame(tiendas_frame, bg="#243340")
            paginacion_frame.pack(pady=10)

            # Botón "Anterior" para ir a la página anterior
            if page > 1:
                Button(paginacion_frame, text="Anterior", font=("Arial", 12), bg="#F2F2F2", fg="black",
                       command=lambda: self.consulta_categoria(cliente,cat, window, page - 1)).pack(side="left",
                                                                                                        padx=5)

            # Botón "Siguiente" para ir a la página siguiente
            if page < total_paginas:
                Button(paginacion_frame, text="Siguiente", font=("Arial", 12), bg="#F2F2F2", fg="black",
                       command=lambda: self.consulta_categoria(cliente,cat, window, page + 1)).pack(side="right",
                                                                                                        padx=5)

            # Botón "Volver" para regresar a la pantalla anterior
            Button(botones_frame, text=f"{indice}. Volver",
                   font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35, command=lambda: self.categoria(cliente, window)).pack(pady=5, anchor=CENTER)
        else:
            Label(tiendas_frame,
                  text="No hay tiendas disponibles en el momento.",
                  font=("Arial", 44), bg="#F2F2F2").pack(pady=10)
            Button(tiendas_frame, text="Volver a Consultas",
                   font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                   width=35, command=lambda: self.consultasEco(cliente,window)).pack(pady=10, anchor=CENTER)
    #--------------------------------------------------------------------------------------------------------------------------------------------

    def mostrar_productos_por_categoria(self, cliente,tienda, categoria, window, page=1):
            widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
            for i, widget in enumerate(widgets):
                if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                    widget.destroy()

            productos = cliente.get_tienda().buscar_productos(categoria)

            # Mostrar productos encontrados
            productos_frame = Frame(window, bg="#243340")
            productos_frame.pack(pady=10, fill=BOTH, expand=True)

            # Configurar las columnas y filas del `productos_frame` para que se expandan
            productos_frame.columnconfigure(0, weight=1)
            productos_frame.rowconfigure(0, weight=1)
            productos_frame.rowconfigure(1, weight=1)
            productos_frame.rowconfigure(2, weight=1)
            productos_frame.rowconfigure(3, weight=1)

            if not productos:
                Label(productos_frame,
                      text="No hay productos disponibles",
                      font=("Arial", 24), bg="#F2F2F2").grid(row=0, column=0, pady=10, columnspan=2)
                Button(productos_frame, text="Volver a Consulta",
                       font=("Arial", 24), bg="#F2F2F2", padx=30, pady=15,
                       width=35, command=lambda: self.consultasEco(cliente, window)).grid(row=1, column=0, pady=10,
                                                                                          columnspan=2)
                return

            Label(productos_frame, text=f"Productos de {tienda.get_nombre()} de la categoria {categoria.get_texto()}:",
                  font=("Arial", 16), bg="#F2F2F2").grid(row=0, column=0, pady=10, columnspan=2)

            # Definir número de productos por página
            productos_por_pagina = 4
            total_paginas = math.ceil(len(productos) / productos_por_pagina)
            productos = productos[(page - 1) * productos_por_pagina: page * productos_por_pagina]

            # Crear el `botones_frame` y expandir en la columna 0
            botones_frame = Frame(productos_frame, bg="#F2F2F2")
            botones_frame.grid(row=1, column=0, pady=10, columnspan=2, sticky="ew")

            # Configurar las columnas del `botones_frame` para que los botones se expandan
            botones_frame.columnconfigure(0, weight=1)

            # Crear los botones dentro del `botones_frame` y centrarlos
            for i, producto in enumerate(productos):
                Button(botones_frame,
                       text=f"{producto.get_nombre()} ",
                       font=("Arial", 12), bg="#243340", padx=30, pady=15,
                       width=35,fg="white",
                       command=lambda prod=producto: self.detalles(cliente, tienda, producto, window, categoria)).grid(
                    row=i, column=0, pady=5, padx=5, sticky="ew")

            # Controles de paginación
            paginacion_frame = Frame(productos_frame, bg="#243340")
            paginacion_frame.grid(row=2, column=0, pady=10, columnspan=2)

            # Botones de paginación
            if page > 1:
                Button(paginacion_frame, text="Anterior", font=("Arial", 12), bg="#243340", fg="white", width=35,
                       padx=30,
                       command=lambda: self.mostrar_productos_por_categoria(cliente, categoria, tienda, window,
                                                                            page - 1)).grid(
                    row=2, column=1, padx=5, sticky="w")

            if page < total_paginas:
                Button(paginacion_frame, text="Siguiente", font=("Arial", 12), bg="#243340", fg="white", width=35,
                       padx=30,
                       command=lambda: self.mostrar_productos_por_categoria(cliente, categoria, tienda, window,
                                                                            page + 1)).grid(
                    row=2, column=0, padx=5, sticky="e")

            # Botón de volver
            Button(productos_frame, text="Volver", font=("Arial", 12), bg="#243340", padx=30, pady=5, fg="white",
                   width=35, command=lambda: self.consultasEco(cliente, window)).grid(row=3, column=0, pady=10,
                                                                                      columnspan=2)

    #--------------------------------------------------------------------------------------------------------------------------------------------
    def consulta_membresia(self, cliente, window):
        from gestorAplicacion.sujetos.cliente import Cliente
        from uiMain.main import Main
        from gestorAplicacion.servicios.tienda import Tienda
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        if Tienda.buscar_tienda():

            if cliente.get_edad()>18:
                if cliente.get_membresia()==None:
                    from gestorAplicacion.servicios.enums import Membresia
                    # Crear un FieldFrame con el título y descripción correspondiente
                    zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                           [None], "Membresias",
                                           None
                                           , False, 25, 15, "#243340", "white", "black", "#243340", 0, 800,False)

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
                    texto_label = Label(boton_frame, text="No tienes una membresía. ¿Te gustaría elegir una?",
                                        font=("Arial", 20), bg="#F2F2F2")
                    texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

                    membresia_dict = {}
                    enumerado = 1
                    for tipo in Membresia:
                        membresia_dict[enumerado] = tipo
                        Button(boton_frame, text=f"{tipo.get_nombre()}",
                               font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                               width=35,command=lambda mem=tipo: self.presentar_membresia(cliente,mem,window)
                               ).grid(row=enumerado, column=0, sticky='ew', padx=50, pady=10)
                        enumerado+=1

                    # Botón 4: Volver al menú principal
                    boton4 = Button(boton_frame, text="Volver", font=("Arial", 15),command=lambda:self.consultasEco(cliente,window) )
                    boton4.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

                    # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
                    zona2Fun1.campos.columnconfigure(1, weight=1)
                    zona2Fun1.campos.rowconfigure(1, weight=1)

                    # Mostrar el frame con los botones
                    zona2Fun1.pack(fill=BOTH, expand=True)
                else:
                    from gestorAplicacion.servicios.enums import Membresia
                    if cliente.get_membresia()==Membresia.VIP:
                        perfil = cliente.perfil_demografico()
                        mensaje = cliente.get_mensaje_por_perfil(perfil, cliente.get_membresia())
                        # Crear un FieldFrame con el título y descripción correspondiente
                        zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                               [None], f"Membresia { cliente.get_membresia().get_nombre()}", f"{mensaje}", False, 25,
                                               15, "#243340", "white", "black", "#243340", 0, 0, True)

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
                        texto_label = Label(boton_frame, text="¡Gracias por ser un cliente VIP! Disfruta de todos los beneficios exclusivos.\nRecuerda ir a revisar alguna tienda esto servirá para escoger productos en la funcionalidad 2",
                                            font=("Arial", 20), bg="#F2F2F2")
                        texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

                        # Botón 4: Volver al menú principal
                        boton4 = Button(boton_frame, text="Volver", font=("Arial", 15),
                                        command=lambda: self.consultasEco(cliente, window))
                        boton4.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

                        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
                        zona2Fun1.campos.columnconfigure(1, weight=1)
                        zona2Fun1.campos.rowconfigure(1, weight=1)

                        # Mostrar el frame con los botones
                        zona2Fun1.pack(fill=BOTH, expand=True)
                    elif cliente.get_membresia()==Membresia.BASICO:
                        perfil = cliente.perfil_demografico()
                        mensaje = cliente.get_mensaje_por_perfil(perfil, cliente.get_membresia())
                        # Crear un FieldFrame con el título y descripción correspondiente
                        zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                               [None], f"Membresia {cliente.get_membresia().get_nombre()}",
                                               f"{mensaje}", False, 25,
                                               15, "#243340", "white", "black", "#243340", 0, 0, True)

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
                        texto_label = Label(boton_frame,
                                            text="¡¿Te gustaría mejorar tu membresía?",
                                            font=("Arial", 20), bg="#F2F2F2")
                        texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

                        # Botón 3: Aceptar
                        boton4 = Button(boton_frame, text="Aceptar", font=("Arial", 15),
                                        command=lambda: self.intermedio(cliente,cliente.get_membresia(),window))
                        boton4.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

                        # Botón 4: Volver al menú principal
                        boton4 = Button(boton_frame, text="Cancelar", font=("Arial", 15),
                                        command=lambda: self.consultasEco(cliente, window))
                        boton4.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

                        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
                        zona2Fun1.campos.columnconfigure(1, weight=1)
                        zona2Fun1.campos.rowconfigure(1, weight=1)

                        # Mostrar el frame con los botones
                        zona2Fun1.pack(fill=BOTH, expand=True)

                    elif cliente.get_membresia()==Membresia.PREMIUM:
                        perfil = cliente.perfil_demografico()
                        mensaje = cliente.get_mensaje_por_perfil(perfil, cliente.get_membresia())
                        # Crear un FieldFrame con el título y descripción correspondiente
                        zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                               [None], f"Membresia {cliente.get_membresia().get_nombre()}",
                                               f"{mensaje}", False, 25,
                                               15, "#243340", "white", "black", "#243340", 0, 0, True)

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
                        texto_label = Label(boton_frame,
                                            text="¡¿Te gustaría mejorar tu membresía?",
                                            font=("Arial", 20), bg="#F2F2F2")
                        texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

                        # Botón 3: Aceptar
                        boton4 = Button(boton_frame, text="Aceptar", font=("Arial", 15),
                                        command=lambda: self.intermedio(cliente,cliente.get_membresia(),window))
                        boton4.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

                        # Botón 4: Volver al menú principal
                        boton4 = Button(boton_frame, text="Cancelar", font=("Arial", 15),
                                        command=lambda: self.consultasEco(cliente, window))
                        boton4.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

                        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
                        zona2Fun1.campos.columnconfigure(1, weight=1)
                        zona2Fun1.campos.rowconfigure(1, weight=1)

                        # Mostrar el frame con los botones
                        zona2Fun1.pack(fill=BOTH, expand=True)






            else:
                # Crear el marco para las Tiendas
                tiendasGeneral_frame = Frame(window, bg="#243340")
                tiendasGeneral_frame.pack(pady=10, fill=BOTH, expand=True)

                # Crear el marco para las Tiendas
                membresia_frame = Frame(tiendasGeneral_frame, bg="#243340")
                membresia_frame.pack(pady=10, fill=BOTH, expand=True)
                Label(membresia_frame,
                      text="Lo sentimos, no puedes obtener una membresía ya que eres menor de edad\nRecuerda ir a revisar alguna tienda esto servirá para escoger productos en la funcionalidad 2",
                      font=("Arial", 25), bg="#F2F2F2").pack(pady=10)
                Button(membresia_frame, text="Volver a Consultas",
                       font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                       width=35, command=lambda: self.consultasEco(cliente, window)).pack(pady=10, anchor=CENTER)


        else:
            # Crear el marco para las Tiendas
            tiendasGeneral_frame = Frame(window, bg="#243340")
            tiendasGeneral_frame.pack(pady=10, fill=BOTH, expand=True)

            # Crear el marco para las Tiendas
            membresia_frame = Frame(tiendasGeneral_frame, bg="#243340")
            membresia_frame.pack(pady=10, fill=BOTH, expand=True)

            Label(membresia_frame,
                    text="No hay tiendas disponibles en el momento.",
                    font=("Arial", 44), bg="#F2F2F2").pack(pady=10)
            Button(membresia_frame, text="Volver a Consultas",
                    font=("Arial", 12), bg="#F2F2F2", padx=30, pady=15,
                    width=35, command=lambda: self.consultasEco(cliente,window)).pack(pady=10, anchor=CENTER)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------
    def presentar_membresia(self,cliente,membresia,window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        from gestorAplicacion.servicios.enums import Membresia
        perfil=cliente.perfil_demografico()
        mensaje=cliente.get_mensaje_por_perfil(perfil, membresia)
        # Crear un FieldFrame con el título y descripción correspondiente
        zona2Fun1 = FieldFrame(window, None, [None], None, [],
                               [None], f"Membresia {membresia.get_nombre()}",f"{mensaje}",False, 25, 15, "#243340", "white", "black", "#243340", 0, 0, True)

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
        texto_label1 = Label(boton_frame, text=f"El valor de la membresia es ${membresia.get_precio()}",
                             font=("Arial", 20), bg="#F2F2F2")
        texto_label1.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

        texto_label = Label(boton_frame, text="¿Deseas comprar esta membresía?",
                            font=("Arial", 20), bg="#F2F2F2")
        texto_label.grid(row=1, column=0, sticky='ew', padx=50, pady=10)

        # Botón 4: Volver al menú principal
        boton4 = Button(boton_frame, text="Aceptar", font=("Arial", 15),
                   command=lambda:self.felicitar_membresia(cliente,membresia,window))
        boton4.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

        # Botón 4: Volver al menú principal
        boton4 = Button(boton_frame, text="Cancelar", font=("Arial", 15),
                        command=lambda:self.consulta_membresia(cliente,window))
        boton4.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

        # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
        zona2Fun1.campos.columnconfigure(1, weight=1)
        zona2Fun1.campos.rowconfigure(1, weight=1)

        # Mostrar el frame con los botones
        zona2Fun1.pack(fill=BOTH, expand=True)

    def felicitar_membresia(self,cliente,membresia,window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        from gestorAplicacion.servicios.enums import Membresia

        mensaje=cliente.evolucionar_membresia(cliente,membresia)
        if cliente.get_dinero()> membresia.get_precio():
            # Crear un FieldFrame con el título y descripción correspondiente
            zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                   [None], f"Felicitaciones!", None, False, 25, 15, "#243340",
                                   "white", "black", "#243340", 0, 0, False)

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
            texto_label1 = Label(boton_frame, text=f"{mensaje}",
                                 font=("Arial", 20), bg="#F2F2F2")
            texto_label1.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

            # Botón 4: Volver al menú principal
            boton4 = Button(boton_frame, text="Volver a menu principal", font=("Arial", 15),
                        command= lambda:self.consultasEco(cliente,window))
            boton4.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

            # Botón 4: Volver al menú principal
            boton4 = Button(boton_frame, text="Mirar otra Membresia", font=("Arial", 15),
                            command=lambda: self.consulta_membresia(cliente, window))
            boton4.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

            # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
            zona2Fun1.campos.columnconfigure(1, weight=1)
            zona2Fun1.campos.rowconfigure(1, weight=1)

            # Mostrar el frame con los botones
            zona2Fun1.pack(fill=BOTH, expand=True)
        else:
            # Crear un FieldFrame con el título y descripción correspondiente
            zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                   [None], f"Lo lamentamos!", None, False, 25, 15, "#243340",
                                   "white", "black", "#243340", 0, 0, False)

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
            texto_label1 = Label(boton_frame, text=f"{mensaje}",
                                 font=("Arial", 20), bg="#F2F2F2")
            texto_label1.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

            # Botón 4: Volver al menú principal
            boton4 = Button(boton_frame, text="Volver a menu principal", font=("Arial", 15),
                            command=lambda: self.consultasEco(cliente, window))
            boton4.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

            # Botón 4: Volver al menú principal
            boton4 = Button(boton_frame, text="Mirar otra Membresia", font=("Arial", 15),
                            command=lambda: self.consulta_membresia(cliente, window))
            boton4.grid(row=3, column=0, sticky='ew', padx=50, pady=10)

            # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
            zona2Fun1.campos.columnconfigure(1, weight=1)
            zona2Fun1.campos.rowconfigure(1, weight=1)

            # Mostrar el frame con los botones
            zona2Fun1.pack(fill=BOTH, expand=True)

    def intermedio(self,cliente,membresia,window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        from gestorAplicacion.servicios.enums import Membresia
        if membresia == Membresia.BASICO:
            # Crear un FieldFrame con el título y descripción correspondiente
            zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                   [None], "Puedes mejorar tu membresia a",
                                   None
                                   , False, 25, 15, "#243340", "white", "black", "#243340", 0, 800, False)

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
            texto_label = Label(boton_frame,
                                text=f"Las mejoras Te costaran\nPremiun ${Membresia.PREMIUM.get_precio()}\nVIP ${Membresia.VIP.get_precio()}\nTu saldo actual es de {cliente.get_dinero()}",
                                font=("Arial", 20), bg="#F2F2F2")
            texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

            # Botón 1: Volver al menú principal
            boton1 = Button(boton_frame, text=f"Membresia {Membresia.PREMIUM.get_nombre()}", font=("Arial", 15),
                            command=lambda: self.felicitar_membresia(cliente,Membresia.PREMIUM, window))
            boton1.grid(row=1, column=0, sticky='ew', padx=50, pady=10)

            # Botón 2: Volver al menú principal
            boton2 = Button(boton_frame, text=f"Membresia {Membresia.VIP.get_nombre()}", font=("Arial", 15),
                            command=lambda: self.felicitar_membresia(cliente,Membresia.VIP, window))
            boton2.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

            # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
            zona2Fun1.campos.columnconfigure(1, weight=1)
            zona2Fun1.campos.rowconfigure(1, weight=1)

            # Mostrar el frame con los botones
            zona2Fun1.pack(fill=BOTH, expand=True)

        elif membresia == Membresia.PREMIUM :
            # Crear un FieldFrame con el título y descripción correspondiente
            zona2Fun1 = FieldFrame(window, None, [None], None, [],
                                   [None], "Puedes mejorar tu membresia a",
                                   None
                                   , False, 25, 15, "#243340", "white", "black", "#243340", 0, 800, False)

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
            texto_label = Label(boton_frame, text=f"Las mejoras Te costaran\nPremiun ${Membresia.PREMIUM.get_precio()}\nTu saldo actual es de {cliente.get_dinero()}",
                                font=("Arial", 20), bg="#F2F2F2")
            texto_label.grid(row=0, column=0, sticky='ew', padx=50, pady=10)

            # Botón 2: Volver al menú principal
            boton2 = Button(boton_frame, text=f"Membresia {Membresia.VIP.get_nombre()}", font=("Arial", 15),
                                command=lambda: self.felicitar_membresia(cliente,Membresia.VIP, window))
            boton2.grid(row=2, column=0, sticky='ew', padx=50, pady=10)

            # Ajustar la configuración del grid para que el `boton_frame` ocupe el espacio disponible
            zona2Fun1.campos.columnconfigure(1, weight=1)
            zona2Fun1.campos.rowconfigure(1, weight=1)

            # Mostrar el frame con los botones
            zona2Fun1.pack(fill=BOTH, expand=True)