from tkinter import Button, Frame, Label, Tk, TkVersion, messagebox
import tkinter
import tkinter as tk
from typing import List, Optional
import sys
sys.path.append('C:\\Users\\js682\\OneDrive\\Documentos\\pr-ctica-2-python-group-2-team-4\\src')
from fieldFrame import FieldFrame



from gestorAplicacion.servicios.proveedor import Proveedor



from gestorAplicacion.servicios.enums import Genero
from gestorAplicacion.servicios.tienda import Tienda
from gestorAplicacion.sujetos.administrador import Administrador
from uiMain import identidad, interfaz

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
        # Mostrar el frame rojo o azul dependiendo del tipo de usuario
        def callback():
            if not isinstance(self.usuario, Administrador):
                frame = Frame(window, bg="red")
                frame.pack(fill=tk.BOTH, expand=True)
            else:
                frame = Frame(window, bg="blue")
                frame.pack(fill=tk.BOTH, expand=True)
                self.seleccionar_tienda2(window)

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
            Label(window, text="¿Qué desea hacer?", font=("Arial", 12)).pack(pady=5)
            #pady=20, padx=20, fill='both', expand=True
            # Botones para cambiar de usuario o volver al menú principal
            opciones_frame = Frame(window)
            opciones_frame.pack(pady=40)
               
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
        Button(window, text="Administrar Productos", font=("Arial", 12)).pack(pady=5)
        Button(window, text="Administrar Proveedores", font=("Arial", 12), command=lambda: self.mostrar_proveedores(window)).pack(pady=5)

    @classmethod
    def mostrar_proveedores(self, window):
        """Método para mostrar proveedores disponibles y permitir seleccionar uno que coincida con la categoría de un pasillo"""
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
        pasillos = self.tienda_selecta.get_pasillos()

        # Obtener las categorías de los pasillos
        categorias_pasillos = {pasillo.categoria for pasillo in pasillos}

        # Obtener la lista de proveedores
        proveedores = Proveedor.get_seis_proveedores()

        # Filtrar los proveedores que coincidan con las categorías de los pasillos
        proveedores_filtrados = [proveedor for proveedor in proveedores if proveedor.get_tipo() in categorias_pasillos]

        if len(proveedores_filtrados) == 0:
            Label(proveedores_frame, text="No hay proveedores disponibles para esta tienda.", font=("Arial", 12)).pack(pady=5)
        else:
            # Mostrar cada proveedor filtrado como un botón seleccionable
            for idx, proveedor in enumerate(proveedores_filtrados, start=1):
                Button(proveedores_frame, text=f"{idx}. {proveedor.get_nombre()} - {proveedor.get_tipo().get_texto()}", 
                    font=("Arial", 12), 
                    command=lambda p=proveedor: self.seleccionar_proveedor(window, p)).pack(pady=5)

    @classmethod
    def seleccionar_proveedor(self, window, proveedor):
        """Método para manejar la selección de un proveedor y mostrar información adicional"""
        # Limpiar la ventana de widgets anteriores
        for widget in window.winfo_children():
            widget.destroy()

        Label(window, text=f"Has seleccionado al proveedor: {proveedor.get_nombre()}", font=("Arial", 15)).pack(pady=10)
        
        # Mostrar detalles adicionales del proveedor seleccionado
        Label(window, text=f"Tipo de proveedor: {proveedor.get_tipo().get_texto()}", font=("Arial", 12)).pack(pady=5)
        Label(window, text=f"Entrega en las siguientes tiendas: {', '.join([t.get_nombre() for t in proveedor.get_tiendas()])}", font=("Arial", 12)).pack(pady=5)


