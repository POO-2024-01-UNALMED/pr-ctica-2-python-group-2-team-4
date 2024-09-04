class Funcionalidad1:
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

