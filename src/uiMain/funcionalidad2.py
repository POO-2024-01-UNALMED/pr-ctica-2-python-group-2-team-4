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
        def buscar_productos_por_nombre(nombre):
            # Buscar productos por coincidencia parcial (insensible a mayúsculas/minúsculas)
            productos = cliente.get_tienda().buscar_productos_por_nombre(nombre)
            return [p for p in productos if nombre.lower() in p.get_nombre().lower()]

        def mostrar_error(frame, mensaje):
            # Limpiar errores anteriores
            for widget in frame.winfo_children():
                if widget.cget('fg') == 'red':
                    widget.destroy()

            label_error = Label(frame, text=mensaje, font=("Arial", 12), fg="red", bg="light blue", borderwidth=2,
                                relief="solid")
            label_error.pack(pady=5, padx=10)

        def actualizar_mostrar_productos(frame1, productos, inferior, superior):
            if (len(productos) - superior) < 0:
                superior = len(productos)

            # Limpiar los widgets existentes en el frame
            for widget in frame1.winfo_children():
                widget.destroy()

            label_instrucciones = Label(frame1, text="Estas son las opciones de búsqueda por nombre:",
                                        font=("Arial", 16, "bold"), bg="light blue")
            label_instrucciones.pack(pady=10)

            # Mostrar los productos
            for i, producto in enumerate(productos[inferior:superior], start=1):
                frame_producto = Frame(frame1, bg="light gray", padx=10, pady=5, borderwidth=2, relief="ridge")
                frame_producto.pack(pady=5, fill=BOTH, expand=True)

                boton_producto = Button(frame_producto,
                                        text=f"{i}. {producto.get_nombre()} - {producto.get_marca()} - ${producto.get_precio():.2f}",
                                        font=("Arial", 12, "italic"), bg="light gray", anchor='w',
                                        command=lambda p=producto: seleccionar_producto(p))
                boton_producto.pack(fill=BOTH, expand=True)

            # Mensaje de paginación
            if inferior > 0:
                label_paginacion = Label(frame1,
                                         text="Escriba 'a' para anterior página",
                                         font=("Arial", 12), bg="light blue")
                label_paginacion.pack(pady=5)

            if superior < len(productos):
                label_paginacion = Label(frame1,
                                         text="Escriba 's' para siguiente página",
                                         font=("Arial", 12), bg="light blue")
                label_paginacion.pack(pady=5)

            entry_seleccion = Entry(frame1, font=("Arial", 12))
            entry_seleccion.pack(pady=10)

            def seleccionar():
                nonlocal inferior, superior
                seleccion = entry_seleccion.get().strip()
                seleccionado = None

                try:
                    numero = int(seleccion)
                except ValueError:
                    numero = None  # Usar `None` para representar que no es un número

                if numero is None or numero < 1 or numero > 4:
                    if seleccion.lower() == "s":
                        if superior < len(productos):
                            inferior = superior
                            superior += 4
                            actualizar_mostrar_productos(frame1, productos, inferior, superior)
                        return

                    if seleccion.lower() == "a":
                        if inferior > 0:
                            superior = inferior
                            inferior -= 4
                            if inferior < 0:
                                inferior = 0
                            actualizar_mostrar_productos(frame1, productos, inferior, superior)
                        return

                    productos_busqueda = buscar_productos_por_nombre(seleccion)
                    if not productos_busqueda:
                        mostrar_error(frame1, "No hay productos disponibles con ese nombre. Escoja otro por favor.")
                        return
                    else:
                        productos.clear()
                        productos.extend(productos_busqueda)
                else:
                    if 1 <= numero <= len(productos):
                        seleccionado = productos[numero - 1]
                    elif numero == 5:
                        self.elegir_tipo_busqueda(cliente, window)
                        return
                    else:
                        mostrar_error(frame1, "Ese número está fuera del rango")
                        return

                if seleccionado is not None:
                    label_seleccionado = Label(frame1, text=f"Producto seleccionado: {seleccionado.get_nombre()}",
                                               font=("Arial", 12, "bold"), fg="green", bg="light blue", borderwidth=2,
                                               relief="solid")
                    label_seleccionado.pack(pady=5)
                    # Llamar a la función donde se agregan productos
                    self.donde_se_agregan_productos(cliente, seleccionado, window)

            boton_seleccionar = Button(frame1, text="Seleccionar", command=seleccionar,
                                       font=("Arial", 12), bg="#00FF00", fg="black")
            boton_seleccionar.pack(pady=10)

            def seleccionar_producto(producto):
                # Llamar a la función donde se agregan productos
                label_seleccionado = Label(frame1, text=f"Producto seleccionado: {producto.get_nombre()}",
                                           font=("Arial", 12, "bold"), fg="green", bg="light blue", borderwidth=2,
                                           relief="solid")
                label_seleccionado.pack(pady=5)
                self.donde_se_agregan_productos(cliente, producto, window)

        def buscar_y_mostrar(frame1, entry_nombre):
            nombre = entry_nombre.get().strip()
            productos = buscar_productos_por_nombre(nombre)
            if not productos:
                mostrar_error(frame1, "No se encontraron productos. Introduzca otro nombre.")
                return
            inferior = 0
            superior = 4
            actualizar_mostrar_productos(frame1, productos, inferior, superior)

        def mostrar_productos():
            widgets = window.winfo_children()
            for i, widget in enumerate(widgets):
                if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                    widget.destroy()

            frame1 = Frame(window, bg="light blue")
            frame1.pack(fill=BOTH, expand=True)

            # Entrada inicial
            entry_nombre = Entry(frame1, font=("Arial", 12))
            entry_nombre.pack(pady=10)

            boton_buscar = Button(frame1, text="Buscar",
                                  command=lambda: buscar_y_mostrar(frame1, entry_nombre),
                                  font=("Arial", 12), bg="#00FF00", fg="black")
            boton_buscar.pack(pady=10)

        mostrar_productos()

    @staticmethod
    def ajustar_texto(texto, ancho_celda):
        if len(texto) > ancho_celda:
            return texto[:ancho_celda - 1] + "."
        else:
            return texto

    def donde_se_agregan_productos(self, cliente, seleccionado,window):
        cantidad = simpledialog.askinteger("Cantidad", "¿Cuántos productos de este quiere usted?",
                                           minvalue=1, parent=window)

        if cantidad is None:
            return  # El usuario canceló el diálogo

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
            boton3 = Button(frame.campos, text="Eliminar un producto de mi carrito")
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

