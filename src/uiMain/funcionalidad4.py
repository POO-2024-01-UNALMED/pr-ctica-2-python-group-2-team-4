from datetime import datetime
from tkinter import Button, Frame, Label, Tk, TkVersion, messagebox
import tkinter
import tkinter as tk
#from typing import List, Optional
import sys
sys.path.append('C:\\Users\\js682\\OneDrive\\Documentos\\pr-ctica-2-python-group-2-team-4\\src')

from gestorAplicacion.servicios.producto import Producto
from uiMain.fieldFrame import FieldFrame
from gestorAplicacion.servicios.proveedor import Proveedor

from gestorAplicacion.servicios.enums import Genero
from gestorAplicacion.servicios.tienda import Tienda
from gestorAplicacion.sujetos.administrador import Administrador
#from uiMain import identidad, interfaz

import gestorAplicacion

class Funcionalidad4:
     
    from gestorAplicacion.servicios.producto import Producto
    from gestorAplicacion.servicios.tienda import Tienda
    from gestorAplicacion.sujetos.administrador import Administrador
    
    def __init__(self):
        self.user_id = None
        self.usuario = None
        self.tienda_selecta = None
        #self.tiendaSelecta: Optional[Tienda] = None


    # @staticmethod
    # def escaner(max_opcion: int) -> int:
    #     try:
    #         opcion = int(input("Ingrese una opción: "))
    #         if 1 <= opcion <= max_opcion:
    #             return opcion
    #         else:
    #             print("Opción no válida. Intente de nuevo.")
    #             return Funcionalidad4.escaner(max_opcion)
    #     except ValueError:
    #         print("Entrada inválida. Ingrese un número.")
    #         return Funcionalidad4.escaner(max_opcion)

    # @staticmethod
    # def print_tabla_productos(productos: List[Producto]):
    #     print("+------------------------------------+")
    #     print("| No. |      Nombre de Producto      |")
    #     print("+------------------------------------+")

    #     ancho_celda = 28
    #     for i, producto in enumerate(productos):
    #         cant = Funcionalidad4.tiendaSelecta.cantidad_producto(producto)
    #         nombre_producto = f"{producto.nombre}. unidades en el inventario: {cant}"
    #         espacios = (ancho_celda - len(nombre_producto)) // 2
    #         padding_izquierdo = " " * espacios
    #         padding_derecho = " " * (ancho_celda - len(nombre_producto) - espacios)

    #         print(f"| {i + 1:>2} |{padding_izquierdo}{nombre_producto}{padding_derecho}|")
    #     print("+------------------------------------+")

    

    # @staticmethod
    # def seleccionar_tienda(usuario):

    #     print("------------------ REVISION DE TIENDA -----------------")
        
    #     if not usuario.tiendas:
    #         print("No tienes ninguna tienda registrada.")
    #         print("¿Qué desea hacer?")
    #         print("1. Cambiar de usuario")
    #         print("2. Volver al Menú principal")

    #         valor = Funcionalidad4.escaner(2)
    #         if valor == 1:
    #             # Aquí deberías incluir el código para cambiar de usuario
    #             pass
    #         elif valor == 2:
    #             # Aquí deberías incluir el código para volver al menú principal
    #             pass
    #         return
        
    #     print("Tiendas disponibles:")
    #     for idx, tienda in enumerate(usuario.tiendas):
    #         print(f"{idx + 1}. {tienda.nombre}")

    #     decs = Funcionalidad4.escaner(len(usuario.tiendas))
    #     tienda = usuario.tiendas[decs - 1]
    #     Funcionalidad4.tiendaSelecta = tienda
    #     Funcionalidad4.adminitrar_tienda(tienda)

    # @staticmethod
    # def adminitrar_tienda(tienda: Tienda):
    #     from gestorAplicacion.servicios.producto import Producto
    #     from gestorAplicacion.servicios.enums import EstadoProducto
    #     print("Seleccione una opción:")
    #     print("1. Total de productos en el inventario")
    #     print("2. Productos vencidos")
    #     print("3. Ver productos devueltos")
    #     print("4. Reabastecimiento")
    #     print("5. Seleccionar otra tienda")
    #     print("6. Volver al menú principal")

    #     opcion = Funcionalidad4.escaner(6)

    #     if opcion == 1:
    #         productos = tienda.obtener_todos_los_productos()
    #         productos_unicos = list({p.nombre: p for p in productos}.values())
    #         if productos_unicos:
    #             Funcionalidad4.print_tabla_productos(productos_unicos)
    #         else:
    #             print("La tienda no tiene ningún producto.")

    #         print("Seleccione una opción:")
    #         print("1. Seleccionar otra tienda")
    #         print("2. Volver al menú principal")
    #         print("3. Volver atrás")
            
    #         opcion_case1 = Funcionalidad4.escaner(3)
    #         if opcion_case1 == 1:
    #             # Aquí deberías incluir el código para seleccionar otra tienda
    #             pass
    #         elif opcion_case1 == 2:
    #             # Aquí deberías incluir el código para volver al menú principal
    #             pass
    #         elif opcion_case1 == 3:
    #             Funcionalidad4.adminitrar_tienda(tienda)

    #     elif opcion == 2:
    #         print("Productos vencidos recolectados:")
    #         productos_vencidos = tienda.get_productos_vencidos()
    #         if productos_vencidos:
    #             for producto in productos_vencidos:
    #                 print(f"{producto.nombre} {producto.marca} {producto.tamaño} {producto.estado}")

    #         print("Desea recolectar productos vencidos de los pasillos?")
    #         print("1. Sí")
    #         print("2. No")
    #         print("3. Seleccionar otra tienda")
    #         print("4. Volver al menú principal")
    #         print("5. Volver atrás")

    #         opcion_case2 = Funcionalidad4.escaner(5)
    #         if opcion_case2 == 1:
    #             tienda.vencer_producto()
    #             productos_vencidos = tienda.get_productos_vencidos()
    #             if productos_vencidos:
    #                 for producto in productos_vencidos:
    #                     print(producto.nombre)

    #             print("Seleccione una opción:")
    #             print("1. Seleccionar otra tienda")
    #             print("2. Volver al menú principal")
    #             print("3. Volver atrás")

    #             opcion_case2 = Funcionalidad4.escaner(3)
    #             if opcion_case2 == 1:
    #                 # Aquí deberías incluir el código para seleccionar otra tienda
    #                 pass
    #             elif opcion_case2 == 2:
    #                 # Aquí deberías incluir el código para volver al menú principal
    #                 pass
    #             elif opcion_case2 == 3:
    #                 Funcionalidad4.adminitrar_tienda(tienda)
    #         elif opcion_case2 == 2:
    #             print("Seleccione una opción:")
    #             print("1. Seleccionar otra tienda")
    #             print("2. Volver al menú principal")
    #             print("3. Volver atrás")

    #             opcion_case2 = Funcionalidad4.escaner(3)
    #             if opcion_case2 == 1:
    #                 # Aquí deberías incluir el código para seleccionar otra tienda
    #                 pass
    #             elif opcion_case2 == 2:
    #                 # Aquí deberías incluir el código para volver al menú principal
    #                 pass
    #             elif opcion_case2 == 3:
    #                 Funcionalidad4.adminitrar_tienda(tienda)
    #         elif opcion_case2 == 3:
    #             # Aquí deberías incluir el código para seleccionar otra tienda
    #             pass
    #         elif opcion_case2 == 4:
    #             # Aquí deberías incluir el código para volver al menú principal
    #             pass

    #     elif opcion == 3:
    #         print("Productos devueltos en la tienda:")
    #         productos_devueltos = tienda.get_productos_devueltos()
    #         if productos_devueltos:
    #             for producto in productos_devueltos:
    #                 print(f"{producto.nombre} Estado: {producto.estado}")

    #             print("Seleccione una opción:")
    #             print("1. Eliminar de la tienda los productos defectuosos")
    #             print("2. Devolver a los pasillos los productos activos")
    #             print("3. Seleccionar otra tienda")
    #             print("4. Volver al menú principal")
    #             print("5. Volver atrás")

    #             opcion_case3 = Funcionalidad4.escaner(5)
    #             if opcion_case3 == 1:
    #                 tienda.get_productos_devueltos().remove_if(lambda producto: producto.estado == EstadoProducto.DEFECTUOSO)
    #                 print("El dinero ya ha sido devuelto al cliente.")
    #                 print("Productos eliminados con éxito.")

    #                 print("Seleccione una opción:")
    #                 print("1. Seleccionar otra tienda")
    #                 print("2. Volver al menú principal")
    #                 print("3. Volver atrás")

    #                 opcion_casea = Funcionalidad4.escaner(3)
    #                 if opcion_casea == 1:
    #                     # Aquí deberías incluir el código para seleccionar otra tienda
    #                     pass
    #                 elif opcion_casea == 2:
    #                     # Aquí deberías incluir el código para volver al menú principal
    #                     pass
    #                 elif opcion_casea == 3:
    #                     Funcionalidad4.adminitrar_tienda(tienda)
    #             elif opcion_case3 == 2:
    #                 tienda.transferir_productos(productos_devueltos)
    #                 print("Productos devueltos al pasillo con éxito.")

    #                 print("Seleccione una opción:")
    #                 print("1. Seleccionar otra tienda")
    #                 print("2. Volver al menú principal")
    #                 print("3. Volver atrás")

    #                 opcion_casec = Funcionalidad4.escaner(3)
    #                 if opcion_casec == 1:
    #                     # Aquí deberías incluir el código para seleccionar otra tienda
    #                     pass
    #                 elif opcion_casec == 2:
    #                     # Aquí deberías incluir el código para volver al menú principal
    #                     pass
    #                 elif opcion_casec == 3:
    #                     Funcionalidad4.adminitrar_tienda(tienda)
    #             elif opcion_case3 == 3:
    #                 # Aquí deberías incluir el código para seleccionar otra tienda
    #                 pass
    #             elif opcion_case3 == 4:
    #                 # Aquí deberías incluir el código para volver al menú principal
    #                 pass
    #         else:
    #             print("No hay productos devueltos.")
    #             print("Seleccione una opción:")
    #             print("1. Seleccionar otra tienda")
    #             print("2. Volver al menú principal")
    #             print("3. Volver atrás")

    #             opcion_case3 = Funcionalidad4.escaner(3)
    #             if opcion_case3 == 1:
    #                 # Aquí deberías incluir el código para seleccionar otra tienda
    #                 pass
    #             elif opcion_case3 == 2:
    #                 # Aquí deberías incluir el código para volver al menú principal
    #                 pass
    #             elif opcion_case3 == 3:
    #                 Funcionalidad4.adminitrar_tienda(tienda)

    #     elif opcion == 4:
    #         print("Reabastecimiento de la tienda:")
    #         print("Ingrese los datos del producto a reabastecer:")

    #         nombre = input("Nombre del producto: ")
    #         marca = input("Marca del producto: ")
    #         tamaño = input("Tamaño del producto: ")
    #         cantidad = int(input("Cantidad a reabastecer: "))

    #         producto = Producto(nombre=nombre, marca=marca, tamaño=tamaño, estado=EstadoProducto.ACTIVO)
    #         Funcionalidad4.tiendaSelecta.agregar_producto(producto, cantidad)
    #         print(f"Producto {nombre} reabastecido con éxito.")

    #         print("Seleccione una opción:")
    #         print("1. Seleccionar otra tienda")
    #         print("2. Volver al menú principal")
    #         print("3. Volver atrás")

    #         opcion_case4 = Funcionalidad4.escaner(3)
    #         if opcion_case4 == 1:
    #             # Aquí deberías incluir el código para seleccionar otra tienda
    #             pass
    #         elif opcion_case4 == 2:
    #             # Aquí deberías incluir el código para volver al menú principal
    #             pass
    #         elif opcion_case4 == 3:
    #             Funcionalidad4.adminitrar_tienda(tienda)

    #     elif opcion == 5:
    #         # Aquí deberías incluir el código para seleccionar otra tienda
    #         pass
    #     elif opcion == 6:
    #         # Aquí deberías incluir el código para volver al menú principal
    #         pass

            # ------------------------------------------- # 

    # alerta de que el usuario no tiene tiendas 
    @classmethod
    def mostrar_ventana(cls):
        ventana = tk.Tk()
        ventana.title("Aviso")
        ventana.geometry("300x150")

        # Crear el mensaje
        mensaje = tk.Label(ventana, text="El usuario no posee ninguna tienda o no es administrador.")
        mensaje.pack(pady=20)

        # Crear el botón Aceptar
        boton_aceptar = tk.Button(ventana, text="Aceptar", command=ventana.destroy)
        boton_aceptar.pack(pady=10)

        # Iniciar el loop de tkinter
        ventana.mainloop()

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
                if identidad.resultado is not None and identidad.terminado is not False:
                    self.usuario = identidad.resultado
                    # Llama al frame de usuario solo si el usuario ha sido identificado
                    self.mostrar_frame_usuario(window)
                else:
                    # Si aún no se ha identificado, verificar de nuevo
                    window.after(100, check_identificacion)

            # Iniciar la espera para que el resultado se procese
            window.after(100, check_identificacion)

        ingresa()

    @classmethod
    def mostrar_frame_usuario(self, window):
    # Mostrar el frame correspondiente dependiendo del tipo de usuario
        def callback():
            # Si no es administrador
            if not isinstance(self.usuario, Administrador):
                # Limpiar la ventana
                widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
                for i, widget in enumerate(widgets):
                    if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                        widget.destroy()

                # Crear un frame para mostrar el mensaje de que no es administrador
                frame = Frame(window, bg="red")
                frame.pack(fill=tk.BOTH, expand=True, pady=50)

                # Mensaje para el usuario no administrador
                Label(frame, text="No eres un administrador.", font=("Arial", 15), bg="red", fg="white").pack(pady=10)

                # Botón para volver a ingresar
                Button(frame, text="Aceptar", font=("Arial", 12),
                    command=lambda: self.ingresar(window)).pack(pady=10)

            # Si es administrador
            else:
                # Limpiar la ventana
                widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
                for i, widget in enumerate(widgets):
                    if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                        widget.destroy()

                # Crear un frame para administrador
                frame = Frame(window, bg="blue")
                frame.pack(fill=tk.BOTH, expand=True)

                # Llamar a la función seleccionar tienda para el administrador
                self.seleccionar_tienda2(window)

        # Usar after para evitar problemas asincrónicos y ejecutar el callback
        window.after(100, callback)
    
    @classmethod
    def seleccionar_tienda2(self, window):
        """Método para seleccionar una tienda"""
        # Limpiar la ventana de widgets anteriores
        usuario = self.usuario
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                widget.destroy()

        # Si no hay tiendas registradas
        if len(usuario.get_tiendas()) == 0:
            Label(window, text="No tienes ninguna tienda registrada", font=("Arial", 15)).pack(pady=10)
            Label(window, text="Por favor, registre una tienda en la funcionalidad 5 para continuar.", font=("Arial", 12)).pack(pady=5)

            # Frame para botones
            opciones_frame = Frame(window)
            opciones_frame.pack(pady=40)

            # # Botón para redirigir al usuario a registrar una nueva tienda
            # Button(opciones_frame, text="Registrar tienda", font=("Arial", 12), command=self.registrar_tienda).pack(side="left", padx=10)

            # # Botón para cambiar de usuario si lo desea
            # Button(opciones_frame, text="Cambiar de usuario", font=("Arial", 12), command=lambda: self.ingresar(window)).pack(side="left", padx=10)

        else:
            Label(window, text="Tiendas disponibles:", font=("Arial", 15)).pack(pady=10)

            tiendas_frame = Frame(window)
            tiendas_frame.pack(pady=10)

            # Listar las tiendas disponibles
            for idx, tienda in enumerate(usuario.get_tiendas(), start=1):
                Button(tiendas_frame, text=f"{idx}. {tienda.get_nombre()}", font=("Arial", 12), 
                    command=lambda t=tienda: self.administrar_tienda(window, t)).pack(pady=5)
    

    @classmethod
    def administrar_tienda(self, window, tienda):
        """Método para administrar la tienda seleccionada"""
        self.tienda_selecta = tienda
        # Limpiar la ventana de widgets anteriores
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                widget.destroy()

        Label(window, text=f"Has seleccionado la tienda: {tienda.get_nombre()}", font=("Arial", 15)).pack(pady=10)

        # Botones para administrar la tienda
        Button(window, text="Administrar Productos", font=("Arial", 12), command=lambda: self.administrar_productos(window, tienda)).pack(pady=5)
        Button(window, text="Administrar Proveedores", font=("Arial", 12), command=lambda: self.mostrar_proveedores(window, tienda)).pack(pady=5) 

    @classmethod
    def administrar_productos(self, window, tienda):
        """Método para administrar los productos de una tienda"""
        # Limpiar la ventana de widgets anteriores
        widgets = window.winfo_children()  
        for i, widget in enumerate(widgets):
            if i >= 4:  
                widget.destroy()

        Label(window, text=f"Administrando productos de la tienda: {tienda.get_nombre()}", font=("Arial", 15)).pack(pady=10)

        # Frame para las opciones de administración de productos
        opciones_frame = Frame(window)
        opciones_frame.pack(pady=10)

        # Botón para ver todos los productos en el inventario
        Button(opciones_frame, text="Ver Total de Productos en el Inventario", font=("Arial", 12), 
            command=lambda: self.mostrar_inventario_productos(window, tienda)).pack(pady=5)

        # Botón para ver productos vencidos
        Button(opciones_frame, text="Ver Productos Vencidos", font=("Arial", 12), 
            command=lambda: self.mostrar_productos_vencidos(window, tienda)).pack(pady=5)
        

    @classmethod
    def mostrar_inventario_productos(self, window, tienda):
        
        """Método para mostrar el total de productos en el inventario"""
        # Limpiar la ventana de widgets anteriores
        widgets = window.winfo_children()  
        for i, widget in enumerate(widgets):
            if i >= 4:  
                widget.destroy()

        Label(window, text="Inventario de productos:", font=("Arial", 15)).pack(pady=10)

        # Obtener todos los productos de la tienda
        productos_totales = tienda.obtener_todos_los_productos()

        # Diccionario para agrupar productos por nombre, tamaño y marca
        inventario = {}
        for producto in productos_totales:
            clave = (producto.get_nombre(), producto.get_tamano(), producto.get_marca())
            if clave in inventario:
                inventario[clave]["cantidad"] += 1
            else:
                inventario[clave] = {
                    "nombre": producto.get_nombre(),
                    "tamano": producto.get_tamano(),
                    "marca": producto.get_marca(),
                    "precio": producto.get_precio(),
                    "cantidad": 1
                }

        # Frame para mostrar el inventario
        inventario_frame = Frame(window)
        inventario_frame.pack(pady=10)

        # Mostrar los productos en un formato bonito
        for clave, detalles in inventario.items():
            Label(inventario_frame, text=f"{detalles['nombre']} - {detalles['tamano']} - {detalles['marca']} - Cantidad: {detalles['cantidad']} - Precio: ${detalles['precio']:.2f}", font=("Arial", 12)).pack(pady=5)
            

    @classmethod
    def mostrar_productos_vencidos(self, window, tienda):
        """Método para mostrar los productos vencidos en la tienda"""

        # Limpiar la ventana de widgets anteriores
        widgets = window.winfo_children()
        for i, widget in enumerate(widgets):
            if i >= 4:
                widget.destroy()

        # Título de la sección
        Label(window, text="Productos vencidos:", font=("Arial", 15)).pack(pady=10)

        # Lista para almacenar productos vencidos
        productos_vencidos = []

        # Recorrer cada pasillo de la tienda para acceder a los productos
        for pasillo in tienda._pasillos:
            for producto in pasillo.productos:
                fecha_perecer = producto._fecha_perecer

                if isinstance(fecha_perecer, str):
                    try:
                        # Intentar convertir la cadena a fecha usando el formato adecuado
                        fecha_perecer = datetime.strptime(fecha_perecer, "%Y-%m-%d").date()  # Ejemplo de formato 'YYYY-MM-DD'
                    except ValueError:
                        # Si la conversión falla, se ignora este producto
                        continue

                # Verificar si la fecha de vencimiento es válida y si el producto está vencido
                if fecha_perecer and fecha_perecer < Producto.fecha_actual:
                    productos_vencidos.append(producto)

        # Frame para mostrar los productos vencidos
        vencidos_frame = Frame(window)
        vencidos_frame.pack(pady=10)

        # Mostrar los productos vencidos si existen
        if productos_vencidos:
            for producto in productos_vencidos:
                Label(vencidos_frame, text=f"{producto._nombre} - {producto._tamano} - {producto._marca} - Vencido el: {producto._fecha_perecer}", font=("Arial", 12)).pack(pady=5)
        else:
            # Mensaje si no hay productos vencidos
            Label(vencidos_frame, text="No hay productos vencidos en esta tienda.", font=("Arial", 12)).pack(pady=5)

    @classmethod
    def mostrar_proveedores(self, window, tienda):
        """Método para mostrar proveedores disponibles y permitir seleccionar uno que coincida con la categoría de un pasillo"""
        self.tienda_selecta = tienda
        # Limpiar la ventana de widgets anteriores
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                widget.destroy()

        Label(window, text="Proveedores disponibles:", font=("Arial", 15)).pack(pady=10)

        # Frame para contener la lista de proveedores
        proveedores_frame = Frame(window)
        proveedores_frame.pack(pady=10)

        # Obtener la lista de pasillos de la tienda seleccionada
        pasillos = tienda.get_pasillos()

        # Obtener las categorías de los pasillos y convertirlas a texto
        categorias_pasillos = {pasillo.categoria.get_texto() for pasillo in pasillos}

        # Obtener la lista de proveedores
        proveedores = Proveedor.get_seis_proveedores()

        # Filtrar los proveedores que coincidan con las categorías de los pasillos (comparamos en formato texto)
        proveedores_filtrados = [proveedor for proveedor in proveedores if proveedor.get_tipo() in categorias_pasillos]

        if len(proveedores_filtrados) == 0:
            Label(proveedores_frame, text="No hay proveedores disponibles para esta tienda.", font=("Arial", 12)).pack(pady=5)
        else:
            # Mostrar cada proveedor filtrado como un botón seleccionable
            for idx, proveedor in enumerate(proveedores_filtrados, start=1):
                Button(proveedores_frame, text=f"{idx}. {proveedor.get_nombre()} - {proveedor.get_tipo()}", 
                    font=("Arial", 12), 
                    command=lambda p=proveedor: self.seleccionar_proveedor(window, p)).pack(pady=5)

    @classmethod
    def seleccionar_proveedor(self, window, proveedor):
        """Método para manejar la selección de un proveedor y mostrar los productos para que el usuario seleccione la cantidad a pedir"""
        # Limpiar la ventana de widgets anteriores
        widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
        for i, widget in enumerate(widgets):
            if i >= 4:  # Si el índice es 4 o mayor, elimina el widget
                widget.destroy()

        Label(window, text=f"Has seleccionado al proveedor: {proveedor.get_nombre()}", font=("Arial", 15)).pack(pady=10)

        # Obtener los productos del proveedor
        productos_proveedor = proveedor.get_productos_proveedor()

        if not productos_proveedor:
            Label(window, text="Este proveedor no tiene productos disponibles.", font=("Arial", 12)).pack(pady=5)
            return

        # Configurar las etiquetas y valores iniciales
        criterios = [f"{producto.get_nombre()} - ${producto.get_precio():.2f} c/u" for producto in productos_proveedor]
        valores = ["0" for _ in productos_proveedor]  # Inicialmente, todos los valores son 0
        habilitado = [True for _ in productos_proveedor]  # Todos los campos están habilitados

        # Mostrar el frame para que el usuario ingrese la cantidad de cada producto
        field_frame = FieldFrame(
            window, 
            tituloCriterios="Producto", 
            criterios=criterios, 
            tituloValores="Cantidad", 
            valores=valores, 
            habilitado=habilitado, 
            titulo="Productos del Proveedor", 
            descripcion="Seleccione la cantidad de cada producto para reabastecer su tienda.", 
            botones=True
        )
        field_frame.pack(fill="both", expand=True, pady=10)

        def hacer_pedido():
            cantidades = [int(entry.get()) for entry in field_frame._entrys]
            total_costo = 0
            tienda = self.tienda_selecta
            saldo_tienda = tienda.get_saldo()

            for producto, cantidad in zip(productos_proveedor, cantidades):
                if cantidad > 0:
                    # Clonar el producto y agregarlo al pasillo correspondiente
                    for _ in range(cantidad):
                        producto_clonado = Producto(
                            nombre=f"{producto.get_nombre()} - {producto.get_precio()}",
                            marca=producto.get_marca(),
                            precio=producto.get_precio(),
                            tamano=producto.get_tamano(),
                            categoria=producto.get_categoria(),
                            descripcion=producto.get_descripcion(),
                            pasillo=None,  # Esto se asignará en el pasillo correspondiente
                            tienda=tienda
                        )
                        # Asignar al pasillo según la categoría
                        pasillo_correspondiente = next(
                            (p for p in tienda.get_pasillos() if p.categoria == producto.get_categoria()), None
                        )
                        if pasillo_correspondiente:
                            pasillo_correspondiente.agregar_producto(producto_clonado)

                        total_costo += producto.get_precio()

            # Verificar si el total excede el saldo de la tienda
            if total_costo > saldo_tienda:
                Label(window, text="¡Saldo de la tienda insuficiente para completar el pedido!", font=("Arial", 12), fg="red").pack(pady=10)
            else:
                def operacion_completada():
        # Código para actualizar la interfaz después de completar la operación
                    Label(window, text="Reabastecimiento completado.", font=("Arial", 15), fg="green").pack(pady=10)
                    # Botón para terminar
                    terminar_button = Button(window, text="Terminar", font=("Arial", 15), command=window.destroy)
                    terminar_button.pack(pady=10)

    # Programar la actualización de la interfaz después de la operación asincrónica
                window.after(100, operacion_completada)

        # Botón para hacer el pedido
        field_frame.aceptar.config(command=hacer_pedido)

        
        


