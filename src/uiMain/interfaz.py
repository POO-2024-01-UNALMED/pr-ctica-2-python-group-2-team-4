import os
import pathlib
import tkinter
from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.font import Font
import sys
sys.path.append('C:\\Users\\js682\\OneDrive\\Documentos\\pr-ctica-2-python-group-2-team-4\\src')

from gestorAplicacion.servicios.proveedor import Proveedor
from gestorAplicacion.servicios.carrito import Carrito
from gestorAplicacion.sujetos.cliente import Cliente
from gestorAplicacion.sujetos.persona import Persona


from gestorAplicacion.servicios.caja import Caja
from gestorAplicacion.servicios.enums import Genero, Tamano, Edades, Categoria, TipoCaja
from gestorAplicacion.servicios.pasillo import Pasillo
from gestorAplicacion.servicios.producto import Producto
from gestorAplicacion.servicios.tienda import Tienda
from gestorAplicacion.sujetos.administrador import Administrador
from gestorAplicacion.sujetos.cajero import Cajero


from baseDatos.escritorLector import EscritorLector
from uiMain.ventana import Ventana


from uiMain.identidad import Identidad2
class FieldFrame_p(Frame):
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, tipos):
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        self._entries = list()
        self._tipos = tipos
        super().__init__(master)
        self.actualizacion()

    def actualizacion(self):
        Label(self, text=self._tituloCriterios).grid(padx=80, column=0, row=0)
        Label(self, text=self._tituloValores).grid(padx=80, column=1, row=0)
        for i in range(1, len(self._valores) + 1):
            Label(self, text=self._criterios[i - 1]).grid(padx=80, pady=2, column=0, row=i)
            if self._criterios[i - 1] in self._habilitado:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(self, width=40, textvariable=texto, state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(self, width=40, textvariable=texto, justify="center")

            entrada.grid(pady=2, column=1, row=i)
            self._entries.append(entrada)
    def borrarEntry(self):
        for entrada in self._entries:
            entrada.delete(0, "end")
    def crearBotones(self, comando1):
        aceptar = Button(self, text="Aceptar",command=comando1).grid(pady = 50, column = 0, row = len(self._criterios)+1)
        borrar = Button(self, text="Borrar",command=self.borrarEntry).grid(pady = 50, column = 1, row = len(self._criterios)+1)
class Iniciar_ventana_usuario():

    @classmethod
    def funcion2(cls,window):
        from uiMain.funcionalidad2 import Funcionalidad2
        from gestorAplicacion.sujetos.cliente import Cliente
        from gestorAplicacion.servicios.enums import Genero
        from gestorAplicacion.sujetos.persona import Persona

        cliente = None
        for persona in Persona.get_personas():
            if persona.get_nombre() == "Carlos":
                print(f"Bienvenido {persona.get_nombre()}")
                cliente = persona
        funcionalidad2 = Funcionalidad2()
        funcionalidad2.elegir_tipo_busqueda(cliente, window)

    @classmethod
    def funcion3(cls,window):
        from uiMain.funcionalidad3 import Funcionalidad3
        from gestorAplicacion.sujetos.cliente import Cliente
        from gestorAplicacion.servicios.enums import Genero
        from gestorAplicacion.sujetos.persona import Persona

        cliente = None
        for persona in Persona.get_personas():
            if persona.get_nombre() == "Carlos":
                print(f"Bienvenido {persona.get_nombre()}")
                cliente = persona
        tienda = cliente.get_tienda()
        if tienda is None:
            print("El cliente no está asociado a ninguna tienda.")
        else:
            # Crear productos
            producto1 = Producto(nombre="Manzanas", marca="Veracruz", tamano=Tamano.GRANDE,
                                 edad_valida=Edades.MENORES, categoria=Categoria.ALIMENTO, precio=2.5,
                                 tienda=tienda)
            producto2 = Producto(nombre="Pan", marca="Veracruz", tamano=Tamano.GRANDE, edad_valida=Edades.MENORES,
                                 categoria=Categoria.ALIMENTO, precio=1.5, tienda=tienda)
            producto3 = Producto(nombre="Leche", marca="Veracruz", tamano=Tamano.GRANDE, edad_valida=Edades.MENORES,
                                 categoria=Categoria.ALIMENTO, precio=3.0, tienda=tienda)
            for pasillo in tienda.get_pasillos():
                if pasillo.get_categoria() == Categoria.ALIMENTO:
                    pasillo.get_productos().append(producto1)
                    pasillo.get_productos().append(producto2)
                    pasillo.get_productos().append(producto3)
            # Crear carrito y agregar productos
            carrito = Carrito(tienda=tienda)
            carrito.get_productos().append(producto1)
            carrito.get_productos().append(producto2)
            carrito.get_productos().append(producto3)

            carrito.set_cliente(cliente)
            cliente.get_facturas().append(carrito)
            tienda.get_facturas().append(carrito)

        print(cliente.get_facturas())
        funcionalidad3 = Funcionalidad3()
        funcionalidad3.impresion_facturas(cliente, window)

    @classmethod
    def mostrar_funcionalidad_uno(cls, window):
        from uiMain.funcionalidad1 import Funcionalidad1
        funcionalidad1 = Funcionalidad1()
        funcionalidad1.ingresar(window)


        
    def __init__(self):
        def matarloTodo(frameUtilizado):
            for frame in framesAMatar:
                frame.pack_forget()  # Comentado por error
            frameUtilizado.pack(fill=BOTH, expand=True)

        def matarloTodo2():
            for frame in framesAMatar:
                frame.pack_forget()  # Comentado por error
            

        def outPut(string, text):
            text.delete("1.0", "end")
            text.insert(INSERT, string)
            text.pack(fill=X, expand=True)

        def evtClienteManual():
            matarloTodo(cliente_manual)

        """def evtGenerarCliente():
            #cliente = generarCliente()
            #outPut("Se genero el cliente ID: " + str(Cliente.clientes.index(cliente)) + " " + cliente.__str__(),
            #      outputGenerarCliente)
            matarloTodo(outputGenerarCliente)

        def evtSolicitarServicio():
            matarloTodo(solicitarServicio)

        def evtDiagnosticarProducto():
            matarloTodo(diagnosticarProducto)"""



        def definir_rol():
            matarloTodo    
            
        def event_definirRol():
            
            matarloTodo(frame_func4)

        def evtFinalizarServicio():
            matarloTodo(finalizarServicio)

        def evtCobrarServicio():
            matarloTodo(cobrarServicio)

        def evtLiquidarPeriodo():
            pass
        #dependiente = Dependiente.getDependientes()[0]
            #stringqueseprintiara = "En la caja registradora hay " + str(
            #    dependiente.getCajaRegistradora().getDinero()) + "\n"
            #for liquidacion in dependiente.liquidar():
            #    stringqueseprintiara += liquidacion + "\n"
            #stringqueseprintiara += "\n\nEn la caja registradora quedan " + str(
            #    dependiente.getCajaRegistradora().getDinero()) + "\n"
            #outPut(stringqueseprintiara, outputLiquidarPeriodo)
            #matarloTodo(outputLiquidarPeriodo)

        # Output de mostrar clientes
        #outPutMostrarClientes = Text(window, height=len(Cliente.clientes))
        #framesAMatar.append(outPutMostrarClientes)

        # Evento para mostrar clientes
        def evtMostrarClientes():
            stri = ""
            #for i in range(len(Cliente.clientes)):
            #   stri += Cliente.clientes[i].__str__() + "\n"
            #if stri == "":
            #    stri = "No hay clientes registrados\n"
            #outPut(stri, outPutMostrarClientes)
            #matarloTodo(outPutMostrarClientes)

        # Output de mostrar servicios
        #outPutMostrarServicios = Text(window, height=len(Servicio.servicios))
        #framesAMatar.append(outPutMostrarServicios)

        # Evento para mostrar servicios
        def evtMostrarServicios():
            stri = ""
            #for i in range(len(Servicio.servicios)):
            #   stri += Servicio.servicios[i].__str__() + "\n"
            if stri == "":
                stri = "No hay servicios registrados\n"
            #outPut(stri, outPutMostrarServicios)
            #matarloTodo(outPutMostrarServicios)

        # Abre la pestana de dialogo con los nombres de los integrantes del equipo
        def open_popup():
            messagebox.showinfo("Autores","Integrantes del equipo:\n- Jhorman Shair Ramirez Henao\n- Juan Esteban Pineda Henao\n- Juan Diego Ordoñez Londoño\n- Jordan Sanchez Torres")

        # Abre la pestana de dialogo con la informacion del programa y su funcionalidad.
        def aplicacion_popup():
            textonimo ="La función de My_tiendita_2.0 es gestionar una tienda virtual completa ofreciendo una experiencia de compra integral tanto para los clientes como para los administradores. Permite a los usuarios explorar, seleccionar y adquirir productos, ajustando el carrito de compras según restricciones de edad y saldo disponible. Facilita el proceso de pago, gestionando la selección de cajas, aplicando descuentos basados en membresías, y generando facturas detalladas. Además, supervisa el inventario y el estado financiero de la tienda, asegurando la calidad de los productos y tomando medidas para evitar déficits. Finalmente, permite a los usuarios adquirir y personalizar tiendas en bancarrota, reorganizando pasillos, reabasteciendo productos y contratando personal para revitalizar el negocio"
            messagebox.showinfo("Sobre la aplicacion", textonimo)
        # ----------------------------------------------------------------------------------
        def salir():
            framesAMatar = []
            window.destroy()
            ventana = Ventana()
            ventana.crearVentana1()
            ventana.mainloop()

        def evento():
            pass

        def creacionCliente():
            pass
            #try:
                # cliente = Cliente(crearCliente.getValores())  # Comentado por error
            #    pass
            #except ErrorAplicacion as e:
                # output.insert(INSERT, str(e))  # Comentado por error
            #    pass

        # Creacion de los botones para aceptar y borrar de creacion manual de cliente
        #crearCliente.crearBotones(creacionCliente)  # Aceptar             Borrar

        # --------------------------------------------------------------------------------

        # Frame de Solicitar servicio-----------------------------------------------------
        """solicitarServicio = Frame(window)
        nombreSolicitarServicio = Label(solicitarServicio, text="Solicitar servicio", bd=10)
        dcrSolicitarServicio = Label(solicitarServicio,
                                    text="Ingrese el ID del cliente para solicitar la reparacion de su producto", bd=10)
        FFsolicitarServicio = FieldFrame_p(solicitarServicio, None, ["ID cliente"], None, [None], [], [1])
        outputsolicitarServicio = Text(solicitarServicio, height=3)
        framesAMatar.append(outputsolicitarServicio)"""

        def aceptarSolicitarServicio():
            pass
        # try:
                # cliente = Cliente.getClientes()[int(FFsolicitarServicio.getValue("ID cliente"))]  # Comentado por error
            #  pass
            #except ErrorAplicacion as e:
                # outputsolicitarServicio.insert(INSERT, str(e))  # Comentado por error
            #  pass

        """FFsolicitarServicio.crearBotones(aceptarSolicitarServicio)

        nombreSolicitarServicio.pack()
        dcrSolicitarServicio.pack()
        FFsolicitarServicio.pack()
        framesAMatar.append(solicitarServicio)"""
        # -------------------------------------------------------------------------------
        # @summary Diagnostica el servicio seleccionado por el administrador.
        # Frame de Diagnosticar producto-----------------------------------------------------
        """diagnosticarProducto = Frame(window)
        nombreDiagnosticarProducto = Label(diagnosticarProducto, text="Diagnosticar un producto", bd=10)
        dcrDiagnosticarProducto = Label(diagnosticarProducto, text="Ingrese el ID del servicio a diagnosticar", bd=10)
        FFdiagnosticarProducto = FieldFrame_p(diagnosticarProducto, None, ["ID Servicio"], None, [None], [], [1])
        outputDiagnosticarProducto = Text(diagnosticarProducto, height=7)
        framesAMatar.append(outputDiagnosticarProducto)"""

        def aceptarDiagnosticarProducto():
            #try:
                # servicio = Servicio.getServicios()[int(FFdiagnosticarProducto.getValue("ID Servicio"))]  # Comentado por error
                pass
            #except ErrorAplicacion as e:
                # outputDiagnosticarProducto.insert(INSERT, str(e))  # Comentado por error
            #    pass
        def aceptarRepararProducto():
            #try:
                # servicio = Servicio.getServicios()[int(FFrepararProducto.getValue("ID Servicio"))]  # Comentado por error
                #pass
            #except ErrorAplicacion as e:
                # outputRepararProducto.insert(INSERT, str(e))  # Comentado por error
                pass
        """FFdiagnosticarProducto.crearBotones(aceptarDiagnosticarProducto)

        nombreDiagnosticarProducto.pack()
        dcrDiagnosticarProducto.pack()
        FFdiagnosticarProducto.pack()
        framesAMatar.append(diagnosticarProducto)"""

        # Ventana principal
        window = Tk()
        window.state('zoomed')
        window.title("My_Tiendita_2.0")

        # Icono de la ventana
        #window.iconbitmap(os.path.join(pathlib.Path(__file__).parent.parent, 'assets', 'jhorman.ico'))
        #window.option_add("*tearOff", FALSE)

        # Métodos sin argumentos para poder ejecutarlos-------------------------------------

        framesAMatar = []

        # Creacion de la barra de menu------------------------------------------------------
        menubar = Menu()

        menuarchivo = Menu(window)
        menuprocesos = Menu(window)
        menuayuda = Menu(window)

        menubar.add_cascade(menu=menuarchivo,
                            label='Archivo',
                            command=evento)
        menubar.add_cascade(menu=menuprocesos,
                            label='Procesos y Consultas',
                            command=evento)
        menubar.add_cascade(menu=menuayuda,
                            label='Ayuda',
                            command=evento)
        
        # Establecer la barra de menús en la ventana principal
        window.config(menu=menubar)

        # submenu de procesos y consultas

        menuarchivo.add_command(label="Aplicacion", command=aplicacion_popup)
        menuarchivo.add_command(label="Guardar y salir", command=salir)

        from uiMain.fieldFrame import FieldFrame
        zona2 = FieldFrame(window, "Criterios", ["Documento", "citerio2", "criterio3"], "Datos", ["Hola", None, None], ["normal","normal","normal"])




        # Función para mostrar el frame de Funcionalidad Uno


        # Añadir la opción en el menú para activar Funcionalidad Uno
        menuprocesos.add_command(label="Funcionalidad 1", command=lambda:self.mostrar_funcionalidad_uno(window))


        menuprocesos.add_command(label="Funcionalidad 2", command=lambda:self.funcion2(window))

        menuprocesos.add_command(label="Funcionalidad 3", command=lambda:self.funcion3(window))

        menuayuda.add_command(label="Acerca de", command=open_popup)

        from uiMain.funcionalidad4 import Funcionalidad4
        menuprocesos.add_command(label="Funcionalidad 4", command=lambda: prueba(window))

        from uiMain.funcionalidad5 import Funcionalidad5
        menuprocesos.add_command(label="Funcionalidad 5", command=lambda: prueba2(window))

        def prueba2(window):
            matarloTodo2()
            widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
            for i, widget in enumerate(widgets):
                if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                    widget.destroy()
            Funcionalidad5.ingresar(window)

        def prueba(window):
            proveedor1 = Proveedor(nombre="Proveedor de Alimentos", tipo=Categoria.ALIMENTO.get_texto())
            proveedor2 = Proveedor(nombre="Proveedor de Bebidas", tipo=Categoria.BEBIDA.get_texto())
            proveedor3 = Proveedor(nombre="Proveedor de Limpieza", tipo=Categoria.LIMPIEZA.get_texto())
            proveedor4 = Proveedor(nombre="Proveedor de Productos Personales", tipo=Categoria.PERSONAL.get_texto())
            proveedor5 = Proveedor(nombre="Proveedor de Hogar", tipo=Categoria.HOGAR.get_texto())
            proveedor6 = Proveedor(nombre="Proveedor de Electrónica", tipo=Categoria.ELECTRONICO.get_texto())

            # Create sample products for each category
            producto_alimento1 = Producto(nombre="Manzanas", marca="FreshFarms", precio=3.5, categoria="Alimento")
            producto_alimento2 = Producto(nombre="Leche", marca="La Vaquita", precio=2.0, categoria="Alimento")
            producto_bebida1 = Producto(nombre="Coca Cola", marca="Coca Cola", precio=1.5, categoria="Bebida")
            producto_bebida2 = Producto(nombre="Agua Mineral", marca="Nestlé", precio=1.0, categoria="Bebida")
            producto_limpieza1 = Producto(nombre="Detergente", marca="CleanMax", precio=5.0, categoria="Limpieza")
            producto_personal1 = Producto(nombre="Shampoo", marca="Herbal Essences", precio=6.0, categoria="Personal")
            producto_hogar1 = Producto(nombre="Sábanas", marca="HomeCollection", precio=20.0, categoria="Hogar")
            producto_electronico1 = Producto(nombre="Televisor", marca="Samsung", precio=300.0, categoria="Electrónico")

            # Assign products to their respective providers
            proveedor1.set_productos_proveedor([producto_alimento1, producto_alimento2])  # Alimentos
            proveedor2.set_productos_proveedor([producto_bebida1, producto_bebida2])  # Bebidas
            proveedor3.set_productos_proveedor([producto_limpieza1])  # Limpieza
            proveedor4.set_productos_proveedor([producto_personal1])  # Productos Personales
            proveedor5.set_productos_proveedor([producto_hogar1])  # Hogar
            proveedor6.set_productos_proveedor([producto_electronico1])  # Electrónica

            # Add these providers to the list of providers
            Proveedor.set_seis_proveedores([proveedor1, proveedor2, proveedor3, proveedor4, proveedor5, proveedor6])

            # Example to print the products for each provider
            for proveedor in Proveedor.get_seis_proveedores():
                print(f"Productos de {proveedor.nombre}:")
                for producto in proveedor.get_productos_proveedor():
                    print(f"- {producto._nombre}: ${producto._precio} c/u")


            matarloTodo2()
            funcionalidad = Funcionalidad4()
            widgets = window.winfo_children()  # Obtén todos los widgets en la ventana
            for i, widget in enumerate(widgets):
                if i >= 4:  # Si el índice es 3 o mayor, elimina el widget
                    widget.destroy()
            funcionalidad.ingresar(window)

        window['menu'] = menubar

        # Frame de creacion manual del cliente ------------------------------------------------------------
        window.resizable(True, True)

        cliente_manual = Frame(window, bd=10)
        nombre = Label(cliente_manual, text="Crear cliente manualmente", bd=10)

        # Interfaz de inicio----------------------------------------------------------------
        interfaz_inicio = Inicio(window)

        framesAMatar.append(interfaz_inicio)
        # ----------------------------------------------------------------------------------

        descripcion = Label(cliente_manual,
                            text="Diligenciar la siguiente información para el correcto ingreso del cliente al sistema: ",
                            bd=10)

        nombre.pack()
        # texto.pack()  # Comentado por error
        interfaz_inicio.pack()
        descripcion.pack()
        #crearCliente.pack(fill=BOTH, expand=True)
        framesAMatar.append(cliente_manual)

        # frame de funcionalidad 4-------------------------------------------------------------------

        frame_func4 = Frame(window)
        titilo_rol = Label(frame_func4, text="seleccion de rol", bd=10)
        seleccionId = Label(frame_func4, text="Ingrese su ID ", bd=10)
        
        # Frame de Reparar un producto-----------------------------------------------------

        #nombreRepararProducto = Label(repararProducto, text="Reparar un producto", bd=10)
        #dcrRepararProducto = Label(repararProducto, text="Ingrese el ID del servicio a reparar", bd=10)
        #FFrepararProducto = FieldFrame_p(repararProducto, None, ["ID Servicio"], None, [None], [], [1])
        #outputRepararProducto = Text(repararProducto, height=3)
        #framesAMatar.append(outputRepararProducto)

        """nombreRepararProducto.pack()
        dcrRepararProducto.pack()"""
        #FFrepararProducto.pack()
        #framesAMatar.append(repararProducto)
        # -------------------------------------------------------------------------------

        # Frame de Finalizar un servicio-----------------------------------------------------
        finalizarServicio = Frame(window)
        nombreFinalizarServicio = Label(finalizarServicio, text="Finalizar un servicio", bd=10)
        dcrFinalizarServicio = Label(finalizarServicio, text="Ingrese el ID del servicio a finalizar", bd=10)
        FFfinalizarServicio = FieldFrame_p(finalizarServicio, None, ["ID Servicio"], None, [None], [], [1])
        outputFinalizarServicio = Text(finalizarServicio, height=6)
        framesAMatar.append(outputFinalizarServicio)

        def aceptarFinalizarServicio():
            #try:
                # index = FFfinalizarServicio.getValue("ID Servicio")  # Comentado por error
                # servicio = Servicio.getServicios()[int(index)]  # Comentado por error
                #pass
            #except ErrorAplicacion as e:
                # outputFinalizarServicio.insert(INSERT, str(e))  # Comentado por error
                pass

        FFfinalizarServicio.crearBotones(aceptarFinalizarServicio)

        nombreFinalizarServicio.pack()
        dcrFinalizarServicio.pack()
        FFfinalizarServicio.pack()
        framesAMatar.append(finalizarServicio)
        # -------------------------------------------------------------------------------

        # Frame de Cobrar un servicio-----------------------------------------------------
        cobrarServicio = Frame(window)
        nombreCobrarServicio = Label(cobrarServicio, text="Cobrar un servicio", bd=10)
        dcrCobrarServicio = Label(cobrarServicio, text="Ingrese el ID del servicio a cobrar", bd=10)
        FFcobrarServicio = FieldFrame_p(cobrarServicio, None, ["ID Servicio"], None, [None], [], [1])
        outputCobrarServicio = Text(cobrarServicio, height=3)
        framesAMatar.append(outputCobrarServicio)

        def aceptarCobrarServicio():
            #try:
                # servicio = Servicio.getServicios()[int(FFcobrarServicio.getValue("ID Servicio"))]  # Comentado por error
                # dependiente = Dependiente.getDependientes()[0]  # Comentado por error
                #pass
            #except ErrorAplicacion as e:
                # outputCobrarServicio.insert(INSERT, str(e))  # Comentado por error
                pass

        FFcobrarServicio.crearBotones(aceptarCobrarServicio)

        nombreCobrarServicio.pack()
        dcrCobrarServicio.pack()
        FFcobrarServicio.pack()
        framesAMatar.append(cobrarServicio)

        # ------------------------------------------------------------------------------------------------------
        window.mainloop()

class Inicio(Frame):
    def __init__(self, window):
        super().__init__(window)
        text = scrolledtext.ScrolledText(self,height=100,width=300)
        text.pack()
        path = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),"instrucciones.txt")
        with open(path, "r+") as instrucciones:
            text.insert(INSERT, instrucciones.read())
        text.tag_configure('center', justify='center')




if __name__ == "__main__":
    EscritorLector.deserializarTodo()

    """
    for tienda in admin1.get_tiendas():
        print(tienda.get_nombre())
   

    cliente = None
    for persona in Persona.get_personas():  # Asegúrate de que `Persona.get_personas()` devuelva todos los clientes
        if persona.get_nombre()== "Carlos":
            cliente = persona
            break


    print(cliente)
    if cliente is None:
        print("Cliente no encontrado.")
    else:
        print(f"Bienvenido {cliente.get_nombre()}")

        # Obtener la tienda del cliente
        tienda = cliente.get_tienda()

        for t in tienda.get_cajas():
            tienda.get_empleados().append(t.get_cajero())
        print(len(tienda.get_empleados()))
        print(tienda.get_nombre())
        if tienda is None:
            print("El cliente no está asociado a ninguna tienda.")
        else:
            # Crear productos
            producto1 = Producto(nombre="Manzanas", precio=2.5, tienda=tienda)
            producto2 = Producto(nombre="Pan", precio=1.5, tienda=tienda)
            producto3 = Producto(nombre="Leche", precio=3.0, tienda=tienda)

            # Crear carrito y agregar productos
            carrito = Carrito(tienda=tienda)
            carrito.get_productos().append(producto1)
            carrito.get_productos().append(producto2)
            carrito.get_productos().append(producto3)

            cliente.get_facturas().append(carrito)
            tienda.get_facturas().append(carrito)

            print(cliente.get_facturas())
            print(tienda.get_facturas())
            # El carrito ya se ha agregado a la lista de facturas del cliente y de la tienda
            print("Carrito creado y productos añadidos con éxito.")
            print(f"Total del carrito: {carrito.calcular_total()}")
            """
    ventana = Ventana()
    ventana.crearVentana1()
    ventana.mainloop()
    from uiMain.fieldFrame import FieldFrame

