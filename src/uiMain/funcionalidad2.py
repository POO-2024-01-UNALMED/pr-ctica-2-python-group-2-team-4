import sys

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
        from gestorAplicacion.servicios.tienda import Tienda
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

        print("")

        # Imprimir líneas horizontales superiores
        print("-" * (mayor_m + mayor_n + mayor_p + 30))

        # Imprimir encabezados de la tabla
        print("    Nombre" + " " * (mayor_n - 4) + "|  Marca/Tamaño" + " " * (mayor_m - 10) +
              "|  Precio" + " " * (mayor_p - 4) + "|  Cantidad  |")

        print("-" * (mayor_m + mayor_n + mayor_p + 30))

        # Imprimir productos en la tabla
        contador = 1
        for p in productos[inferior:superior]:
            cantidad = cliente.get_tienda().cantidad_producto(p)  # Llamada a cantidad_producto()
            print(f"{contador}.", end="")
            print(Tienda.imprimir_producto(mayor_n, mayor_m, mayor_p, mayor_c, cantidad,
                                           p))  # Llamada a imprimir_producto()
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

    def impresion_seleccion_categoria(self, cliente, productos, categoria, mal_seleccionado):
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
                    self.busqueda_categoria(cliente,categoria, productos, seleccionado)
                    return None
                else:
                    print("Ese número está fuera del rango")
                    mal_seleccionado = True
                    continue

            if seleccionado is not None:
                return seleccionado

    def impresion_seleccion_nombre(self, cliente, productos, seleccionado):
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
                    self.busqueda_nombre(cliente, productos, seleccionado)  # Llamada a busqueda_nombre()

            return seleccionado

    def busqueda_categoria(self, cliente):
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

        productos = cliente.get_tienda().buscar_productos(cliente, categoria)

        while len(productos) == 0:
            print("No hay productos disponibles de esa categoría, escoja otra por favor.")
            decision_categoria = Main.escaner_con_rango(enumerado)

            if decision_categoria == enumerado:
                self.elegir_tipo_busqueda(cliente)

            categoria = Categoria.resolver_enum(decision_categoria)
            productos = cliente.get_tienda().buscar_productos(cliente, categoria)

        mal_seleccionado = False

        seleccionado = self.impresion_seleccion_categoria(cliente, productos, categoria, mal_seleccionado)

        Main.lineas()
        self.donde_se_agregan_productos(cliente, seleccionado)

    def busqueda_nombre(self, cliente):
        from main import Main
        productos = []
        seleccionado = None
        Main.lineas()  # Llamada a la función lineas()

        print("Introduzca el nombre del producto que desea buscar\n" +
              "O escoja [3]. [Volver] para regresar: ")
        nombre = input()

        try:
            number = int(nombre)
            string = True
        except ValueError:
            string = False

        if string:
            if int(nombre) == 3:
                self.elegir_tipo_busqueda(cliente)  # Llamada a elegir_tipo_busqueda()
                return

        if nombre.lower() == "volver":
            self.elegir_tipo_busqueda(cliente)  # Llamada a elegir_tipo_busqueda()
            return

        productos = []  # Inicialización de productos
        productos = cliente.get_tienda().buscar_productos(cliente, nombre)  # Llamada a buscar_productos()

        while len(productos) == 0:
            print("No hay productos disponibles con ese nombre, escoja otro por favor")
            print("Introduzca otro nombre: ")
            nombre = input()

            try:
                number = int(nombre)
                string = True
            except ValueError:
                string = False

            if string:
                if int(nombre) == 3:
                    self.elegir_tipo_busqueda(cliente)  # Llamada a elegir_tipo_busqueda()
                    return

            if nombre.lower() == "volver":
                self.elegir_tipo_busqueda(cliente)  # Llamada a elegir_tipo_busqueda()
                return

            productos = cliente.get_tienda().buscar_productos(cliente, nombre)  # Llamada a buscar_productos()

        seleccionado = self.impresion_seleccion_nombre(cliente, productos,
                                                  seleccionado)  # Llamada a impresion_seleccion_nombre()
        self.donde_se_agregan_productos(cliente, seleccionado)  # Llamada a donde_se_agregan_productos()

    @staticmethod
    def ajustar_texto(texto, ancho_celda):
        if len(texto) > ancho_celda:
            return texto[:ancho_celda - 1] + "."
        else:
            return texto

    def donde_se_agregan_productos(self, cliente, seleccionado):
        from main import Main
        print("¿Cuántos productos de este quiere usted?\n")
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

        self.elegir_tipo_busqueda(cliente)

    def elegir_tipo_busqueda(self, cliente):
        from main import Main
        from funcionalidad1 import Funcionalidad1
        tienda = cliente.get_tienda()
        if tienda is None:
            Main.lineas()  # Implementar este método
            print("Debería seleccionar una tienda primero, diríjase a la funcionalidad 1")
            print("1. Ir a la funcionalidad 1")
            print("2. Ver el menú para escoger otra funcionalidad")
            decision = Main.escaner_con_rango(2)  # Implementar este método
            if decision == 1:
                Funcionalidad1.consultas_eco()  # Implementar este método en Funcionalidad1
            elif decision == 2:
                Main.escoger_funcionalidad()  # Implementar este método en Main
            return

        Main.lineas()  # Implementar este método
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

        decision = Main.escaner_con_rango(5)  # Implementar este método

        if decision == 1:
            self.busqueda_categoria(cliente)  # Implementar este método
        elif decision == 2:
            self.busqueda_nombre(cliente)  # Implementar este método
        elif decision == 3:
            if len(cliente.get_carrito().get_productos()) == 0:
                Main.lineas()  # Implementar este método
                print("Usted no puede seleccionar esta opción")
                self.elegir_tipo_busqueda(cliente)
                return

            Main.lineas()  # Implementar este método
            print("Estos son los productos de su carrito:")
            print("")
            productos = cliente.get_carrito().get_productos()

            ancho_celda_nombre = 20
            ancho_celda_marca = 15
            ancho_celda_tamano = 10
            ancho_celda_precio = 10
            ancho_celda_cantidad = 10

            # Mostrar productos únicos en el carrito
            print("+----+--------------------+---------------+----------+----------+----------+")
            print("| No | Nombre             | Marca         | Tamaño   | Precio   | Cantidad |")
            print("+----+--------------------+---------------+----------+----------+----------+")

            productos_cantidad = {}
            productos_map = {}

            # Sumar cantidades de productos iguales
            for producto in cliente.get_carrito().get_productos():
                id_producto = producto.get_id()
                productos_map[id_producto] = producto
                productos_cantidad[id_producto] = productos_cantidad.get(id_producto, 0) + 1

            # Imprimir los productos sin duplicados con la cantidad total
            contador = 1
            for id_producto, producto in productos_map.items():
                cantidad_total = productos_cantidad[producto.get_id()]
                nombre_producto = producto.get_nombre()
                marca_producto = producto.get_marca()
                tamano_producto = producto.get_tamano().get_tamano()  # Implementar método en clase Tamaño
                precio_producto = f"{producto.get_precio():.2f}"

                print(
                    f"| {contador:2d} | {nombre_producto:<18} | {marca_producto:<13} | {tamano_producto:<8} | {precio_producto:<8} | {cantidad_total:<8} |")
                contador += 1

            print("+----+--------------------+---------------+----------+----------+----------+")
            print("")
            print("Escoja una de los productos que desee borrar")
            print(f"{contador}. Cancelar borrar producto del carrito")
            seleccion = Main.escaner_con_rango(contador)  # Implementar este método

            if seleccion == contador:
                self.elegir_tipo_busqueda(cliente)
                return

            if 0 < seleccion <= len(cliente.get_carrito().get_productos()):
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

                if producto_seleccionado:
                    print("")
                    cantidad_eliminar = int(input("Ingrese la cantidad que desea eliminar: "))
                    cantidad_actual = cliente.get_carrito().contar_repeticiones(
                        producto_seleccionado)  # Implementar método en Carrito
                    if 0 < cantidad_eliminar <= cantidad_actual:
                        cliente.get_carrito().eliminar_productos(producto_seleccionado,
                                                                 cantidad_eliminar)  # Implementar método en Carrito
                        Main.lineas()  # Implementar este método
                        print("Productos actualizados en el carrito:")
                        print("")
                        print("+----+--------------------+---------------+----------+----------+----------+")
                        print("| No | Nombre             | Marca         | Tamaño   | Precio   | Cantidad |")
                        print("+----+--------------------+---------------+----------+----------+----------+")

                        productos_impresos.clear()
                        contador = 1

                        for producto in cliente.get_carrito().get_productos():
                            if producto.get_id() in productos_impresos:
                                continue

                            nombre_producto = producto.get_nombre()
                            marca_producto = producto.get_marca()
                            tamano_producto = producto.get_tamano().get_tamano()  # Implementar método en clase Tamaño
                            precio_producto = f"{producto.get_precio():.2f}"
                            cantidad_producto = cliente.get_carrito().contar_repeticiones(
                                producto)  # Implementar método en Carrito

                            print(
                                f"| {contador:2d} | {nombre_producto:<18} | {marca_producto:<13} | {tamano_producto:<8} | {precio_producto:<8} | {cantidad_producto:<8} |")
                            productos_impresos.add(producto.get_id())
                            contador += 1
                        print("+----+--------------------+---------------+----------+----------+----------+")

                    else:
                        print("Cantidad inválida.")
                else:
                    print("Producto seleccionado no encontrado.")
            else:
                print("Selección inválida.")
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
            Main.escoger_funcionalidad()  # Implementar este método en Main

        elif decision == 5:
            if len(cliente.get_carrito().get_productos()) == 0:
                Main.lineas()  # Implementar este método
                print("Usted no puede seleccionar esta opción")
                self.elegir_tipo_busqueda(cliente)
                return
            cliente.get_tienda().get_facturas().append(cliente.get_carrito())  # Implementar métodos en Tienda y Factura
            cliente.get_facturas().append(cliente.get_carrito())
            cliente.set_carrito(None)
            cliente.set_tienda(None)
            Main.escoger_funcionalidad()  # Implementar este metodo en Main

