import sys
from tkinter import Frame, Label, Entry, Button, messagebox

from gestorAplicacion.servicios.ahorcado import Ahorcado
from gestorAplicacion.servicios.enums import TipoCaja
from gestorAplicacion.servicios.tresEnRaya import TresEnRaya
from gestorAplicacion.sujetos.administrador import Administrador
from gestorAplicacion.sujetos.cliente import Cliente
from uiMain.main import Main


class Funcionalidad3:

    def impresion_facturas(self,persona, window):
        from tkinter import Frame, Label, Button, Entry, END, CENTER
        from uiMain.main import Main
        from gestorAplicacion.sujetos.administrador import Administrador
        from gestorAplicacion.sujetos.cliente import Cliente

        # Limpiar la ventana actual
        for widget in window.winfo_children():
            widget.destroy()

        # Obtener las tiendas con facturas
        tiendas = persona.get_tiendas_con_facturas()

        print(persona.get_facturas())
        print(tiendas)

        if not tiendas:
            Label(window, text="No tienes facturas en ninguna tienda.",
                  font=("Arial", 14), bg="light blue").pack(pady=20)
            return

        # Crear un frame para mostrar las tiendas
        frame_tiendas = Frame(window, bg="light blue")
        frame_tiendas.pack(fill='both', expand=True, pady=20)

        # Mostrar tabla de tiendas
        Label(frame_tiendas, text="Número de Facturas",
              font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)

        Label(frame_tiendas, text="+-----+----------------+-----------------+",
              font=("Arial", 12), bg="light blue").pack()
        Label(frame_tiendas, text="| No. | Nombre         | Cantidad        |",
              font=("Arial", 12), bg="light blue").pack()
        Label(frame_tiendas, text="+-----+----------------+-----------------+",
              font=("Arial", 12), bg="light blue").pack()

        conteo_tiendas = {}
        for tienda in tiendas:
            nombre_tienda = tienda.get_nombre()
            if nombre_tienda:
                cantidad_facturas = len(tienda.get_facturas()) if tienda.get_facturas() else 0
                conteo_tiendas[nombre_tienda] = cantidad_facturas

        for numero, (nombre, cantidad) in enumerate(conteo_tiendas.items(), start=1):
            Label(frame_tiendas, text=f"| {numero:<3} | {nombre:<14} | {cantidad:<15} |",
                  font=("Arial", 12), bg="light blue").pack()

        Label(frame_tiendas, text="+-----+----------------+-----------------+",
              font=("Arial", 12), bg="light blue").pack()

        # Entry y botón para seleccionar la tienda
        Label(frame_tiendas, text="Selecciona el número de la tienda:",
              font=("Arial", 12), bg="light blue").pack(pady=10)
        entry_tienda = Entry(frame_tiendas, font=("Arial", 12))
        entry_tienda.pack(pady=5)

        def seleccionar_tienda():
            try:
                seleccion = int(entry_tienda.get())
                tienda_seleccionada = None
                if 1 <= seleccion <= len(conteo_tiendas):
                    for numero, tienda in enumerate(tiendas, start=1):
                        if numero == seleccion:
                            tienda_seleccionada = tienda
                            break

                if tienda_seleccionada:
                    self.mostrar_facturas(tienda_seleccionada, persona, window)
                else:
                    mostrar_error("Selección inválida.")
            except ValueError:
                mostrar_error("Debes ingresar un número válido.")

        Button(frame_tiendas, text="Seleccionar tienda",
               font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
               command=seleccionar_tienda).pack(pady=10)

        def mostrar_error(mensaje):
            Label(frame_tiendas, text=mensaje, font=("Arial", 12), fg="red", bg="light blue").pack(pady=10)

    def mostrar_facturas(self,tienda_seleccionada, persona, window):
        # Limpiar la ventana actual
        for widget in window.winfo_children():
            widget.destroy()

        mis_facturas = persona.get_facturas1(tienda_seleccionada)

        # Crear un frame para mostrar las facturas
        frame_facturas = Frame(window, bg="light blue")
        frame_facturas.pack(fill='both', expand=True, pady=20)

        # Mostrar tabla de facturas
        Label(frame_facturas, text="Facturas",
              font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)

        Label(frame_facturas,
              text="+-----+--------------------+------------+-----------------+------------+----------+",
              font=("Arial", 12), bg="light blue").pack()
        Label(frame_facturas,
              text="| No. | Tienda             | Fecha      | Productos        | Precio     | Pagada   |",
              font=("Arial", 12), bg="light blue").pack()
        Label(frame_facturas,
              text="+-----+--------------------+------------+-----------------+------------+----------+",
              font=("Arial", 12), bg="light blue").pack()

        for numero, factura in enumerate(mis_facturas, start=1):
            if factura:
                estado_pago = "Sí" if factura.get_pagado() else "No"
                precio_total = factura.calcular_total()
                Label(frame_facturas,
                      text=f"| {numero:<3} | {factura.get_tienda().get_nombre():<18} | {factura.get_fecha_facturacion():<10} | {len(factura.get_productos()):<15} | {precio_total:<10.2f} | {estado_pago:<8} |",
                      font=("Arial", 12), bg="light blue").pack()

        Label(frame_facturas,
              text="+-----+--------------------+------------+-----------------+------------+----------+",
              font=("Arial", 12), bg="light blue").pack()

        # Entry y botón para seleccionar la factura
        Label(frame_facturas, text="Selecciona el número de la factura:",
              font=("Arial", 12), bg="light blue").pack(pady=10)
        entry_factura = Entry(frame_facturas, font=("Arial", 12))
        entry_factura.pack(pady=5)

        def seleccionar_factura():
            try:
                seleccion = int(entry_factura.get())
                if 1 <= seleccion <= len(mis_facturas):
                    factura_seleccionada = mis_facturas[seleccion - 1]
                    if factura_seleccionada:
                        self.mostrar_detalle_factura(factura_seleccionada, persona,window)
                    else:
                        mostrar_error("Factura seleccionada no encontrada.")
                else:
                    mostrar_error("Selección inválida.")
            except ValueError:
                mostrar_error("Debes ingresar un número válido.")

        Button(frame_facturas, text="Seleccionar factura",
               font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
               command=seleccionar_factura).pack(pady=10)

        def mostrar_error(mensaje):
            Label(frame_facturas, text=mensaje, font=("Arial", 12), fg="red", bg="light blue").pack(pady=10)

    def mostrar_detalle_factura(self,factura_seleccionada, persona, window):
        # Limpiar la ventana actual
        for widget in window.winfo_children():
            widget.destroy()

        # Mostrar detalles de los productos de la factura seleccionada
        frame_detalle = Frame(window, bg="light blue")
        frame_detalle.pack(fill='both', expand=True, pady=20)

        Label(frame_detalle, text="Detalles de la Factura",
              font=("Arial", 16, "bold"), bg="light blue").pack(pady=10)

        Label(frame_detalle, text="+-----+--------------------+---------------+----------+------------+----------+",
              font=("Arial", 12), bg="light blue").pack()
        Label(frame_detalle, text="| No. | Producto           | Marca         | Tamaño   | Categoría  | Precio   |",
              font=("Arial", 12), bg="light blue").pack()
        Label(frame_detalle, text="+-----+--------------------+---------------+----------+------------+----------+",
              font=("Arial", 12), bg="light blue").pack()

        for numero_producto, producto in enumerate(factura_seleccionada.get_productos(), start=1):
            if producto:
                Label(frame_detalle,
                      text=f"| {numero_producto:<3} | {producto.get_nombre():<18} | {producto.get_marca():<13} | {producto.get_tamano().get_tamano():<8} | {producto.get_categoria().get_texto():<10} | {producto.get_precio():<8.2f} |",
                      font=("Arial", 12), bg="light blue").pack()

        Label(frame_detalle, text="+-----+--------------------+---------------+----------+------------+----------+",
              font=("Arial", 12), bg="light blue").pack()

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
                  font=("Arial", 12, "bold"), bg="light blue").pack(pady=10)
            Button(frame_detalle, text="Pagar factura",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: persona.set_tienda(
                       factura_seleccionada.get_tienda()) or Funcionalidad3.seleccionar_caja(persona,
                                                                                             factura_seleccionada)).pack(
                pady=5)
            Button(frame_detalle, text="Escoger otra factura",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: self.impresion_facturas(persona, window)).pack(pady=5)
            Button(frame_detalle, text="Salir de funcionalidad",
                   font=("Arial", 12), bg="#ADD8E6", padx=20, pady=10,
                   command=lambda: Main.escoger_funcionalidad()).pack(pady=5)


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