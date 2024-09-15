from tkinter import Tk, TkVersion
import tkinter
import tkinter as tk
from typing import List, Optional
import sys

from fieldFrame import FieldFrame
sys.path.append('C:\\Users\\js682\\OneDrive\\Documentos\\pr-ctica-2-python-group-2-team-4\\src')
from gestorAplicacion.sujetos.administrador import Administrador
from uiMain import identidad, interfaz

import gestorAplicacion

class Funcionalidad4:
    from gestorAplicacion.servicios.producto import Producto
    from gestorAplicacion.servicios.tienda import Tienda
    from gestorAplicacion.sujetos.administrador import Administrador
    tiendaSelecta: Optional[Tienda] = None

    @staticmethod
    def escaner(max_opcion: int) -> int:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= max_opcion:
                return opcion
            else:
                print("Opción no válida. Intente de nuevo.")
                return Funcionalidad4.escaner(max_opcion)
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            return Funcionalidad4.escaner(max_opcion)

    @staticmethod
    def print_tabla_productos(productos: List[Producto]):
        print("+------------------------------------+")
        print("| No. |      Nombre de Producto      |")
        print("+------------------------------------+")

        ancho_celda = 28
        for i, producto in enumerate(productos):
            cant = Funcionalidad4.tiendaSelecta.cantidad_producto(producto)
            nombre_producto = f"{producto.nombre}. unidades en el inventario: {cant}"
            espacios = (ancho_celda - len(nombre_producto)) // 2
            padding_izquierdo = " " * espacios
            padding_derecho = " " * (ancho_celda - len(nombre_producto) - espacios)

            print(f"| {i + 1:>2} |{padding_izquierdo}{nombre_producto}{padding_derecho}|")
        print("+------------------------------------+")

    

    @staticmethod
    def seleccionar_tienda(usuario):

        print("------------------ REVISION DE TIENDA -----------------")
        
        if not usuario.tiendas:
            print("No tienes ninguna tienda registrada.")
            print("¿Qué desea hacer?")
            print("1. Cambiar de usuario")
            print("2. Volver al Menú principal")

            valor = Funcionalidad4.escaner(2)
            if valor == 1:
                # Aquí deberías incluir el código para cambiar de usuario
                pass
            elif valor == 2:
                # Aquí deberías incluir el código para volver al menú principal
                pass
            return
        
        print("Tiendas disponibles:")
        for idx, tienda in enumerate(usuario.tiendas):
            print(f"{idx + 1}. {tienda.nombre}")

        decs = Funcionalidad4.escaner(len(usuario.tiendas))
        tienda = usuario.tiendas[decs - 1]
        Funcionalidad4.tiendaSelecta = tienda
        Funcionalidad4.adminitrar_tienda(tienda)

    @staticmethod
    def adminitrar_tienda(tienda: Tienda):
        from gestorAplicacion.servicios.producto import Producto
        from gestorAplicacion.servicios.enums import EstadoProducto
        print("Seleccione una opción:")
        print("1. Total de productos en el inventario")
        print("2. Productos vencidos")
        print("3. Ver productos devueltos")
        print("4. Reabastecimiento")
        print("5. Seleccionar otra tienda")
        print("6. Volver al menú principal")

        opcion = Funcionalidad4.escaner(6)

        if opcion == 1:
            productos = tienda.obtener_todos_los_productos()
            productos_unicos = list({p.nombre: p for p in productos}.values())
            if productos_unicos:
                Funcionalidad4.print_tabla_productos(productos_unicos)
            else:
                print("La tienda no tiene ningún producto.")

            print("Seleccione una opción:")
            print("1. Seleccionar otra tienda")
            print("2. Volver al menú principal")
            print("3. Volver atrás")
            
            opcion_case1 = Funcionalidad4.escaner(3)
            if opcion_case1 == 1:
                # Aquí deberías incluir el código para seleccionar otra tienda
                pass
            elif opcion_case1 == 2:
                # Aquí deberías incluir el código para volver al menú principal
                pass
            elif opcion_case1 == 3:
                Funcionalidad4.adminitrar_tienda(tienda)

        elif opcion == 2:
            print("Productos vencidos recolectados:")
            productos_vencidos = tienda.get_productos_vencidos()
            if productos_vencidos:
                for producto in productos_vencidos:
                    print(f"{producto.nombre} {producto.marca} {producto.tamaño} {producto.estado}")

            print("Desea recolectar productos vencidos de los pasillos?")
            print("1. Sí")
            print("2. No")
            print("3. Seleccionar otra tienda")
            print("4. Volver al menú principal")
            print("5. Volver atrás")

            opcion_case2 = Funcionalidad4.escaner(5)
            if opcion_case2 == 1:
                tienda.vencer_producto()
                productos_vencidos = tienda.get_productos_vencidos()
                if productos_vencidos:
                    for producto in productos_vencidos:
                        print(producto.nombre)

                print("Seleccione una opción:")
                print("1. Seleccionar otra tienda")
                print("2. Volver al menú principal")
                print("3. Volver atrás")

                opcion_case2 = Funcionalidad4.escaner(3)
                if opcion_case2 == 1:
                    # Aquí deberías incluir el código para seleccionar otra tienda
                    pass
                elif opcion_case2 == 2:
                    # Aquí deberías incluir el código para volver al menú principal
                    pass
                elif opcion_case2 == 3:
                    Funcionalidad4.adminitrar_tienda(tienda)
            elif opcion_case2 == 2:
                print("Seleccione una opción:")
                print("1. Seleccionar otra tienda")
                print("2. Volver al menú principal")
                print("3. Volver atrás")

                opcion_case2 = Funcionalidad4.escaner(3)
                if opcion_case2 == 1:
                    # Aquí deberías incluir el código para seleccionar otra tienda
                    pass
                elif opcion_case2 == 2:
                    # Aquí deberías incluir el código para volver al menú principal
                    pass
                elif opcion_case2 == 3:
                    Funcionalidad4.adminitrar_tienda(tienda)
            elif opcion_case2 == 3:
                # Aquí deberías incluir el código para seleccionar otra tienda
                pass
            elif opcion_case2 == 4:
                # Aquí deberías incluir el código para volver al menú principal
                pass

        elif opcion == 3:
            print("Productos devueltos en la tienda:")
            productos_devueltos = tienda.get_productos_devueltos()
            if productos_devueltos:
                for producto in productos_devueltos:
                    print(f"{producto.nombre} Estado: {producto.estado}")

                print("Seleccione una opción:")
                print("1. Eliminar de la tienda los productos defectuosos")
                print("2. Devolver a los pasillos los productos activos")
                print("3. Seleccionar otra tienda")
                print("4. Volver al menú principal")
                print("5. Volver atrás")

                opcion_case3 = Funcionalidad4.escaner(5)
                if opcion_case3 == 1:
                    tienda.get_productos_devueltos().remove_if(lambda producto: producto.estado == EstadoProducto.DEFECTUOSO)
                    print("El dinero ya ha sido devuelto al cliente.")
                    print("Productos eliminados con éxito.")

                    print("Seleccione una opción:")
                    print("1. Seleccionar otra tienda")
                    print("2. Volver al menú principal")
                    print("3. Volver atrás")

                    opcion_casea = Funcionalidad4.escaner(3)
                    if opcion_casea == 1:
                        # Aquí deberías incluir el código para seleccionar otra tienda
                        pass
                    elif opcion_casea == 2:
                        # Aquí deberías incluir el código para volver al menú principal
                        pass
                    elif opcion_casea == 3:
                        Funcionalidad4.adminitrar_tienda(tienda)
                elif opcion_case3 == 2:
                    tienda.transferir_productos(productos_devueltos)
                    print("Productos devueltos al pasillo con éxito.")

                    print("Seleccione una opción:")
                    print("1. Seleccionar otra tienda")
                    print("2. Volver al menú principal")
                    print("3. Volver atrás")

                    opcion_casec = Funcionalidad4.escaner(3)
                    if opcion_casec == 1:
                        # Aquí deberías incluir el código para seleccionar otra tienda
                        pass
                    elif opcion_casec == 2:
                        # Aquí deberías incluir el código para volver al menú principal
                        pass
                    elif opcion_casec == 3:
                        Funcionalidad4.adminitrar_tienda(tienda)
                elif opcion_case3 == 3:
                    # Aquí deberías incluir el código para seleccionar otra tienda
                    pass
                elif opcion_case3 == 4:
                    # Aquí deberías incluir el código para volver al menú principal
                    pass
            else:
                print("No hay productos devueltos.")
                print("Seleccione una opción:")
                print("1. Seleccionar otra tienda")
                print("2. Volver al menú principal")
                print("3. Volver atrás")

                opcion_case3 = Funcionalidad4.escaner(3)
                if opcion_case3 == 1:
                    # Aquí deberías incluir el código para seleccionar otra tienda
                    pass
                elif opcion_case3 == 2:
                    # Aquí deberías incluir el código para volver al menú principal
                    pass
                elif opcion_case3 == 3:
                    Funcionalidad4.adminitrar_tienda(tienda)

        elif opcion == 4:
            print("Reabastecimiento de la tienda:")
            print("Ingrese los datos del producto a reabastecer:")

            nombre = input("Nombre del producto: ")
            marca = input("Marca del producto: ")
            tamaño = input("Tamaño del producto: ")
            cantidad = int(input("Cantidad a reabastecer: "))

            producto = Producto(nombre=nombre, marca=marca, tamaño=tamaño, estado=EstadoProducto.ACTIVO)
            Funcionalidad4.tiendaSelecta.agregar_producto(producto, cantidad)
            print(f"Producto {nombre} reabastecido con éxito.")

            print("Seleccione una opción:")
            print("1. Seleccionar otra tienda")
            print("2. Volver al menú principal")
            print("3. Volver atrás")

            opcion_case4 = Funcionalidad4.escaner(3)
            if opcion_case4 == 1:
                # Aquí deberías incluir el código para seleccionar otra tienda
                pass
            elif opcion_case4 == 2:
                # Aquí deberías incluir el código para volver al menú principal
                pass
            elif opcion_case4 == 3:
                Funcionalidad4.adminitrar_tienda(tienda)

        elif opcion == 5:
            # Aquí deberías incluir el código para seleccionar otra tienda
            pass
        elif opcion == 6:
            # Aquí deberías incluir el código para volver al menú principal
            pass

            # ------------------------------------------- # 

    # alerta de que el usuario no tiene tiendas 
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
    def ingresar(cls,window):   
        from .identidad import Identidad2
        usuario =Identidad2(window).identificar_persona()
        if not isinstance(usuario,Administrador):
            cls.mostrar_ventana()
            cls.ingresar(window)
        return usuario
    
    

    #muestra el frame donde se puede seleccionar la tienda ( aplicar a fieldframe de ser posible)
    def mostrar_frame(self, window, usuario ):

        # Frame para mostrar las tiendas
        frame_tiendas = tk.Frame(window)
        frame_tiendas.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

        # Crear botones para cada tienda
        for i, tienda in enumerate(usuario.get_tiendas()):
            nombre_tienda = tienda.getNombre()  # Obtener el nombre de la tienda
            boton_tienda = tk.Button(frame_tiendas, text=nombre_tienda, command=lambda t=tienda: self.seleccionar_tienda(t))
            boton_tienda.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        # Botón para confirmar la selección
        boton_confirmar = tk.Button(window, text="Confirmar")# command confirmar 
        boton_confirmar.pack(pady=10)

        # Iniciar el loop de tkinter
        window.mainloop()

    #guarda la seleccion en la variable
    def seleccionar_tienda(self, tienda):
        self.seleccion_tienda = tienda
        

    def procesar_seleccion(self, usuario):
        if not usuario.get_tiendas():  # Verifica si la lista de tiendas está vacía
            self.mostrar_ventana()
            return  # Finaliza la ejecución del método si no hay tiendas

        # Muestra la ventana para seleccionar una tienda
        self.mostrar_frame(usuario)

        # Espera a que el usuario seleccione una tienda
        # Al finalizar, `self.seleccion_tienda` debería tener la tienda seleccionada
        if self.seleccion_tienda is not None:
            self.administrar_tienda(self.seleccion_tienda)
        else:
            print("No se ha seleccionado ninguna tienda.")

    def administrar_tienda(self, tienda):
        # Aquí iría la lógica para administrar la tienda
        print(f"Administrando la tienda: {tienda.getNombre()}")