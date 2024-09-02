import sys

class Funcionalidad3:
    @staticmethod
    def impresion_facturas(persona):
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
            mis_facturas = persona.get_facturas(tienda_seleccionada)

            # Imprimir las facturas
            print("+-----+--------------------+------------+-----------------+------------+----------+")
            print("| No. | Tienda             | Fecha      | Productos        | Precio     | Pagada   |")
            print("+-----+--------------------+------------+-----------------+------------+----------+")

            for numero, factura in enumerate(mis_facturas, start=1):
                if factura:
                    estado_pago = "Sí" if factura.is_pagado() else "No"
                    precio_total = Carrito.calcular_total(factura.get_productos())
                    print(f"| {numero:<3} | {factura.get_tienda().get_nombre():<18} | {factura.get_fecha_facturacion():<10} | {len(factura.get_productos()):<15} | {precio_total:<10.2f} | {estado_pago:<8} |")
            
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
                            print(f"| {numero_producto:<3} | {producto.get_nombre():<18} | {producto.get_marca():<13} | {producto.get_tamaño().get_tamaño():<8} | {producto.get_categoria().get_texto():<10} | {producto.get_precio():<8.2f} |")
                    
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
    def seleccionar_caja(cliente, carrito):
        cajas = cliente.get_tienda().cajas_disponibles()
        cliente.set_carrito(carrito)
        caja_seleccionada = None

        while True:
            if not cajas:
                print("No hay cajas disponibles.")
                print("1. Esperar a que una caja esté disponible.")
                print("2. No pagar y salir.")
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    tienda = cliente.get_tienda()
                    tienda.asignar_cajero(Tienda.encontrar_cajero(tienda.get_empleados()))  # Método para asignar un empleado a una caja
                    continue
                elif opcion == 2:
                    print("Ha decidido no pagar. Saliendo del proceso.")
                    return
                else:
                    print("Opción no válida.")
                    continue

            print("Seleccione una caja para pagar:")
            for i, caja in enumerate(cajas):
                print(f"{i + 1}. Caja: {caja.get_nombre()}, Tipo: {caja.get_tipo()}, Empleado: {caja.get_cajero().get_nombre()}")

            seleccion = int(input("Seleccione el número de la caja: "))

            if 1 <= seleccion <= len(cajas):
                caja_seleccionada = cajas[seleccion - 1]

                if caja_seleccionada.get_tipo() == TipoCaja.RAPIDA and len(cliente.get_carrito().get_productos()) > 5:
                    print("No puede usar la caja rápida porque tiene más de 5 productos.")
                    print("Por favor, seleccione otra caja.")
                    continue

                print("Ha seleccionado la caja:", caja_seleccionada.get_nombre())
                break
            else:
                print("Selección inválida. Inténtelo de nuevo.")

        caja_seleccionada.set_cliente(cliente)
        cliente.set_carrito(carrito)

        # Aplicar descuento por membresía
        descuento_membresia = cliente.calcular_descuento_por_membresia()
        precio_total = Carrito.calcular_total(carrito.get_productos())
        precio_con_descuento = precio_total * (1 - descuento_membresia)

        # Imprimir factura con descuento por membresía
        print(carrito.generar_detalles_factura(descuento_membresia, False))

        # Opción de borrar la factura antes de pagar
        print("¿Desea borrar esta factura antes de pagar?")
        print("1. Sí")
        print("2. No")
        opcion_borrar = int(input())

        if opcion_borrar == 1:
            carrito.eliminar_carrito()  # Eliminar carrito y devolver productos
            cliente.set_carrito(None)  # Desasignar carrito del cliente
            caja_seleccionada.set_cliente(None)  # Desasignar cliente de la caja
            print("Factura eliminada y productos devueltos al inventario.")
            return

        # Opción de jugar para obtener más descuento
        print("¿Desea intentar obtener un descuento adicional jugando?")
        print("1. Sí")
        print("2. No")
        opcion_juego = int(input())

        gano_juego = False
        if opcion_juego == 1:
            tiene_membresia = cliente.get_membresia() is not None
            if not tiene_membresia:
                print("Debe pagar 10 mil para intentar jugar.")
                carrito.incrementar_costo(10000)
                precio_total += 10000  # Aumentar el precio total antes de aplicar descuento del juego

            # Selección del juego
            print("Seleccione un juego:")
            print("1. Tres en Raya")
            print("2. Ahorcado")
            seleccion_juego = int(input())

            if seleccion_juego == 1:
                gano_juego = Funcionalidad3.tres_en_raya()
            elif seleccion_juego == 2:
                gano_juego = Funcionalidad3.ahorcado()
            else:
                print("Selección inválida.")
                return

            if gano_juego:
                descuento_juego = 0.10
                precio_con_descuento -= precio_total * descuento_juego
                print("¡Ganó el juego! Se aplica un 10% de descuento.")
            else:
                print("No ganó el juego. No se aplica descuento adicional.")
        
        # Realizar el pago final
        if precio_con_descuento > 0:
            if cliente.get_saldo() >= precio_con_descuento:
                cliente.set_saldo(cliente.get_saldo() - precio_con_descuento)
                caja_seleccionada.registrar_pago(precio_con_descuento)
                print("Pago realizado con éxito.")
            else:
                print("Saldo insuficiente para completar la compra.")
        else:
            print("El total de la compra es 0. No se requiere pago.")

    @staticmethod
    def tres_en_raya():
        # Implementar el juego Tres en Raya aquí
        pass

    @staticmethod
    def ahorcado():
        # Implementar el juego Ahorcado aquí
        pass

class Carrito:
    @staticmethod
    def calcular_total(productos):
        # Implementar el cálculo total de productos en el carrito
        pass

class Main:
    @staticmethod
    def escoger_funcionalidad():
        # Implementar el menú para seleccionar funcionalidades
        pass
