import sys
from tkinter import Frame, Label, Entry, Button, messagebox, simpledialog, IntVar, Radiobutton, StringVar, RIGHT, LEFT, \
    font, BOTH

from numpy.ma.core import filled

from gestorAplicacion.servicios.ahorcado import Ahorcado
from gestorAplicacion.servicios.enums import TipoCaja
from gestorAplicacion.servicios.tresEnRaya import TresEnRaya
from gestorAplicacion.sujetos import cliente
from gestorAplicacion.sujetos.administrador import Administrador
from gestorAplicacion.sujetos.cliente import Cliente
from uiMain.fieldFrame import FieldFrame
from uiMain.main import Main
import tkinter as tk

class Funcionalidad3:

    def __init__(self):
        self.precio_con_descuento = None

    def impresion_facturas(self, persona, window):
        from tkinter import Frame, Label, Button, Listbox, END, Tk, Scrollbar, VERTICAL
        # Limpiar la ventana actual
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Obtener las tiendas con facturas
        tiendas = persona.get_tiendas_con_facturas()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)

        for widget in frame.campos.winfo_children():
            widget.destroy()

        frame1=frame.campos

        # Verificar si hay tiendas con facturas
        if not tiendas:
            Label(frame1, text="No tienes facturas en ninguna tienda.",
                  font=("Arial", 14), bg="#69a0ce").pack(pady=20)
            return

        # Crear un frame para mostrar las tiendas
        frame_tiendas = Frame(frame1, bg="#69a0ce")
        frame_tiendas.pack(fill='both', expand=True, pady=20)

        # Título
        Label(frame_tiendas, text="Selecciona una tienda:",
              font=("Arial", 16, "bold"), bg="#69a0ce").pack(pady=10)

        # Crear Listbox para las tiendas
        listbox_tiendas = Listbox(frame_tiendas, font=("Arial", 24),width=50)
        listbox_tiendas.pack(side='left', padx=10)

        # Scrollbar para el Listbox
        scrollbar = Scrollbar(frame_tiendas, orient=VERTICAL)
        scrollbar.pack(side='right', fill='both')
        listbox_tiendas.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_tiendas.yview)

        # Agregar tiendas al Listbox
        for tienda in tiendas:
            listbox_tiendas.insert(END, tienda.get_nombre())

        def seleccionar_tienda():
            seleccion = listbox_tiendas.curselection()
            if seleccion:
                index = seleccion[0]
                tienda_seleccionada = tiendas[index]
                self.mostrar_facturas(tienda_seleccionada, persona, window,frame1)
            else:
                mostrar_error("Selecciona una tienda de la lista.")

        Button(frame_tiendas, text="Seleccionar tienda",
               font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
               command=seleccionar_tienda).pack(pady=10)

        def mostrar_error(mensaje):
            Label(frame_tiendas, text=mensaje, font=("Arial", 12), fg="red", bg="#69a0ce").pack(pady=10)

        frame.pack(fill='both', expand=True, pady=20)

    def mostrar_facturas(self, tienda_seleccionada, persona, window,frame1):
        from tkinter import Frame, Label, Button, Listbox, END, Scrollbar, VERTICAL

        # Limpiar la ventana actual # Obtén todos los widgets en la ventana
        for i in frame1.winfo_children():
            i.destroy()

        mis_facturas = persona.get_facturas1(tienda_seleccionada)

        # Crear un frame para mostrar las facturas
        frame_facturas = Frame(frame1, bg="#69a0ce")
        frame_facturas.pack(fill='both', expand=True, pady=20)

        # Título
        Label(frame_facturas, text="Selecciona una factura:",
              font=("Arial", 16, "bold"), bg="#69a0ce").pack(pady=10)

        # Crear Listbox para las facturas
        listbox_facturas = Listbox(frame_facturas, font=("Arial", 24), width=60, height=10)
        listbox_facturas.pack(side='left', fill=BOTH, padx=10)

        # Scrollbar para el Listbox
        scrollbar = Scrollbar(frame_facturas, orient=VERTICAL)
        scrollbar.pack(side='right', fill='y')
        listbox_facturas.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_facturas.yview)

        # Agregar facturas al Listbox
        for factura in mis_facturas:
            info_factura = f"{factura.get_fecha_facturacion()} - {len(factura.get_productos())} productos - ${factura.calcular_total():.2f}"
            listbox_facturas.insert(END, info_factura)

        def seleccionar_factura():
            seleccion = listbox_facturas.curselection()
            if seleccion:
                index = seleccion[0]
                factura_seleccionada = mis_facturas[index]
                self.mostrar_detalle_factura(factura_seleccionada, persona, window)
            else:
                mostrar_error("Selecciona una factura de la lista.")

        Button(frame_facturas, text="Seleccionar factura",
               font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
               command=seleccionar_factura).pack(pady=10,padx=40)

        def mostrar_error(mensaje):
            Label(frame_facturas, text=mensaje, font=("Arial", 12), fg="red", bg="light blue").pack(pady=10)

    def mostrar_detalle_factura(self, factura_seleccionada, persona, window):
        from tkinter import Frame, Label, Button

        # Limpiar la ventana actual
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)

        frame1=frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()
        # Crear un frame para mostrar los detalles
        frame_detalle = Frame(frame1, bg="#69a0ce")
        frame_detalle.pack(fill='both', expand=True, pady=20)

        # Título
        Label(frame_detalle, text="Detalles de la Factura",
              font=("Arial", 16, "bold"), bg="#69a0ce").pack(pady=10)

        # Encabezado
        Label(frame_detalle, text="Productos de la factura:",
              font=("Arial", 14, "bold"), bg="#69a0ce").pack(pady=10)

        for numero_producto, producto in enumerate(factura_seleccionada.get_productos(), start=1):
            if producto:
                Label(frame_detalle,
                      text=f"{numero_producto}. {producto.get_nombre()} - {producto.get_marca()} - {producto.get_tamano().get_tamano()} - {producto.get_categoria().get_texto()} - ${producto.get_precio():.2f}",
                      font=("Arial", 12), bg="#69a0ce").pack(pady=5)

        # Opciones adicionales
        if isinstance(persona, Administrador):
            Label(frame_detalle, text="Opciones:",
                  font=("Arial", 12, "bold"), bg="light blue").pack(pady=10)
            Button(frame_detalle, text="Escoger otra factura",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: self.impresion_facturas(persona, window)).pack(pady=5)
            Button(frame_detalle, text="Salir de funcionalidad",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: Main.escoger_funcionalidad()).pack(pady=5)

        elif isinstance(persona, Cliente):
            Label(frame_detalle, text="Opciones:",
                  font=("Arial", 12, "bold"), bg="#69a0ce").pack(pady=10)
            Button(frame_detalle, text="Pagar factura",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: self.seleccionar_caja(persona,factura_seleccionada,window)).pack(pady=10)
            Button(frame_detalle, text="Escoger otra factura",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: self.impresion_facturas(persona, window)).pack(pady=10)
        frame.pack(fill='both', expand=True, pady=20)

    def seleccionar_caja(self, cliente, carrito, window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)


        cajas = cliente.get_tienda().cajas_disponibles()
        frame1=frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()
        frame.pack(fill='both', expand=True, pady=20)
        def esperar_caja():
            pass

        def salir():
            pass

        if not cajas:
            mensaje_label = Label(frame1, text="No hay cajas disponibles.")
            mensaje_label.pack(pady=5)

            # Botón para esperar a que una caja esté disponible
            esperar_button = Button(frame1, text="Esperar a que una caja esté disponible",
                                       command=esperar_caja)
            esperar_button.pack(pady=5)

            # Botón para no pagar y salir
            salir_button = Button(frame1, text="No pagar y salir", command=salir)
            salir_button.pack(pady=5)

        else:
            caja_label = Label(frame1, text="Seleccione una caja para pagar:",bg="#69a0ce")
            caja_label.pack(pady=5)

            # Definir una fuente personalizada para los botones
            custom_font = font.Font(family="Helvetica", size=16, weight="bold")

            # Colores para el fondo y el texto
            bg_color = "#4CAF50"  # Verde agradable
            fg_color = "#FFFFFF"
            for i, caja in enumerate(cajas):
                cajero = caja.get_cajero()
                caja_info = f"{i + 1}. Caja: {caja.get_nombre()}, Tipo: {caja.get_tipo()}, Empleado: {cajero.get_nombre()}"

                # Crear el botón con propiedades personalizadas
                caja_button = tk.Button(
                    frame1,
                    text=caja_info,
                    font=custom_font,
                    bg=bg_color,
                    fg=fg_color,
                      # Ajusta el ancho del botón
                    height=1,  # Ajusta la altura del botón
                    relief=tk.RAISED,  # Añade un efecto de relieve
                    bd=4,  # Bordes más gruesos
                    command=lambda c=caja: self.pagar_factura(cliente, carrito, c, window)
                    # Usa `c` para evitar el problema de late binding
                )

                caja_button.pack(pady=10)

    def pagar_factura(self, cliente,carrito,caja_seleccionada,window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)
        frame1=frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()
        descuento_membresia = cliente.calcular_descuento_por_membresia()
        precio_total = carrito.calcular_total()
        self.precio_con_descuento = precio_total * (1 - descuento_membresia)

        # Imprimir factura con descuento por membresía
        factura_text = carrito.generar_detalles_factura(descuento_membresia, False)
        Label(frame1, text=factura_text, justify=LEFT,font=("Helvetica",20)).pack()
        frame1.pack(fill='x', expand=True, pady=20)
        # Opción de borrar la factura antes de pagar
        Label(frame1, text="¿Desea borrar esta factura y no pagarla?",font=("Helvetica",20)).pack(pady=5)
        Button(frame1, text="Sí",font=("Helvetica",20),bg="red",width=10, command=lambda:self.borrar_factura(carrito,cliente,caja_seleccionada)).pack(side=LEFT, padx=10, pady=10)
        Button(frame1, text="No",font=("Helvetica",20),bg="light green",width=10, command=lambda: self.opcion_juego(cliente,carrito,caja_seleccionada,window)).pack(side=RIGHT, padx=10, pady=10)
        frame.pack(fill='both', expand=True, pady=20)

    def borrar_factura(self,carrito,cliente,caja_seleccionada):
        carrito.eliminar_carrito()
        cliente.set_tienda(None)
        cliente.set_carrito(None)
        caja_seleccionada.set_cliente(None)
        carrito.set_caja(None)
        messagebox.showinfo("Factura", "Factura eliminada y productos devueltos al inventario.")
        return

    def opcion_juego(self,cliente,carrito,caja_seleccionada, window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)
        frame1=frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()
        self.gano_juego = False
        Label(frame1, text="¿Desea intentar obtener un descuento adicional jugando?, pagara 10 mil si no tiene membresia",font=("Helvetica",20),bg="#69a0ce").pack(pady=5)
        Button(frame1, text="Sí",bg="light green",font=("Helvetica",20),width=20, command=lambda: self.seleccionar_juego(cliente,carrito,caja_seleccionada,window)).pack(side=LEFT, padx=10)
        Button(frame1, text="No",bg="red",width=20,font=("Helvetica",20), command=lambda: self.confirmar_pago(cliente,carrito,caja_seleccionada,window)).pack(side=RIGHT, padx=10)
        frame.pack(fill='both', expand=True, pady=20)

    def seleccionar_juego(self,cliente,carrito,caja_seleccionada, window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)
        frame1 = frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()

        Label(frame1, text="Seleccione un juego:").pack(pady=5)
        Button(frame1, text="Tres en Raya", command=lambda: self.jugar(cliente,carrito,caja_seleccionada,window,1)).pack(side=LEFT, padx=10)
        Button(frame1, text="Ahorcado", command=lambda: self.jugar(cliente,carrito,caja_seleccionada,window, 2)).pack(side=RIGHT, padx=10)
        frame.pack(fill='both', expand=True, pady=20)

    def ahorcado(self, window):
        from gestorAplicacion.servicios.ahorcado import Ahorcado

        def handle_guess():
            letra = guess_entry.get().lower()
            if letra:
                juego_ahorcado.jugar(letra)
                update_display()
                guess_entry.delete(0, tk.END)
                if juego_ahorcado.ha_ganado():
                    result_label.config(text="¡Ganaste!")
                    guess_entry.config(state=tk.DISABLED)
                    self.gano_juego = True
                    self.ya_jugo = True
                elif juego_ahorcado.ha_perdido():
                    result_label.config(text="¡Perdiste!")
                    guess_entry.config(state=tk.DISABLED)
                    self.gano_juego = False
                    self.ya_jugo = True

        def update_display():
            estado = juego_ahorcado.obtener_estado()
            estado_label.config(text=estado)

        def restart_game():
            nonlocal juego_ahorcado
            juego_ahorcado = Ahorcado("python")  # Cambia "python" a una palabra aleatoria si lo deseas
            update_display()
            result_label.config(text="")
            guess_entry.config(state=tk.NORMAL)

        # Inicialización del juego
        juego_ahorcado = Ahorcado("python")  # Cambia "python" a una palabra aleatoria si lo deseas
        juego_ahorcado.iniciar()

        # Crear un Frame para el juego
        game_frame = tk.Frame(window, padx=10, pady=10)
        game_frame.pack(padx=20, pady=20)

        # Definir una fuente para los botones y etiquetas
        custom_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Etiqueta para mostrar el estado del juego
        estado_label = tk.Label(game_frame, text=juego_ahorcado.obtener_estado(), font=custom_font)
        estado_label.pack(pady=10)

        # Entrada para letras
        guess_entry = tk.Entry(game_frame, font=custom_font)
        guess_entry.pack(pady=5)

        # Botón para hacer la adivinanza
        guess_button = tk.Button(game_frame, text="Adivinar", font=custom_font, command=handle_guess)
        guess_button.pack(pady=5)

        # Etiqueta para mostrar el resultado
        result_label = tk.Label(game_frame, text="", font=custom_font)
        result_label.pack(pady=10)

        # Botón para reiniciar el juego
        restart_button = tk.Button(game_frame, text="Reiniciar", font=custom_font, command=restart_game)
        restart_button.pack(pady=10)

        # Actualizar la pantalla inicialmente
        update_display()

        # Esperar a que el juego termine
        while not self.ya_jugo:
            window.update_idletasks()
            window.update()

        return self.gano_juego

    def tres_en_raya(self, window):
        from gestorAplicacion.servicios.tresEnRaya import TresEnRaya

        juego = TresEnRaya()
        juego.iniciar()

        def handle_click(pos):
            if juego.jugar(pos):
                update_board()
                if juego.check_win(juego.jugador):
                    result_label.config(text="¡Ganaste!")
                    disable_buttons()
                    self.gano_juego = True
                    self.ya_jugo = True
                elif juego.check_win(juego.maquina):
                    result_label.config(text="¡Perdiste!")
                    disable_buttons()
                    self.gano_juego = False
                    self.ya_jugo = True
                elif not juego.hay_espacios():
                    result_label.config(text="¡Empate!")
                    disable_buttons()
                    self.gano_juego = False
                    self.ya_jugo = True

        def update_board():
            for i in range(3):
                for j in range(3):
                    buttons[i * 3 + j].config(text=juego.tablero[i][j])

        def disable_buttons():
            for button in buttons:
                button.config(state=tk.DISABLED)

        buttons = []
        frame=Frame(window,bg="#69a0ce")
        frame.pack(fill='both', expand=True, pady=20)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        for i in range(9):
            button = tk.Button(frame, text="", width=40,height=20, command=lambda i=i: handle_click(i + 1))
            button.grid(row=i // 3, column=i % 3)
            buttons.append(button)

        result_label = tk.Label(frame, text="")
        result_label.grid(row=3, columnspan=3)

        update_board()

        # Esperar a que el juego termine
        while not self.ya_jugo:
            window.update_idletasks()
            window.update()

        return self.gano_juego


    def jugar(self, cliente, carrito, caja_seleccionada, window, seleccion_juego):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)
        frame1 = frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()
        self.ya_jugo = False
        frame.pack(fill='both', expand=True, pady=20)

        if seleccion_juego == 1:
            self.gano_juego = self.tres_en_raya(frame1)
        elif seleccion_juego == 2:
            self.gano_juego = self.ahorcado(frame1)

        if self.gano_juego:
            tk.messagebox.showinfo("Juego", "¡Felicidades! Ha ganado un descuento adicional del 10%.")
            self.precio_con_descuento *= 0.9
        else:
            tk.messagebox.showinfo("Juego", "Lo sentimos, no ha ganado el juego.")

        self.confirmar_pago(cliente, carrito, caja_seleccionada, window)

    def confirmar_pago(self,cliente,carrito,caja_seleccionada, window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame = FieldFrame(window,
                           "La búsqueda de nuestra tienda es" + " lo más accesible para nuestros clientes. ¿Que desea hacer?",
                           [], "Escoja uno de los botones", [], [], "Funcionalidad 3",
                           "La funcionalidad de la aplicación permite al cliente interactuar de manera fluida con los productos disponibles en la tienda, ofreciéndole la posibilidad de seleccionar artículos específicos y definir sus cantidades. Los productos seleccionados se agregan al carrito de compras, desde donde se pueden revisar, modificar o eliminar según sea necesario. Una vez que el cliente ha configurado su carrito a su gusto, puede proceder a guardar la factura, lo que facilita la revisión final y el pago del total acumulado. Esta funcionalidad asegura que el proceso de compra sea sencillo y flexible, adaptándose a las necesidades del cliente y permitiendo una experiencia de compra eficiente y organizada.",
                           False)
        frame1 = frame.campos
        for widget in frame1.winfo_children():
            widget.destroy()

        Label(frame1, text="¿Desea pagar la factura?").pack(pady=5)
        factura_text = carrito.generar_detalles_factura(cliente.calcular_descuento_por_membresia(), self.gano_juego)
        Label(frame1, text=factura_text, justify=LEFT).pack(pady=10)
        Button(frame1, text="Sí", command=lambda: self.pagar_factura1(cliente,carrito,caja_seleccionada,window)).pack(side=LEFT, padx=10)
        Button(frame1, text="No", command=lambda: self.cancelar_pago(cliente,carrito,caja_seleccionada,window)).pack(side=RIGHT, padx=10)
        frame.pack(fill='both', expand=True, pady=20)

    def cancelar_pago(self,cliente,carrito,caja_seleccionada,window):
        cliente.set_tienda(None)
        cliente.set_carrito(None)
        caja_seleccionada.set_cliente(None)
        carrito.set_caja(None)
        messagebox.showinfo("Pago", "Ha decidido no pagar la factura. Regresando a la tienda.")
        self.impresion_facturas(cliente, window)

    def pagar_factura1(self,cliente,carrito,caja_seleccionada, window):
        precio_final = self.precio_con_descuento
        if cliente.get_dinero() < precio_final:
            messagebox.showinfo("Pago", "No tiene suficiente saldo para pagar la factura. Regresando a la tienda.")
            self.cancelar_pago(cliente,carrito,caja_seleccionada,window)
            return

        carrito.set_pagado(True)
        cliente.get_facturas().append(carrito)
        cliente.get_tienda().subir_saldo(precio_final)
        cliente.bajar_dinero(precio_final)

        cajero = caja_seleccionada.get_cajero()
        pago_cajero = 20000
        if cajero.get_prestacion_pension():
            pago_cajero += 5000
        if cajero.get_prestacion_salud():
            pago_cajero += 5000
        cliente.get_tienda().bajar_saldo(pago_cajero)

        cliente.set_tienda(None)
        cliente.set_carrito(None)
        caja_seleccionada.set_cliente(None)
        carrito.set_caja(None)

        messagebox.showinfo("Pago", "La factura ha sido pagada exitosamente.")
        self.impresion_facturas(cliente, window)


""" caja_seleccionada.cliente = cliente

    # Aplicar descuento por membresía
    descuento_membresia = cliente.calcular_descuento_por_membresia()
    precio_total = carrito.calcular_total()
    precio_con_descuento = precio_total * (1 - descuento_membresia)

    # Imprimir factura con descuento por membresía
    print(carrito.generar_detalles_factura(descuento_membresia, False))

    # Opción de borrar la factura antes de pagar
    print("¿Desea borrar esta factura y no pagarla?")
    print("1. Sí")
    print("2. No")
    opcion_borrar = Main.escaner_con_rango(2)

    if opcion_borrar == 1:
        carrito.eliminar_carrito()  # Eliminar carrito y devolver productos
        cliente.set_tienda(None)
        cliente.set_carrito(None)  # Desasignar carrito del cliente
        caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
        carrito.set_caja(None)  # Desasignar cliente de la caja
        print("Factura eliminada y productos devueltos al inventario.")
        return

    # Opción de jugar para obtener más descuento
    print("¿Desea intentar obtener un descuento adicional jugando?")
    print("1. Sí")
    print("2. No")
    opcion_juego = Main.escaner_con_rango(2)

    costo_juego = 0
    gano_juego = False
    if opcion_juego == 1:
        tiene_membresia = cliente.get_membresia() is not None
        if not tiene_membresia:
            print("Debe pagar 10 mil para intentar jugar.")
            costo_juego = 10000
            carrito.incrementar_costo(costo_juego)
            precio_total += costo_juego  # Aumentar el precio total antes de aplicar descuento del juego

        # Selección del juego
        print("Seleccione un juego:")
        print("1. Tres en Raya")
        print("2. Ahorcado")
        seleccion_juego = int(input())

        if seleccion_juego == 1:
            gano_juego = Funcionalidad3.tres_en_raya()
        elif seleccion_juego == 2:
            gano_juego = Funcionalidad3.ahorcado()

        if gano_juego:
            print("¡Felicidades! Ha ganado un descuento adicional del 10%.")
            precio_con_descuento *= 0.9  # Aplicar descuento adicional del juego
        else:
            print("Lo sentimos, no ha ganado el juego.")

    # Imprimir factura con descuento adicional si ganó el juego
    print(carrito.generar_detalles_factura(descuento_membresia, gano_juego))

    # Confirmar si el cliente desea pagar la factura
    print("¿Desea pagar la factura?")
    print("1. Sí")
    print("2. No")
    opcion_pago = int(input())

    if opcion_pago == 2:
        print("Ha decidido no pagar la factura. Regresando a la tienda...")
        cliente.set_tienda(None)
        cliente.set_carrito(None)  # Desasignar carrito del cliente
        caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
        carrito.set_caja(None)  # Desasignar cliente de la caja
        return
    elif opcion_pago == 1:
        # Verificar si el cliente tiene suficiente saldo
        precio_final = precio_con_descuento  # Usar el precio con descuento
        if cliente.get_dinero() < precio_final:
            print("No tiene suficiente saldo para pagar la factura. Regresando a la tienda...")
            cliente.set_tienda(None)
            cliente.set_carrito(None)  # Desasignar carrito del cliente
            caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
            carrito.set_caja(None)  # Desasignar cliente de la caja
            return

        # Marcar la factura como pagada
        carrito.set_pagado(True)
        cliente.get_facturas().append(carrito)  # Registrar la factura en las facturas del cliente

        # Actualizar saldo de la tienda
        cliente.get_tienda().subir_saldo(precio_final)

        # Restar el monto al saldo del cliente
        cliente.bajar_dinero(precio_final + costo_juego)

        # Calcular y descontar el pago del cajero
        cajero = caja_seleccionada.get_cajero()
        pago_cajero = 20000  # Pago inicial
        if cajero.get_prestacion_pension():
            pago_cajero += 5000
        if cajero.get_prestacion_salud():
            pago_cajero += 5000
        cliente.get_tienda().bajar_saldo(pago_cajero)

        # Desasignar referencias
        cliente.set_tienda(None)
        cliente.set_carrito(None)  # Desasignar carrito del cliente
        caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
        carrito.set_caja(None)  # Desasignar caja del carrito

        print("La factura ha sido pagada exitosamente.")
        Main.escoger_funcionalidad()
        caja_seleccionada = None

        def on_select_caja():
            nonlocal caja_seleccionada
            seleccion = caja_var.get() - 1
            if 0 <= seleccion < len(cajas):
                caja_seleccionada = cajas[seleccion]

                if caja_seleccionada.get_tipo() == TipoCaja.RAPIDA and len(carrito.get_productos()) > 5:
                    error_label.config(text="No puede usar la caja rápida porque tiene más de 5 productos.")
                    return

                caja_label.config(text=f"Ha seleccionado la caja: {caja_seleccionada.get_nombre()}")
                process_payment()

        def process_payment():
            # Apply membership discount
            descuento_membresia = cliente.calcular_descuento_por_membresia()
            precio_total = carrito.calcular_total()
            precio_con_descuento = precio_total * (1 - descuento_membresia)

            # Show invoice details
            factura_detalles = carrito.generar_detalles_factura(descuento_membresia, False)
            factura_text.set(factura_detalles)

            # Ask to delete invoice or not
            delete_invoice_label.grid(row=6, column=0, columnspan=2)
            delete_yes_button.grid(row=7, column=0)
            delete_no_button.grid(row=7, column=1)

        def delete_invoice():
            carrito.eliminar_carrito()
            cliente.set_tienda(None)
            cliente.set_carrito(None)
            caja_seleccionada.set_cliente(None)
            carrito.set_caja(None)
            result_label.config(text="Factura eliminada y productos devueltos al inventario.")
            delete_invoice_label.grid_forget()
            delete_yes_button.grid_forget()
            delete_no_button.grid_forget()
            pay_or_not_label.grid_forget()
            pay_yes_button.grid_forget()
            pay_no_button.grid_forget()

        def dont_delete_invoice():
            delete_invoice_label.grid_forget()
            delete_yes_button.grid_forget()
            delete_no_button.grid_forget()
            play_game()

        def play_game():
            # Ask to play for extra discount
            play_game_label.grid(row=8, column=0, columnspan=2)
            play_yes_button.grid(row=9, column=0)
            play_no_button.grid(row=9, column=1)

        def try_play_game():
            tiene_membresia = cliente.get_membresia() is not None
            costo_juego = 0
            gano_juego = False
            if not tiene_membresia:
                costo_juego = 10000
                carrito.incrementar_costo(costo_juego)
                precio_total = carrito.calcular_total()
                precio_total += costo_juego

            # Game selection
            game_select_label.grid(row=10, column=0, columnspan=2)
            three_in_row_button.grid(row=11, column=0)
            hangman_button.grid(row=11, column=1)

        def play_three_in_row():
            gano_juego = Funcionalidad3.tres_en_raya()
            finish_game()

        def play_hangman():
            gano_juego = Funcionalidad3.ahorcado()
            finish_game()

        def finish_game():
            if gano_juego:
                result_label.config(text="¡Felicidades! Ha ganado un descuento adicional del 10%.")
                precio_con_descuento *= 0.9
            else:
                result_label.config(text="Lo sentimos, no ha ganado el juego.")

            game_select_label.grid_forget()
            three_in_row_button.grid_forget()
            hangman_button.grid_forget()
            play_yes_button.grid_forget()
            play_no_button.grid_forget()
            confirm_payment()

        def confirm_payment():
            # Confirm payment
            pay_or_not_label.grid(row=12, column=0, columnspan=2)
            pay_yes_button.grid(row=13, column=0)
            pay_no_button.grid(row=13, column=1)

        def pay_invoice():
            precio_final = precio_con_descuento
            if cliente.get_dinero() < precio_final:
                result_label.config(text="No tiene suficiente saldo para pagar la factura. Regresando a la tienda...")
                return

            carrito.set_pagado(True)
            cliente.get_facturas().append(carrito)
            cliente.get_tienda().subir_saldo(precio_final)
            cliente.bajar_dinero(precio_final + costo_juego)

            cajero = caja_seleccionada.get_cajero()
            pago_cajero = 20000
            if cajero.get_prestacion_pension():
                pago_cajero += 5000
            if cajero.get_prestacion_salud():
                pago_cajero += 5000
            cliente.get_tienda().bajar_saldo(pago_cajero)

            cliente.set_tienda(None)
            cliente.set_carrito(None)
            caja_seleccionada.set_cliente(None)
            carrito.set_caja(None)

            result_label.config(text="La factura ha sido pagada exitosamente.")
            pay_or_not_label.grid_forget()
            pay_yes_button.grid_forget()
            pay_no_button.grid_forget()

        def cancel_payment():
            result_label.config(text="Ha decidido no pagar la factura. Regresando a la tienda...")
            cliente.set_tienda(None)
            cliente.set_carrito(None)
            caja_seleccionada.set_cliente(None)
            carrito.set_caja(None)
            pay_or_not_label.grid_forget()
            pay_yes_button.grid_forget()
            pay_no_button.grid_forget()

        if not cajas:
            error_label = Label(window, text="No hay cajas disponibles.")
            error_label.grid(row=0, column=0, columnspan=2)
            wait_button = Button(window, text="Esperar", command=lambda: cliente.tienda.asignar_cajero(
                cliente.tienda.encontrar_cajero(cliente.tienda.empleados)))
            wait_button.grid(row=1, column=0)
            leave_button = Button(window, text="Salir", command=lambda: Main.escoger_funcionalidad())
            leave_button.grid(row=1, column=1)
            return

        # Display available boxes
        caja_label = Label(window, text="Seleccione una caja para pagar:")
        caja_label.grid(row=0, column=0, columnspan=2)
        caja_var = IntVar()
        for i, caja in enumerate(cajas):
            Radiobutton(window, text=f"{caja.get_nombre()}, Tipo: {caja.get_tipo()}", variable=caja_var,
                           value=i + 1).grid(row=i + 1, column=0, columnspan=2)

        select_button = Button(window, text="Seleccionar", command=on_select_caja)
        select_button.grid(row=len(cajas) + 1, column=0, columnspan=2)

        factura_text = StringVar()
        factura_label = Label(window, textvariable=factura_text)
        factura_label.grid(row=5, column=0, columnspan=2)

        delete_invoice_label = Label(window, text="¿Desea borrar esta factura y no pagarla?")
        delete_yes_button = Button(window, text="Sí", command=delete_invoice)
        delete_no_button = Button(window, text="No", command=dont_delete_invoice)

        play_game_label = Label(window, text="¿Desea intentar obtener un descuento adicional jugando?")
        play_yes_button = Button(window, text="Sí", command=try_play_game)
        play_no_button = Button(window, text="No", command=confirm_payment)

        game_select_label = Label(window, text="Seleccione un juego:")
        three_in_row_button = Button(window, text="Tres en Raya", command=play_three_in_row)
        hangman_button = Button(window, text="Ahorcado", command=play_hangman)

        pay_or_not_label = Label(window, text="¿Desea pagar la factura?")
        pay_yes_button = Button(window, text="Sí", command=pay_invoice)
        pay_no_button = Button(window, text="No", command=cancel_payment)

        result_label = Label(window, text="")"""

"""
    def impresion_facturas(persona):
        from uiMain.main import Main
        from gestorAplicacion.sujetos.administrador import Administrador
        from gestorAplicacion.sujetos.cliente import Cliente
        tiendas = persona.get_tiendas_con_facturas()

        if not tiendas:
            print("No tienes facturas en ninguna tienda.")
            return

        # Crear un diccionario para contar facturas por tienda
        conteo_tiendas = {}
        for tienda in tiendas:
            nombre_tienda = tienda.get_nombre()
            if nombre_tienda:
                cantidad_facturas = len(tienda.get_facturas()) if tienda.get_facturas() else 0
                conteo_tiendas[nombre_tienda] = cantidad_facturas

        # Imprimir tabla de tiendas y cantidad de facturas
        print("Número de Facturas")
        print("+-----+----------------+-----------------+")
        print("| No. | Nombre         | Cantidad        |")
        print("+-----+----------------+-----------------+")

        for numero, (nombre, cantidad) in enumerate(conteo_tiendas.items(), start=1):
            print(f"| {numero:<3} | {nombre:<14} | {cantidad:<15} |")

        print("+-----+----------------+-----------------+")

        # Solicitar selección del usuario
        seleccion = int(input("Seleccione el número de la tienda: "))

        tienda_seleccionada = None
        if 1 <= seleccion <= len(conteo_tiendas):
            for numero, tienda in enumerate(tiendas, start=1):
                if numero == seleccion:
                    tienda_seleccionada = tienda
                    break

        if tienda_seleccionada:
            print("Has seleccionado la tienda:", tienda_seleccionada.get_nombre())
            mis_facturas = persona.get_facturas1(tienda_seleccionada)

            # Imprimir las facturas
            print("+-----+--------------------+------------+-----------------+------------+----------+")
            print("| No. | Tienda             | Fecha      | Productos        | Precio     | Pagada   |")
            print("+-----+--------------------+------------+-----------------+------------+----------+")

            for numero, factura in enumerate(mis_facturas, start=1):
                if factura:
                    estado_pago = "Sí" if factura.get_pagado() else "No"
                    precio_total = factura.calcular_total()
                    print(
                        f"| {numero:<3} | {factura.get_tienda().get_nombre():<18} | {factura.get_fecha_facturacion():<10} | {len(factura.get_productos()):<15} | {precio_total:<10.2f} | {estado_pago:<8} |")

            print("+-----+--------------------+------------+-----------------+------------+----------+")

            # Solicitar selección de factura
            seleccion = int(input("Seleccione el número de la factura que desea imprimir: "))

            if 1 <= seleccion <= len(mis_facturas):
                factura_seleccionada = mis_facturas[seleccion - 1]
                if factura_seleccionada:
                    print("Has seleccionado la factura de la tienda:", factura_seleccionada.get_tienda().get_nombre())

                    # Imprimir detalles de los productos de la factura seleccionada
                    print("+-----+--------------------+---------------+----------+------------+----------+")
                    print("| No. | Producto           | Marca         | Tamaño   | Categoría  | Precio   |")
                    print("+-----+--------------------+---------------+----------+------------+----------+")

                    for numero_producto, producto in enumerate(factura_seleccionada.get_productos(), start=1):
                        if producto:
                            print(
                                f"| {numero_producto:<3} | {producto.get_nombre():<18} | {producto.get_marca():<13} | {producto.get_tamano().get_tamano():<8} | {producto.get_categoria().get_texto():<10} | {producto.get_precio():<8.2f} |")

                    print("+-----+--------------------+---------------+----------+------------+----------+")

                    # Opciones adicionales dependiendo del tipo de objeto
                    if isinstance(persona, Administrador):
                        print("Opciones:")
                        print("1. Escoger otra factura")
                        print("2. Salir de funcionalidad")

                        opcion = int(input("Seleccione una opción: "))
                        if opcion == 1:
                            Funcionalidad3.impresion_facturas(persona)  # Volver a llamar al método
                        elif opcion == 2:
                            Main.escoger_funcionalidad()  # Llamar al método para salir de la funcionalidad
                        else:
                            print("Opción no válida.")
                    elif isinstance(persona, Cliente):
                        print("Opciones:")
                        print("1. Pagar factura")
                        print("2. Escoger otra factura")
                        print("3. Salir de funcionalidad")

                        opcion = int(input("Seleccione una opción: "))
                        if opcion == 1:
                            persona.set_tienda(factura_seleccionada.get_tienda())
                            Funcionalidad3.seleccionar_caja(persona, factura_seleccionada)
                        elif opcion == 2:
                            Funcionalidad3.impresion_facturas(persona)  # Volver a llamar al método
                        elif opcion == 3:
                            Main.escoger_funcionalidad()  # Llamar al método para salir de la funcionalidad
                        else:
                            print("Opción no válida.")
                else:
                    print("Selección inválida.")
            else:
                print("Selección inválida.")
        else:
            print("Selección inválida.")
    @staticmethod
    def seleccionar_caja(cliente,carrito):
        from gestorAplicacion.servicios.enums import TipoCaja
        from uiMain.main import Main
        cajas = cliente.get_tienda().cajas_disponibles()
        caja_seleccionada = None

        while True:
            if not cajas:
                print("No hay cajas disponibles.")
                print("1. Esperar a que una caja esté disponible.")
                print("2. No pagar y salir.")
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    tienda = cliente.tienda
                    tienda.asignar_cajero(tienda.encontrar_cajero(tienda.empleados))
                    continue  # Repetir el proceso después de asignar un empleado
                elif opcion == 2:
                    print("Ha decidido no pagar. Saliendo del proceso.")
                    Main.escoger_funcionalidad()  # Salir del método
                    return
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
                    continue

            print("Seleccione una caja para pagar:")
            for i, caja in enumerate(cajas):
                cajero = caja.get_cajero()
                print(f"{i + 1}. Caja: {caja.get_nombre()}, Tipo: {caja.get_tipo()}, Empleado: {cajero.get_nombre()}")

            seleccion = int(input("Seleccione el número de la caja: "))

            if 1 <= seleccion <= len(cajas):
                caja_seleccionada = cajas[seleccion - 1]

                if caja_seleccionada.get_tipo() == TipoCaja.RAPIDA and len(carrito.get_productos()) > 5:
                    print("No puede usar la caja rápida porque tiene más de 5 productos.")
                    print("Por favor, seleccione otra caja.")
                    continue

                print("Ha seleccionado la caja:", caja_seleccionada.get_nombre())
                break  # Caja seleccionada correctamente, salir del bucle
            else:
                print("Selección inválida. Inténtelo de nuevo.")

        caja_seleccionada.cliente = cliente

        # Aplicar descuento por membresía
        descuento_membresia = cliente.calcular_descuento_por_membresia()
        precio_total = carrito.calcular_total()
        precio_con_descuento = precio_total * (1 - descuento_membresia)

        # Imprimir factura con descuento por membresía
        print(carrito.generar_detalles_factura(descuento_membresia, False))

        # Opción de borrar la factura antes de pagar
        print("¿Desea borrar esta factura y no pagarla?")
        print("1. Sí")
        print("2. No")
        opcion_borrar = Main.escaner_con_rango(2)

        if opcion_borrar == 1:
            carrito.eliminar_carrito()# Eliminar carrito y devolver productos
            cliente.set_tienda(None)
            cliente.set_carrito(None)  # Desasignar carrito del cliente
            caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
            carrito.set_caja(None)  # Desasignar cliente de la caja
            print("Factura eliminada y productos devueltos al inventario.")
            return

        # Opción de jugar para obtener más descuento
        print("¿Desea intentar obtener un descuento adicional jugando?")
        print("1. Sí")
        print("2. No")
        opcion_juego = Main.escaner_con_rango(2)

        costo_juego = 0
        gano_juego = False
        if opcion_juego == 1:
            tiene_membresia = cliente.get_membresia() is not None
            if not tiene_membresia:
                print("Debe pagar 10 mil para intentar jugar.")
                costo_juego = 10000
                carrito.incrementar_costo(costo_juego)
                precio_total += costo_juego  # Aumentar el precio total antes de aplicar descuento del juego

            # Selección del juego
            print("Seleccione un juego:")
            print("1. Tres en Raya")
            print("2. Ahorcado")
            seleccion_juego = int(input())

            if seleccion_juego == 1:
                gano_juego = Funcionalidad3.tres_en_raya()
            elif seleccion_juego == 2:
                gano_juego = Funcionalidad3.ahorcado()

            if gano_juego:
                print("¡Felicidades! Ha ganado un descuento adicional del 10%.")
                precio_con_descuento *= 0.9  # Aplicar descuento adicional del juego
            else:
                print("Lo sentimos, no ha ganado el juego.")

        # Imprimir factura con descuento adicional si ganó el juego
        print(carrito.generar_detalles_factura(descuento_membresia, gano_juego))

        # Confirmar si el cliente desea pagar la factura
        print("¿Desea pagar la factura?")
        print("1. Sí")
        print("2. No")
        opcion_pago = int(input())

        if opcion_pago == 2:
            print("Ha decidido no pagar la factura. Regresando a la tienda...")
            cliente.set_tienda(None)
            cliente.set_carrito(None)  # Desasignar carrito del cliente
            caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
            carrito.set_caja(None) # Desasignar cliente de la caja
            return
        elif opcion_pago == 1:
            # Verificar si el cliente tiene suficiente saldo
            precio_final = precio_con_descuento  # Usar el precio con descuento
            if cliente.get_dinero() < precio_final:
                print("No tiene suficiente saldo para pagar la factura. Regresando a la tienda...")
                cliente.set_tienda(None)
                cliente.set_carrito(None)  # Desasignar carrito del cliente
                caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
                carrito.set_caja(None)  # Desasignar cliente de la caja
                return

            # Marcar la factura como pagada
            carrito.set_pagado(True)
            cliente.get_facturas().append(carrito)  # Registrar la factura en las facturas del cliente

            # Actualizar saldo de la tienda
            cliente.get_tienda().subir_saldo(precio_final)

            # Restar el monto al saldo del cliente
            cliente.bajar_dinero(precio_final + costo_juego)

            # Calcular y descontar el pago del cajero
            cajero = caja_seleccionada.get_cajero()
            pago_cajero = 20000  # Pago inicial
            if cajero.get_prestacion_pension():
                pago_cajero += 5000
            if cajero.get_prestacion_salud():
                pago_cajero += 5000
            cliente.get_tienda().bajar_saldo(pago_cajero)

            # Desasignar referencias
            cliente.set_tienda(None)
            cliente.set_carrito(None)  # Desasignar carrito del cliente
            caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
            carrito.set_caja(None)  # Desasignar caja del carrito

            print("La factura ha sido pagada exitosamente.")
            Main.escoger_funcionalidad()

    @staticmethod
    def tres_en_raya():
        from uiMain.main import Main
        from gestorAplicacion.servicios.tresEnRaya import TresEnRaya
        # Juego de Tres en Raya
        juego_tres_en_raya = TresEnRaya()
        juego_tres_en_raya.iniciar()

        while not juego_tres_en_raya.ha_ganado() and not juego_tres_en_raya.ha_perdido():
            print(juego_tres_en_raya.obtener_estado())
            print("Elige una posición (1-9): ")
            posicion= Main.escaner_con_rango(9)

            if not juego_tres_en_raya.jugar(posicion):
                print("Posición inválida. Intenta de nuevo.")
                continue

        print(juego_tres_en_raya.obtener_estado())
        if juego_tres_en_raya.ha_ganado():
            print("¡Ganaste!")
            return True
        else:
            print("¡Perdiste!")
            return False

    @staticmethod
    def ahorcado():
        from gestorAplicacion.servicios.ahorcado import Ahorcado
        juego_ahorcado = Ahorcado("java")

        while not juego_ahorcado.ha_ganado() and not juego_ahorcado.ha_perdido():
            print(juego_ahorcado.obtener_estado())
            letra = input("Introduce una letra: ").lower()
            juego_ahorcado.jugar(letra)

        print(juego_ahorcado.obtener_estado())
        if juego_ahorcado.ha_ganado():
            print("¡Ganaste!")
            return True
        else:
            print("¡Perdiste!")
            return False"""