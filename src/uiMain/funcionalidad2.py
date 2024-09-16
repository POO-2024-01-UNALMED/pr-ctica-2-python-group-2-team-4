import math
from tkinter import *
from tkinter import messagebox, simpledialog

from uiMain.fieldFrame import FieldFrame


class Funcionalidad2:
    def __init__(self):
        pass

    @classmethod
    def imprimir_producto(cls,mayorn, mayorm, mayorp, mayorc, cantidad, producto):
        nombre = producto.getNombre().ljust(mayorn)
        marca_tamano = f"{producto.getMarca()} {producto.getTamano()}".ljust(mayorm)
        precio = f"{producto.getPrecio():.2f}".rjust(mayorp)
        return f"{nombre} | {marca_tamano} | {precio} | {cantidad}"

    @staticmethod
    def cuadricula_productos(cliente, productos, inferior, superior):
        from main import Main
        # Llamada a la función lineas()
        Main.lineas()

        mayor_n = 0
        mayor_m = 0
        mayor_p = 0

        # Determinar los tamaños máximos para el formato
        for p in productos[inferior:superior]:
            if p.get_nombre():
                mayor_n = max(mayor_n, len(p.get_nombre()))

            if p.get_marca():
                if p.get_tamano():
                    mayor_m = max(mayor_m, len(p.get_marca()) + len(p.get_tamano().get_tamano()) + 1)
                mayor_m = max(mayor_m, len(p.get_marca()))

            mayor_p = max(mayor_p, len(str(p.get_precio())))

        mayor_n = max(mayor_n, 6)
        mayor_m = max(mayor_m, 12)
        mayor_p = max(mayor_p, 6)
        mayor_c = 8

        # Imprimir líneas horizontales superiores
        print("-" * (mayor_m + mayor_n + mayor_p + 30))

        # Encabezados de la tabla
        header = "{:<{n_width}} |  {:<{m_width}} |  {:<{p_width}} |  {:<{c_width}} |".format(
            "Nombre", "Marca/Tamaño", "Precio", "Cantidad",
            n_width=mayor_n, m_width=mayor_m, p_width=mayor_p, c_width=mayor_c
        )
        print("    " + header)

        print("-" * (mayor_m + mayor_n + mayor_p + 30))

        # Imprimir productos en la tabla
        contador = 1
        for p in productos[inferior:superior]:
            cantidad = cliente.get_tienda().cantidad_producto(p)
            product_line = "{:<{n_width}} |  {:<{m_width}} |  {:<{p_width}} |  {:<{c_width}} |".format(
                p.get_nombre(), f"{p.get_marca()} {p.get_tamano().get_tamano() if p.get_tamano() else ''}",
                str(p.get_precio()), str(cantidad),
                n_width=mayor_n, m_width=mayor_m, p_width=mayor_p, c_width=mayor_c
            )
            print(f"{contador}. {product_line}")
            contador += 1

        # Imprimir líneas horizontales inferiores
        print("-" * (mayor_m + mayor_n + mayor_p + 30))
        print("")

        # Imprimir opciones al final
        print(" 1/2/3/4/Texto. ¿Desea alguno de estos productos? Si es así, elíjalo")
        print(" 5. Si desea volver, escriba 5")

        if superior > 4:
            print(" [A] pag. Si desea imprimir los 4 productos anteriores, escriba A")

        if len(productos) - superior > 0:
            print(" [S] pag. Si desea imprimir los 4 próximos productos, escriba S")

        print("")

    def impresion_seleccion_categoria(self, cliente, productos, categoria, mal_seleccionado, window):
        inferior = 0
        superior = 4
        seleccionado = None

        while True:
            if (len(productos) - superior) < 0:
                superior = len(productos)

            if not mal_seleccionado:
                self.cuadricula_productos(cliente,productos, inferior, superior)

            seleccion = input("Seleccione una opción: ").strip()
            seleccionado = None
            mal_seleccionado = False
            texto = False

            try:
                numero = int(seleccion)
            except ValueError:
                texto = True

            if texto:
                for k in productos:
                    if k.get_nombre().lower() == seleccion.lower():
                        seleccionado = k
                        break

                if seleccion.lower() == "s":
                    inferior = superior
                    superior += 4
                    continue
                if seleccion.lower() == "a":
                    superior = inferior
                    inferior -= 4
                    continue

                if seleccionado is None:
                    print("")
                    print("Este producto no se encuentra:")
                    print(" 1. Desea copiar otra opcion")
                    print(" 2. Desea mirar si puede pedir reabastecer el producto")
                    print("Escoja una opción: ")
                    mal_seleccionado = True
                    continue
            else:
                if 1 <= numero <= 4:
                    if numero + inferior - 1 < len(productos):
                        seleccionado = productos[numero + inferior - 1]
                    else:
                        print("Ese número está fuera del rango")
                        mal_seleccionado = True
                        continue
                elif numero == 5:
                    self.busqueda_categoria(cliente,window)
                    return None
                else:
                    print("Ese número está fuera del rango")
                    mal_seleccionado = True
                    continue

            if seleccionado is not None:
                return seleccionado

    def impresion_seleccion_nombre(self, cliente, productos, seleccionado,window):
        inferior = 0
        superior = 4
        mal_seleccionado = False

        while True:
            if (len(productos) - superior) < 0:
                superior = superior - (superior - len(productos))

            if not mal_seleccionado:
                self.cuadricula_productos(cliente, productos, inferior, superior)  # Llamada a cuadricula_productos()

            mal_seleccionado = False
            seleccion = input()

            try:
                numero = int(seleccion)
                texto = False
            except ValueError:
                texto = True

            if texto:
                for k in productos:
                    if k.get_nombre().lower() == seleccion.lower():  # Llamada a get_nombre()
                        seleccionado = k

                if seleccion.lower() == "s":
                    inferior = superior
                    superior += 4
                    continue

                if seleccion.lower() == "a":
                    superior = inferior
                    inferior = superior - 4
                    continue

                if seleccionado is None:
                    print("\nEste producto no se encuentra, escriba otro o seleccione otra opción:")
                    mal_seleccionado = True
                    continue

            else:
                if numero in [1, 2, 3, 4]:
                    seleccionado = productos[numero + inferior - 1]
                elif numero == 5:
                    self.busqueda_nombre(cliente, window)  # Llamada a busqueda_nombre()

            return seleccionado

    def busqueda_categoria(self, cliente, window):
        # Limpieza de cualquier mensaje previo en la ventana
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()

        # Recolectar y mostrar las categorías disponibles
        from gestorAplicacion.servicios.enums import Categoria

        # Crear el marco para las categorías
        categorias_frame = Frame(window, bg="light blue")
        categorias_frame.pack(pady=10, fill=BOTH, expand=True)

        Label(categorias_frame, text="Estas son las categorías de los productos de nuestras tiendas:",
              font=("Arial", 16), bg="light blue").pack(pady=10)

        # Crear un marco adicional para centrar los botones
        botones_frame = Frame(categorias_frame, bg="light blue")
        botones_frame.pack(pady=10, fill=BOTH, expand=True)

        enumerado = 1
        categoria_dict = {}
        for tipo in Categoria:
            categoria_dict[enumerado] = tipo
            Button(botones_frame, text=f"{enumerado}. {tipo.get_texto()}",
                   font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                   width=35, command=lambda cat=tipo: self.mostrar_productos_por_categoria(cliente, cat, window)).pack(
                pady=5, anchor=CENTER)
            enumerado += 1

        # Añadir la opción de buscar por nombre
        Button(botones_frame, text=f"{enumerado}. Volver",
               font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
               width=35, command=lambda: self.elegir_tipo_busqueda(cliente, window)).pack(pady=5, anchor=CENTER)

        # Entrada para seleccionar la categoría
        Label(categorias_frame, text="O ingrese el número de la categoría que desea buscar:",
              font=("Arial", 12), bg="light blue").pack(pady=10)

        seleccion_entry = Entry(categorias_frame, font=("Arial", 12))
        seleccion_entry.pack(pady=10)

        def confirmar_seleccion_categoria():
            try:
                seleccion = int(seleccion_entry.get().strip())
                if seleccion == enumerado:
                    self.elegir_tipo_busqueda(cliente, window)
                    return
                if seleccion in categoria_dict:
                    categoria = categoria_dict[seleccion]
                    self.mostrar_productos_por_categoria(cliente, categoria, window)
                else:
                    Label(categorias_frame, text="Selección inválida. Inténtelo de nuevo.",
                          font=("Arial", 12), bg="light red", fg="black").pack(pady=10)
            except ValueError:
                Label(categorias_frame, text="Debe ingresar un número.",
                      font=("Arial", 12), bg="light red", fg="black").pack(pady=10)

        Button(categorias_frame, text="Confirmar", command=confirmar_seleccion_categoria,
               font=("Arial", 12), bg="#00FF00", fg="black").pack(pady=10)

    def mostrar_productos_por_categoria(self, cliente, categoria, window, page=1):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        productos = cliente.get_tienda().buscar_productos(categoria)

        # Mostrar productos encontrados
        productos_frame = Frame(window, bg="light blue")
        productos_frame.pack(pady=10, fill=BOTH, expand=True)

        if not productos:
            Label(productos_frame,
                  text="No hay productos disponibles en esta categoría.",
                  font=("Arial", 12), bg="light blue").pack(pady=10)
            Button(productos_frame, text="Volver a Categorías",
                   font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                   width=35, command=lambda: self.busqueda_categoria(cliente, window)).pack(pady=10, anchor=CENTER)
            return

        Label(productos_frame, text=f"Productos en la categoría {categoria.get_texto()}:",
              font=("Arial", 16), bg="light blue").pack(pady=10)

        # Definir número de productos por página
        productos_por_pagina = 4
        total_paginas = math.ceil(len(productos) / productos_por_pagina)
        productos = productos[(page - 1) * productos_por_pagina: page * productos_por_pagina]

        botones_frame = Frame(productos_frame, bg="light blue")
        botones_frame.pack(pady=10, fill=BOTH, expand=True)

        for i, producto in enumerate(productos):
            Button(botones_frame,
                   text=f"{i + 1}. {producto.get_nombre()} - {producto.get_marca()} - ${producto.get_precio():.2f}",
                   font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                   width=35, command=lambda prod=producto: self.seleccionar_producto(cliente, prod, window)).pack(pady=5,
                                                                                                             anchor=CENTER)

        # Controles de paginación
        paginacion_frame = Frame(productos_frame, bg="light blue")
        paginacion_frame.pack(pady=10)

        # Botones de paginación
        if page > 1:
            Button(paginacion_frame, text="Anterior", font=("Arial", 12), bg="#00FF00", fg="black",
                   command=lambda: self.mostrar_productos_por_categoria(cliente, categoria, window, page - 1)).pack(
                side="left", padx=5)

        if page < total_paginas:
            Button(paginacion_frame, text="Siguiente", font=("Arial", 12), bg="#00FF00", fg="black",
                   command=lambda: self.mostrar_productos_por_categoria(cliente, categoria, window, page + 1)).pack(
                side="right", padx=5)

        Button(productos_frame, text="Volver", font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
               width=35, command=lambda: self.busqueda_categoria(cliente, window)).pack(pady=10, anchor=CENTER)

    def seleccionar_producto(self, cliente, producto, window):
        cantidad = simpledialog.askinteger("Cantidad", "¿Cuántos productos de este quiere usted?",
                                           minvalue=1, parent=window)

        if cantidad is None:
            return  # El usuario canceló el diálogo

        # Agregar el producto al carrito y obtener el resultado como una cadena
        resultado = cliente.get_carrito().agregar_al_carrito(producto, cantidad)

        if "no tienes dinero" in resultado:
            self.mostrar_productos_recomendados(producto, cliente, window)
        elif "Productos no agregados" in resultado and "productos suficientes" in resultado:
            self.mostrar_decision_rapida(producto, cliente, window)
        else:
            messagebox.showinfo("Resultado", resultado)
            self.elegir_tipo_busqueda(cliente, window)

    def mostrar_productos_recomendados(self, seleccionado, cliente, window):
        productos_recomendados = cliente.get_tienda().recomendar_productos(seleccionado, cliente)

        if not productos_recomendados:
            messagebox.showinfo("Recomendación",
                                "No se encontraron productos recomendados. Volviendo a funcionalidad 2.")
            self.elegir_tipo_busqueda(cliente, window)
            return

        recomendacion_window = Toplevel(window)
        recomendacion_window.title("Productos Recomendados")

        for i, producto in enumerate(productos_recomendados):
            Button(recomendacion_window,
                   text=f"{i + 1}. {producto.get_nombre()} - {producto.get_marca()} - ${producto.get_precio():.2f}",
                   font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                   width=35,
                   command=lambda prod=producto: self.seleccionar_producto(cliente, prod, recomendacion_window)).pack(pady=5,
                                                                                                                 anchor=CENTER)

        Button(recomendacion_window, text="Volver",
               font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
               width=35, command=lambda: recomendacion_window.destroy()).pack(pady=10, anchor=CENTER)

    def mostrar_decision_rapida(self, seleccionado, cliente, window):
        decision_window = Toplevel(window)
        decision_window.title("Decisión Rápida")

        Label(decision_window,
              text="¿Desea recibir la cantidad de productos que tenemos o desea escoger otro producto?",
              font=("Arial", 12), bg="light blue").pack(pady=10)

        def decision1():
            cliente.get_carrito().agregar_al_carrito(seleccionado, seleccionado.cantidad_producto())
            decision_window.destroy()
            self.elegir_tipo_busqueda(cliente, window)

        def decision2():
            decision_window.destroy()
            self.elegir_tipo_busqueda(cliente, window)

        Button(decision_window, text="Recibir la cantidad que tienen", command=decision1,
               font=("Arial", 12), bg="#00FF00", fg="black").pack(pady=5)

        Button(decision_window, text="Escoger otro producto", command=decision2,
               font=("Arial", 12), bg="#FF0000", fg="white").pack(pady=5)
    """productos=""
        for pasillo in cliente.get_tienda().get_pasillos():
            for producto in pasillo.get_productos():
                productos+= producto.get_nombre()+", "
        print(productos)
        productos = []
        seleccionado = None
        from main import Main
        from gestorAplicacion.servicios.enums import Categoria
        Main.lineas()
        print("Estas son las categorías de los productos de nuestras tiendas:\n")

        enumerado = 1
        for tipo in Categoria:
            print(f" {enumerado}. {tipo.get_texto()}")
            enumerado += 1

        print(f" {enumerado}. Volver\n")

        decision_categoria = Main.escaner_con_rango(enumerado)

        if decision_categoria == enumerado:
            self.elegir_tipo_busqueda(cliente)

        categoria = Categoria.resolver_enum(decision_categoria)

        productos = cliente.get_tienda().buscar_productos(categoria)

        while len(productos) == 0:
            print("No hay productos disponibles de esa categoría, escoja otra por favor.")
            decision_categoria = Main.escaner_con_rango(enumerado)

            if decision_categoria == enumerado:
                self.elegir_tipo_busqueda(cliente)

            categoria = Categoria.resolver_enum(decision_categoria)
            productos = cliente.get_tienda().buscar_productos(categoria)

        mal_seleccionado = False

        seleccionado = self.impresion_seleccion_categoria(cliente, productos, categoria, mal_seleccionado)

        Main.lineas()
        self.donde_se_agregan_productos(cliente, seleccionado)"""

    def busqueda_nombre(self, cliente, window):
        def buscar():
            widgets = window.winfo_children()
            for i, widget in enumerate(widgets):
                if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                    widget.destroy()

            frame1 = Frame(window, bg="light blue")
            frame1.pack(fill=BOTH, expand=True)

            # Añadir los Entry y Labels
            frame_entries = Frame(frame1, bg="light blue")
            frame_entries.pack(pady=10, fill=X, padx=10)

            label_seleccion = Label(frame_entries, text="Nombre del Producto:", font=("Arial", 12), bg="light blue")
            label_seleccion.pack(side="top", padx=5)

            entry_seleccion = Entry(frame_entries, font=("Arial", 12))
            entry_seleccion.pack(side="top", pady=5)

            def on_buscar():
                nombre = entry_seleccion.get()
                if not nombre:
                    mostrar_error(frame1, "Debe ingresar un nombre para buscar.")
                    return

                productos = buscar_productos_por_nombre(nombre)
                if not productos:
                    mostrar_error(frame1, "No se encontraron productos con ese nombre.")
                    return

                actualizar_mostrar_productos(frame1, productos, 0, 4)

            boton_buscar = Button(frame1, text="Buscar",
                                  command=on_buscar,
                                  font=("Arial", 12), bg="#00FF00", fg="black")
            boton_buscar.pack(pady=10)

        def buscar_productos_por_nombre(nombre):
            # Buscar productos por coincidencia parcial (insensible a mayúsculas/minúsculas)
            productos = cliente.get_tienda().buscar_productos_por_nombre(nombre)
            return [p for p in productos if nombre.lower() in p.get_nombre().lower()]

        def mostrar_error(frame, mensaje):
            # Limpiar errores anteriores
            for widget in frame.winfo_children():
                if hasattr(widget, 'error_widget') and widget.error_widget:
                    widget.destroy()

            label_error = Label(frame, text=mensaje, font=("Arial", 12), fg="red", bg="light blue", borderwidth=2,
                                relief="solid")
            label_error.pack(pady=5, padx=10)

        def mostrar_confirmacion(mensaje):
            # Mostrar una ventana emergente con un mensaje de confirmación
            messagebox.showinfo("Confirmación", mensaje)

        def actualizar_mostrar_productos(frame1, productos, inferior, superior, p=None):
            # Limpiar los widgets existentes en el frame
            superiors=superior
            for widget in frame1.winfo_children():
                widget.destroy()

            label_instrucciones = Label(frame1, text="Estas son las opciones de búsqueda por nombre:",
                                        font=("Arial", 16, "bold"), bg="light blue")
            label_instrucciones.pack(pady=10)

            # Mostrar los productos
            if superior>len(productos):
                superiors=len(productos)-1

            self.producto_seleccionado=None
            def seleccionar_producto(producto, entry_producto):
                # Establecer el producto seleccionado en el Entry correspondiente
                entry_producto.config(state="normal")  # Hacer que el Entry sea editable
                entry_producto.delete(0, END)
                entry_producto.insert(0,
                                      f"{producto.get_nombre()} - {producto.get_marca()} - ${producto.get_precio():.2f}")
                entry_producto.config(state="readonly")  # Hacer que el Entry sea solo lectura
                self.producto_seleccionado=producto

            for i, producto in enumerate(productos[inferior:superior], start=1):
                frame_producto = Frame(frame1, bg="light gray", padx=10, pady=5, borderwidth=2, relief="ridge")
                frame_producto.pack(pady=5, fill=BOTH, expand=True)

                boton_producto = Button(frame_producto,
                                        text=f"{i}. {producto.get_nombre()} - {producto.get_marca()} - ${producto.get_precio():.2f} - Cantidad disponible: {producto.cantidad_producto()}",
                                        font=("Arial", 12, "italic"), bg="light gray", anchor='w',
                                        command=lambda p=producto:seleccionar_producto(p, entry_producto))
                boton_producto.pack(fill=BOTH, expand=True)

            # Controles de paginación
            paginacion_frame = Frame(frame1, bg="light blue")
            paginacion_frame.pack(pady=10, fill=X, padx=20)

            if inferior > 0:
                Button(paginacion_frame, text="Anterior", font=("Arial", 12), bg="#00FF00", fg="black",
                       command=lambda: actualizar_mostrar_productos(frame1, productos, inferior - 4, superior - 4)).pack(side="left", padx=5)

            if superior < len(productos):
                Button(paginacion_frame, text="Siguiente", font=("Arial", 12), bg="#00FF00", fg="black",
                       command=lambda: actualizar_mostrar_productos(frame1, productos, inferior + 4, superior + 4)).pack(
                    side="right", padx=5)

            # Añadir el botón para volver a buscar
            label_producto = Label(frame1, text="Producto Seleccionado:", font=("Arial", 12), bg="light blue")
            label_producto.pack(side="top", padx=5)

            entry_producto = Entry(frame1, font=("Arial", 12), width=60)
            entry_producto.pack(side="top", pady=5)
            entry_producto.config(state="readonly")  # Solo lectura

            label_cantidad = Label(frame1, text="Cantidad Deseada:", font=("Arial", 12), bg="light blue")
            label_cantidad.pack(side="top", padx=5)

            entry_cantidad = Entry(frame1, font=("Arial", 12))
            entry_cantidad.pack(side="top", pady=5)

            boton_agregar = Button(frame1, text="Agregar al carrito",
                                   command=lambda: seleccionar(entry_producto, entry_cantidad,self.producto_seleccionado),
                                   font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15)
            boton_agregar.pack(pady=10, anchor=CENTER)

            Button(frame1, text="Volver a Buscar", font=("Arial", 12), bg="#ADD8E6", padx=30, pady=15,
                   command=lambda: buscar()).pack(pady=10, anchor=CENTER)

        def seleccionar(entry_producto, entry_cantidad,producto):
            # Añade depuración para verificar el estado del widget
            try:
                seleccion = entry_producto.get().strip()
                cantidad=int(entry_cantidad.get())
            except Exception:
                print("Debes llenar ambos espacios")
                return

            self.donde_se_agregan_productos(cliente, producto,cantidad,window)

        buscar()

    @staticmethod
    def ajustar_texto(texto, ancho_celda):
        if len(texto) > ancho_celda:
            return texto[:ancho_celda - 1] + "."
        else:
            return texto

    def donde_se_agregan_productos(self, cliente, seleccionado,cantidad,window):

        # Agregar el producto al carrito y obtener el resultado como una cadena
        resultado = cliente.get_carrito().agregar_al_carrito(seleccionado, cantidad)

        # Verifica si el resultado contiene ciertos mensajes
        if "no tienes dinero" in resultado:
            self.mostrar_productos_recomendados(seleccionado,cliente, window)
        elif "Productos no agregados" in resultado and "productos suficientes" in resultado:
            self.mostrar_decision_rapida(seleccionado,cliente, window)
        else:
            messagebox.showinfo("Resultado", resultado)
            self.elegir_tipo_busqueda(cliente,window)


        """print("¿Cuántos productos de este quiere usted?\n")
        cantidad = Main.escaner()

        # Agrega el producto al carrito y obtiene el resultado como una cadena
        resultado = cliente.get_carrito().agregar_al_carrito(seleccionado, cantidad)
        print(f"\n{resultado}\n")

        # Verifica si el resultado contiene ciertos mensajes
        contiene_productos_no_agregados = "Productos no agregados" in resultado
        contiene_productos_suficientes = "productos suficientes" in resultado
        contiene_no_tienes_dinero = "no tienes dinero" in resultado

        if contiene_no_tienes_dinero:
            productos_recomendados = cliente.get_tienda().recomendar_productos(seleccionado, cliente)
            if not productos_recomendados:
                print("No se encontraron productos recomendados.")
                print("Volviendo a funcionalidad 2")
                self.elegir_tipo_busqueda(cliente)

            # Imprimir encabezado de la tabla
            print("+----+--------------------+---------------+----------+----------+-----------+")
            print("| No | Nombre             | Marca         | Precio   | Categoría| Descripción")
            print("+----+--------------------+---------------+----------+----------+-----------+")

            # Imprimir cada producto en la tabla
            for i, producto in enumerate(productos_recomendados):
                nombre_producto = producto.get_nombre()
                marca_producto = producto.get_marca()
                precio_producto = f"{producto.get_precio():.2f}"  # Precio formateado a dos decimales
                categoria_producto = producto.get_categoria().get_texto()
                descripcion_producto = producto.get_descripcion()

                # Imprimir la fila de la tabla
                print(
                    f"| {i + 1:<2} | {self.ajustar_texto(nombre_producto, 18):<18} | {self.ajustar_texto(marca_producto, 13):<13} | "
                    f"{self.ajustar_texto(precio_producto, 8):<8} | {self.ajustar_texto(categoria_producto, 8):<8} | "
                    f"{self.ajustar_texto(descripcion_producto, 10):<10} |")

            # Imprimir línea final de la tabla
            print("+----+--------------------+---------------+----------+----------+-----------+")
            seleccion = int(input("Seleccione el número del producto que desea agregar al carrito: "))

            if 0 < seleccion <= len(productos_recomendados):
                producto_seleccionado = productos_recomendados[seleccion - 1]
                cantidad = 1
                if cantidad > 0:
                    resultado = cliente.get_carrito().agregar_al_carrito(producto_seleccionado, cantidad)
                    print(resultado)
                else:
                    print("Cantidad no válida.")
            else:
                print("Selección inválida.")

        elif contiene_productos_no_agregados and contiene_productos_suficientes:
            print("¿Desea recibir la cantidad de productos que tenemos o desea mejor escoger otro?")
            print("1. Recibir la cantidad que tienen")
            print("2. Escoger otro producto nuevamente")
            decision = Main.escaner_con_rango(2)

            if decision == 1:
                cliente.get_carrito().agregar_al_carrito(seleccionado, seleccionado.cantidad_producto())
            elif decision == 2:
                self.elegir_tipo_busqueda(cliente)

        self.elegir_tipo_busqueda(cliente)"""

    @staticmethod
    def redirigir_funcionalidad1(window):
        from main import Main
        Main.escoger_funcionalidad()

    @staticmethod
    def descartar_compra(cliente,window):
        carrito = cliente.get_carrito()
        tienda = cliente.get_tienda()

        for producto in carrito.get_productos():
            for pasillo in tienda.get_pasillos():  # Implementar métodos en clases Pasillo y Tienda
                if pasillo.get_categoria() == producto.get_categoria():
                    pasillo.get_productos().append(producto)  # Implementar método en clase Pasillo
                    break

        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                widget.destroy()

        frame = Frame(window, bg="light blue", padx=20, pady=20)
        frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Etiqueta con mensaje en un cuadro de fondo
        mensaje_frame = Frame(frame, bg="white", padx=20, pady=20, relief=RAISED, borderwidth=2)
        mensaje_frame.pack(expand=True, fill=BOTH)

        mensaje = Label(mensaje_frame, text="Tu compra fue descartada con éxito.\n"
                                               "Selecciona otra funcionalidad o dale al botón para ir a la Funcionalidad 1 y volver a empezar la compra.",
                           font=("Arial", 14, "bold"), bg="white", wraplength=350, justify=CENTER)
        mensaje.pack(pady=10)

        # Botón para ir a la Funcionalidad 1
        boton_ir_funcionalidad1 = Button(frame, text="Ir a la Funcionalidad 1",
                                            font=("Arial", 14, "bold"), command=lambda: Funcionalidad2.redirigir_funcionalidad1(window),
                                            bg="light green", fg="black", relief=RAISED, padx=10, pady=5)
        boton_ir_funcionalidad1.pack(pady=20)

        # Centrar el botón
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        carrito.get_productos().clear()
        print(
            "Se han descartado todos los productos del carrito y se han devuelto a los pasillos correspondientes.")
        cliente.set_tienda(None)
        cliente.set_carrito(None)

    def mostrar_carrito(self, cliente, window):
        def actualizar_productos(frame_productos, productos_map, productos_cantidad):
            for widget in frame_productos.winfo_children():
                widget.destroy()

            # Encabezado de la tabla
            encabezado = Label(frame_productos, text="| No | Nombre             | Marca         | Tamaño   | Precio   | Cantidad |", font=("Arial", 12))
            encabezado.pack()

            # Imprimir los productos sin duplicados con la cantidad total
            contador = 1
            for id_producto, producto in productos_map.items():
                cantidad_total = productos_cantidad[id_producto]

                nombre_producto = producto.get_nombre()
                marca_producto = producto.get_marca()
                tamano_producto = producto.get_tamano().get_tamano()
                precio_producto = f"{producto.get_precio():.2f}"  # Precio formateado a dos decimales

                # Imprimir cada producto en la tabla
                producto_info = Label(frame_productos, text=f"| {contador:<2} | {nombre_producto:<18} | {marca_producto:<13} | {tamano_producto:<8} | {precio_producto:<8} | {cantidad_total:<8} |", font=("Arial", 10))
                producto_info.pack()
                contador += 1

        def eliminar_producto(id_producto, frame_productos, productos_map, productos_cantidad):
            producto_seleccionado = productos_map[id_producto]
            cantidad_actual = cliente.get_carrito().contar_repeticiones(producto_seleccionado)

            cantidad_eliminar = simpledialog.askinteger("Eliminar Producto", f"Ingrese la cantidad a eliminar (máximo {cantidad_actual}):", minvalue=1, maxvalue=cantidad_actual)
            if cantidad_eliminar is not None and 0 < cantidad_eliminar <= cantidad_actual:
                cliente.get_carrito().eliminar_productos(producto_seleccionado, cantidad_eliminar)
                messagebox.showinfo("Éxito", "Productos actualizados en el carrito.")
                actualizar_productos(frame_productos, productos_map, productos_cantidad)
            else:
                messagebox.showerror("Error", "Cantidad inválida.")

        # Limpiar la ventana
        for widget in window.winfo_children():
            widget.destroy()

        frame = Frame(window)
        frame.pack(fill=BOTH, expand=True)

        productos = cliente.get_carrito().get_productos()

        if len(productos) == 0:
            messagebox.showinfo("Carrito Vacío", "Usted no puede seleccionar esta opción")
            self.elegir_tipo_busqueda(cliente, window)
            return

        productos_cantidad = {}
        productos_map = {}

        for producto in productos:
            id_producto = producto.get_id()
            productos_map[id_producto] = producto  # Guardar referencia del producto
            productos_cantidad[id_producto] = productos_cantidad.get(id_producto, 0) + 1

        frame_productos = Frame(frame)
        frame_productos.pack(fill=BOTH, expand=True)

        actualizar_productos(frame_productos, productos_map, productos_cantidad)

        def seleccionar_producto():
            seleccion = simpledialog.askinteger("Seleccionar Producto", "Seleccione el número del producto que desea eliminar del carrito:")
            if seleccion is not None and 1 <= seleccion <= len(productos_map):
                id_producto = list(productos_map.keys())[seleccion - 1]
                eliminar_producto(id_producto, frame_productos, productos_map, productos_cantidad)
            else:
                messagebox.showerror("Error", "Selección inválida.")

        boton_seleccionar = Button(frame, text="Seleccionar Producto", command=seleccionar_producto)
        boton_seleccionar.pack(pady=10)

        boton_volver = Button(frame, text="Volver", command=lambda: self.elegir_tipo_busqueda(cliente, window))
        boton_volver.pack(pady=10)

    def elegir_tipo_busqueda(self,cliente,window):
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                widget.destroy()
        frame=FieldFrame(window,"La búsqueda de nuestra tienda es"+" lo más accesible para nuestros clientes. ¿Que desea hacer?",[],"Escoja uno de los botones",[],[],"Funcionalidad2","La funcionalidad se basas en darle la posibilidad al cliente de interactuar"+" con los productos de la tienda y con su carrito asociado"+"permitiendo agregar o eliminar productos, ademas de poder guardar la factura de la compra",False)
        boton1=Button(frame.campos,text="Buscar productos por categoría",command= lambda:self.busqueda_categoria(cliente,window))
        boton2=Button(frame.campos,text="Buscar productos por nombre",command= lambda:self.busqueda_nombre(cliente,window))
        boton1.grid(row=1,column=1)
        boton2.grid(row=1,column=2)
        frame.pack(fill=BOTH, expand=True)
        tienda = cliente.get_tienda()

        # Botón para descartar compra
        boton4 = Button(frame.campos, text="Volver y descartar compra", command= lambda:self.descartar_compra(cliente,window))
        boton4.grid(row=2, column=2)

        if len(cliente.get_carrito().get_productos()) > 0:
            boton3 = Button(frame.campos, text="Eliminar un producto de mi carrito",command= lambda:self.mostrar_carrito(cliente,window))
            boton3.grid(row=2, column=1)

        # Botón para guardar carrito como factura
        if len(cliente.get_carrito().get_productos()) > 0:
            boton5 = Button(frame.campos, text="Guardar carrito como factura")
            boton5.grid(row=3, column=1)

        # Mostrar el monto actual
        monto_actual = sum([producto.get_precio() for producto in cliente.get_carrito().get_productos()])
        label_monto = Label(frame.campos,
                            text=f"Recuerde que el monto que le queda para gastar es {cliente.get_dinero() - monto_actual}$")
        label_monto.grid(row=4, column=1, columnspan=2)

        frame.pack(fill=BOTH, expand=True)

        """if tienda is None:
            #Main.lineas()  # Implementar este método
            print("Debería seleccionar una tienda primero, diríjase a la funcionalidad 1")
            print("1. Ir a la funcionalidad 1")
            print("2. Ver el menú para escoger otra funcionalidad")
            decision = input()  # Implementar este método
            if decision == 1:
                p=2#Funcionalidad1.consultas_eco()  # Implementar este método en Funcionalidad1
            elif decision == 2:
                p=2#Main.escoger_funcionalidad()  # Implementar este método en Main
            return

        #Main.lineas()  # Implementar este método
        print("La búsqueda de nuestra tienda es lo más accesible para nuestros clientes. ¿Desea buscar por"
              "\n" + "una categoría o por nombre del producto?")
        print("")
        print(" 1. Por categoría de un producto")
        print(" 2. Por nombre del producto")
        if len(cliente.get_carrito().get_productos()) > 0:
            print(" 3. Eliminar un producto de mi carrito")
        print(" 4. Volver y descartar compra")
        if len(cliente.get_carrito().get_productos()) > 0:
            print(" 5. Guardar carrito como factura")
        print("")

        monto_actual = sum([producto.get_precio() for producto in cliente.get_carrito().get_productos()])
        print(f"Recuerde que el monto que le queda para gastar es {cliente.get_dinero() - monto_actual}$")
        print("")

        decision = 2#Main.escaner_con_rango(5)  # Implementar este método

        if decision == 1:
            self.busqueda_categoria(cliente)  # Implementar este método
        elif decision == 2:
            self.busqueda_nombre(cliente)  # Implementar este método
        elif decision == 3:
            if len(cliente.get_carrito().get_productos()) == 0:
                #Main.lineas()
                print("Usted no puede seleccionar esta opción")
                self.elegir_tipo_busqueda(cliente)
                return

            #Main.lineas()
            print("Estos son los productos de su carrito: \n")

            productos = cliente.get_carrito().get_productos()

            ancho_celda_nombre = 20
            ancho_celda_marca = 15
            ancho_celda_tamano = 10
            ancho_celda_precio = 10
            ancho_celda_cantidad = 10

            # Encabezado de la tabla
            print("+----+--------------------+---------------+----------+----------+----------+")
            print("| No | Nombre             | Marca         | Tamaño   | Precio   | Cantidad |")
            print("+----+--------------------+---------------+----------+----------+----------+")

            # Diccionarios para almacenar los productos y sus cantidades sumadas
            productos_cantidad = {}
            productos_map = {}

            # Sumar cantidades de productos iguales
            for producto in cliente.get_carrito().get_productos():
                id_producto = producto.get_id()
                productos_map[id_producto] = producto  # Guardar referencia del producto
                productos_cantidad[id_producto] = productos_cantidad.get(id_producto, 0) + 1

            # Imprimir los productos sin duplicados con la cantidad total
            contador = 1
            for id_producto, producto in productos_map.items():
                cantidad_total = productos_cantidad[id_producto]

                nombre_producto = producto.get_nombre()
                marca_producto = producto.get_marca()
                tamano_producto = producto.get_tamano().get_tamano()
                precio_producto = f"{producto.get_precio():.2f}"  # Precio formateado a dos decimales

                # Imprimir cada producto en la tabla
                print(
                    f"| {contador:<2} | {nombre_producto:<18} | {marca_producto:<13} | {tamano_producto:<8} | {precio_producto:<8} | {cantidad_total:<8} |")
                contador += 1

            # Pie de la tabla
            print("+----+--------------------+---------------+----------+----------+----------+")
            print("\nSeleccione el número del producto que desea eliminar del carrito:")
            print(f"{contador}. Cancelar borrar producto del carrito")
            seleccion = int(input("Seleccione una opción: "))

            if seleccion == contador:
                self.elegir_tipo_busqueda(cliente)
                return

            if 1 <= seleccion <= len(productos_map):
                # Buscar el producto seleccionado en la lista impresa
                productos_impresos = set()
                producto_seleccionado = None
                index = 0

                for producto in cliente.get_carrito().get_productos():
                    if producto.get_id() not in productos_impresos:
                        productos_impresos.add(producto.get_id())
                        index += 1

                    if index == seleccion:
                        producto_seleccionado = producto
                        break

                if producto_seleccionado is not None:
                    print("\nIngrese la cantidad que desea eliminar: ")
                    cantidad_eliminar = int(input())

                    cantidad_actual = cliente.get_carrito().contar_repeticiones(producto_seleccionado)
                    if 0 < cantidad_eliminar <= cantidad_actual:
                        cliente.get_carrito().eliminar_productos(producto_seleccionado, cantidad_eliminar)
                        #Main.lineas()
                        print("Productos actualizados en el carrito:\n")

                        # Encabezado de la tabla
                        print("+----+--------------------+---------------+----------+----------+----------+")
                        print("| No | Nombre             | Marca         | Tamaño   | Precio   | Cantidad |")
                        print("+----+--------------------+---------------+----------+----------+----------+")

                        # Imprimir productos actualizados sin duplicados
                        productos_impresos.clear()
                        contador = 1

                        for producto in cliente.get_carrito().get_productos():
                            if producto.get_id() in productos_impresos:
                                continue

                            nombre_producto = producto.get_nombre()
                            marca_producto = producto.get_marca()
                            tamano_producto = producto.get_tamano().get_tamano()
                            precio_producto = f"{producto.get_precio():.2f}"
                            cantidad_producto = cliente.get_carrito().contar_repeticiones(producto)

                            print(
                                f"| {contador:<2} | {nombre_producto:<18} | {marca_producto:<13} | {tamano_producto:<8} | {precio_producto:<8} | {cantidad_producto:<8} |")
                            productos_impresos.add(producto.get_id())
                            contador += 1
                    else:
                        print("Cantidad inválida.")
                else:
                    print("Producto seleccionado no encontrado.")
            else:
                print("Selección inválida.")

            print("+----+--------------------+---------------+----------+----------+----------+")
            self.elegir_tipo_busqueda(cliente)


        elif decision == 4:
            carrito = cliente.get_carrito()
            tienda = cliente.get_tienda()

            for producto in carrito.get_productos():
                for pasillo in tienda.get_pasillos():  # Implementar métodos en clases Pasillo y Tienda
                    if pasillo.get_categoria() == producto.get_categoria():
                        pasillo.get_productos().append(producto)  # Implementar método en clase Pasillo
                        break

            carrito.get_productos().clear()
            print(
                "Se han descartado todos los productos del carrito y se han devuelto a los pasillos correspondientes.")
            cliente.set_tienda(None)
            cliente.set_carrito(None)
            #Main.escoger_funcionalidad()  # Implementar este método en Main

        elif decision == 5:
            if len(cliente.get_carrito().get_productos()) == 0:
                #Main.lineas()  # Implementar este método
                print("Usted no puede seleccionar esta opción")
                self.elegir_tipo_busqueda(cliente)
                return
            cliente.get_tienda().get_facturas().append(cliente.get_carrito())  # Implementar métodos en Tienda y Factura
            cliente.get_facturas().append(cliente.get_carrito())
            cliente.set_carrito(None)
            cliente.set_tienda(None)
            #Main.escoger_funcionalidad()  # Implementar este metodo en Main"""

