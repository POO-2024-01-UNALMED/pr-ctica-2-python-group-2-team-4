
import os
import pathlib
import tkinter
from tkinter import*
from tkinter import messagebox

from uiMain.funcionalidad1 import Funcionalidad1


class FieldFrame(Frame):
    from uiMain.interfaz import FieldFrame_p
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado,
                 titulo="Proceso o Consulta", descripcion="Descripcion proceso/consulta", botones=True):
        super().__init__(master, bg="orange")
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        self._entrys = []

        # Frame para el nombre del proceso
        nombreProceso = Frame(self, relief=SOLID, bd=2, bg="light blue")
        nombreProceso.pack(pady=20, padx=10)
        proceso = Label(nombreProceso, text=titulo, font=("Arial", 30), bg="light blue",wraplength=500)
        proceso.pack(fill=BOTH, pady=10, padx=10)

        # Frame para la descripción del proceso
        descripProceso = Frame(self, relief=SOLID, bd=2, bg="light blue")
        descripProceso.pack(pady=20, padx=10)
        descripcionlabel = Label(descripProceso, text=descripcion, font=("Arial", 20), bg="light blue",wraplength=800)
        descripcionlabel.pack(pady=10, padx=10)

        # Frame para los campos
        self.campos = Frame(self, relief=SOLID, bd=2,pady=20, padx=10)
        self.campos.pack(pady=20, padx=20, expand=True, fill=BOTH)
        self.campos.columnconfigure(0, weight=1)
        self.campos.columnconfigure(1, weight=1)
        self.campos.columnconfigure(2, weight=1)
        self.campos.columnconfigure(3, weight=1)
        for i in range(len(self._valores)+2):
            self.campos.rowconfigure(i, weight=1)

        Label(self.campos, text=self._tituloCriterios, font=("Arial", 20), wraplength=500).grid(padx=10, column=1, row=0)
        Label(self.campos, text=self._tituloValores, font=("Arial", 20), wraplength=500).grid(row=0, column=2, padx=10, pady=10)

        for i in range(len(self._valores)):
            Label(self.campos, text=self._criterios[i], font=("Arial", 15)).grid(row=i + 1, column=1, padx=10)
            entry=Entry(self.campos, textvariable=self._valores[i], state='normal' if self._habilitado[i] else 'disabled', font=("Arial", 15))
            self._entrys.append(entry)
            entry.grid(row=i + 1, column=2, padx=10)

        # Botones de aceptar y borrar
        if botones:
            self.aceptar = Button(self.campos, text="Aceptar", font=("Arial", 15))
            self.aceptar.grid(row=len(self._valores) + 1, column=1, padx=10)
            self.borrar = Button(self.campos, text="Borrar", font=("Arial", 15), command=self.borrar)
            self.borrar.grid(row=len(self._valores) + 1, column=2, padx=10)

        #criterio = FieldFrame_2(self, None, ["ID Servicio"], None, [None], [], [1])
        #outputRepararProducto = Text(self, height=3)
        #framesAMatar.append(outputRepararProducto)

    def borrar(self):
        for entry in self._entrys:
            entry.delete(0, END)

    def iniciar_ventana_usuario(self):
        # Ventana principal
        window = Tk()
        window.state('zoomed')
        window.title("My_Tiendita_2.0")

        # Icono de la ventana
        window.iconbitmap(os.path.join(pathlib.Path(__file__).parent.parent, 'assets', 'jhorman.ico'))
        window.option_add("*tearOff", FALSE)

        # Métodos sin argumentos para poder ejecutarlos-------------------------------------

        framesAMatar = []

        def matarloTodo(frameUtilizado):
            for frame in framesAMatar:
                frame.pack_forget()  # Comentado por error
            frameUtilizado.pack(fill=BOTH, expand=True)

        def outPut(string, text):
            text.delete("1.0", "end")
            text.insert(INSERT, string)
            text.pack(fill=X, expand=True)

        def evtClienteManual():
            matarloTodo(cliente_manual)

        # Output de Generar cliente
        outputGenerarCliente = Text(window, height=3)
        framesAMatar.append(outputGenerarCliente)

        def evtGenerarCliente():
            # cliente = generarCliente()
            # outPut("Se genero el cliente ID: " + str(Cliente.clientes.index(cliente)) + " " + cliente.__str__(),
            #      outputGenerarCliente)
            matarloTodo(outputGenerarCliente)

        def evtSolicitarServicio():
            matarloTodo(solicitarServicio)

        def evtDiagnosticarProducto():
            matarloTodo(diagnosticarProducto)

        def evtRepararProducto():
            matarloTodo(repararProducto)

        def definir_rol():
            matarloTodo

        def event_definirRol():
            matarloTodo(frame_func4)

        def evtFinalizarServicio():
            matarloTodo(finalizarServicio)

        def evtCobrarServicio():
            matarloTodo(cobrarServicio)

        # Output de Liquidar el periodo
        outputLiquidarPeriodo = Text(window, height=6)
        framesAMatar.append(outputLiquidarPeriodo)

        def evtLiquidarPeriodo():
            pass

        # dependiente = Dependiente.getDependientes()[0]
        # stringqueseprintiara = "En la caja registradora hay " + str(
        #    dependiente.getCajaRegistradora().getDinero()) + "\n"
        # for liquidacion in dependiente.liquidar():
        #    stringqueseprintiara += liquidacion + "\n"
        # stringqueseprintiara += "\n\nEn la caja registradora quedan " + str(
        #    dependiente.getCajaRegistradora().getDinero()) + "\n"
        # outPut(stringqueseprintiara, outputLiquidarPeriodo)
        # matarloTodo(outputLiquidarPeriodo)

        # Output de mostrar clientes
        # outPutMostrarClientes = Text(window, height=len(Cliente.clientes))
        # framesAMatar.append(outPutMostrarClientes)

        # Evento para mostrar clientes
        def evtMostrarClientes():
            stri = ""
            # for i in range(len(Cliente.clientes)):
            #   stri += Cliente.clientes[i].__str__() + "\n"
            # if stri == "":
            #    stri = "No hay clientes registrados\n"
            # outPut(stri, outPutMostrarClientes)
            # matarloTodo(outPutMostrarClientes)

        # Output de mostrar servicios
        # outPutMostrarServicios = Text(window, height=len(Servicio.servicios))
        # framesAMatar.append(outPutMostrarServicios)

        # Evento para mostrar servicios
        def evtMostrarServicios():
            stri = ""
            # for i in range(len(Servicio.servicios)):
            #   stri += Servicio.servicios[i].__str__() + "\n"
            if stri == "":
                stri = "No hay servicios registrados\n"
            # outPut(stri, outPutMostrarServicios)
            # matarloTodo(outPutMostrarServicios)

        # Abre la pestana de dialogo con los nombres de los integrantes del equipo
        def open_popup():
            messagebox.showinfo("Titulo",
                                "Integrantes del equipo:\n- Jhorman Shair Ramirez Henao\n- Juan Esteban Pineda Henao\n- Juan Diego Ordoñez Londoño\n- Jordan Sanchez Torres")

        # Abre la pestana de dialogo con la informacion del programa y su funcionalidad.
        def aplicacion_popup():
            textonimo = "La aplicación My_Tiendita_2.0 es un software que permite la gestión de una tienda de tecnología. \n "
            messagebox.showinfo("Titulo descriptivo", textonimo)

        # ----------------------------------------------------------------------------------
        def salir():
            framesAMatar = []
            window.destroy()
            ventana = FieldFrame()
            ventana.mainloop()

        def evento():
            pass

        frame_a = Frame()  # master = window

        frame_a.pack()
        # Barra menu superior
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

        # submenu de procesos y consultas
        submenu = Menu(window)
        submenu.add_command(label="Crear cliente manualmente", command=evtClienteManual)

        menuarchivo.add_command(label="Aplicacion", command=aplicacion_popup)
        menuarchivo.add_command(label="Guardar y salir", command=salir)

        menuprocesos.add_cascade(label="Menu creaciones y destrucciones", menu=submenu)
        from uiMain.funcionalidad2 import Funcionalidad2
        menuprocesos.add_command(label="Funcionalidad 2", command=Funcionalidad2.elegir_tipo_busqueda())

        evtRepararProducto()

        menuprocesos.add_command(label="Funcionalidad 4", command=event_definirRol)

        menuayuda.add_command(label="Acerca de", command=open_popup)

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

        # VALOR DE ID = len(Cliente.clientes)
        # crearCliente = FieldFrame_p(cliente_manual, "Datos cliente", ["ID", "Nombre", "Cedula", "Cartera"], "Valor",
        #                         [len(Cliente.clientes), None, None, None], ["ID"], [1, 0, 1, 1])
        # crearCliente.grid_columnconfigure(0, weight=1)
        # crearCliente.grid_columnconfigure(1, weight=1)
        # crearCliente.grid_rowconfigure(0, weight=1)
        # crearCliente.grid_rowconfigure(1, weight=1)
        # crearCliente.grid_rowconfigure(2, weight=1)
        # crearCliente.grid_rowconfigure(3, weight=1)
        # crearCliente.grid_rowconfigure(4, weight=1)
        # crearCliente.grid_rowconfigure(5, weight=1)

        output = Text(cliente_manual, height=3)
        framesAMatar.append(output)

        def creacionCliente():
            pass
            # try:
            # cliente = Cliente(crearCliente.getValores())  # Comentado por error
            #    pass
            # except ErrorAplicacion as e:
            # output.insert(INSERT, str(e))  # Comentado por error
            #    pass

        # Creacion de los botones para aceptar y borrar de creacion manual de cliente
        # crearCliente.crearBotones(creacionCliente)  # Aceptar             Borrar

        nombre.pack()
        # texto.pack()  # Comentado por error
        interfaz_inicio.pack()
        descripcion.pack()
        # crearCliente.pack(fill=BOTH, expand=True)
        framesAMatar.append(cliente_manual)

        # --------------------------------------------------------------------------------

        # Frame de Solicitar servicio-----------------------------------------------------
        solicitarServicio = Frame(window)
        nombreSolicitarServicio = Label(solicitarServicio, text="Solicitar servicio", bd=10)
        dcrSolicitarServicio = Label(solicitarServicio,
                                     text="Ingrese el ID del cliente para solicitar la reparacion de su producto",
                                     bd=10)
        FFsolicitarServicio = FieldFrame_p(solicitarServicio, None, ["ID cliente"], None, [None], [], [1])
        outputsolicitarServicio = Text(solicitarServicio, height=3)
        framesAMatar.append(outputsolicitarServicio)

        def aceptarSolicitarServicio():
            pass

        # try:
        # cliente = Cliente.getClientes()[int(FFsolicitarServicio.getValue("ID cliente"))]  # Comentado por error
        #  pass
        # except ErrorAplicacion as e:
        # outputsolicitarServicio.insert(INSERT, str(e))  # Comentado por error
        #  pass

        FFsolicitarServicio.crearBotones(aceptarSolicitarServicio)

        nombreSolicitarServicio.pack()
        dcrSolicitarServicio.pack()
        FFsolicitarServicio.pack()
        framesAMatar.append(solicitarServicio)
        # -------------------------------------------------------------------------------
        # @summary Diagnostica el servicio seleccionado por el administrador.
        # Frame de Diagnosticar producto-----------------------------------------------------
        diagnosticarProducto = Frame(window)
        nombreDiagnosticarProducto = Label(diagnosticarProducto, text="Diagnosticar un producto", bd=10)
        dcrDiagnosticarProducto = Label(diagnosticarProducto, text="Ingrese el ID del servicio a diagnosticar", bd=10)
        FFdiagnosticarProducto = FieldFrame_p(diagnosticarProducto, None, ["ID Servicio"], None, [None], [], [1])
        outputDiagnosticarProducto = Text(diagnosticarProducto, height=7)
        framesAMatar.append(outputDiagnosticarProducto)

        def aceptarDiagnosticarProducto():
            # try:
            # servicio = Servicio.getServicios()[int(FFdiagnosticarProducto.getValue("ID Servicio"))]  # Comentado por error
            pass

        # except ErrorAplicacion as e:
        # outputDiagnosticarProducto.insert(INSERT, str(e))  # Comentado por error
        #    pass

        FFdiagnosticarProducto.crearBotones(aceptarDiagnosticarProducto)

        nombreDiagnosticarProducto.pack()
        dcrDiagnosticarProducto.pack()
        FFdiagnosticarProducto.pack()
        framesAMatar.append(diagnosticarProducto)
        # frame de funcionalidad 4-------------------------------------------------------------------

        frame_func4 = Frame(window)
        titilo_rol = Label(frame_func4, text="seleccion de rol", bd=10)
        seleccionId = Label(frame_func4, text="Ingrese su ID ", bd=10)
        titilo_rol.pack()
        seleccionId.pack()
        # Frame de Reparar un producto-----------------------------------------------------
        repararProducto = Frame(window)
        nombreRepararProducto = Label(repararProducto, text="Reparar un producto", bd=10)
        dcrRepararProducto = Label(repararProducto, text="Ingrese el ID del servicio a reparar", bd=10)
        FFrepararProducto = FieldFrame_p(repararProducto, None, ["ID Servicio"], None, [None], [], [1])
        outputRepararProducto = Text(repararProducto, height=3)
        framesAMatar.append(outputRepararProducto)

        def aceptarRepararProducto():
            # try:
            # servicio = Servicio.getServicios()[int(FFrepararProducto.getValue("ID Servicio"))]  # Comentado por error
            # pass
            # except ErrorAplicacion as e:
            # outputRepararProducto.insert(INSERT, str(e))  # Comentado por error
            pass

        FFrepararProducto.crearBotones(aceptarRepararProducto)

        nombreRepararProducto.pack()
        dcrRepararProducto.pack()
        FFrepararProducto.pack()
        framesAMatar.append(repararProducto)
        # -------------------------------------------------------------------------------

        # Frame de Finalizar un servicio-----------------------------------------------------
        finalizarServicio = Frame(window)
        nombreFinalizarServicio = Label(finalizarServicio, text="Finalizar un servicio", bd=10)
        dcrFinalizarServicio = Label(finalizarServicio, text="Ingrese el ID del servicio a finalizar", bd=10)
        FFfinalizarServicio = FieldFrame_p(finalizarServicio, None, ["ID Servicio"], None, [None], [], [1])
        outputFinalizarServicio = Text(finalizarServicio, height=6)
        framesAMatar.append(outputFinalizarServicio)

        def aceptarFinalizarServicio():
            # try:
            # index = FFfinalizarServicio.getValue("ID Servicio")  # Comentado por error
            # servicio = Servicio.getServicios()[int(index)]  # Comentado por error
            # pass
            # except ErrorAplicacion as e:
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
            # try:
            # servicio = Servicio.getServicios()[int(FFcobrarServicio.getValue("ID Servicio"))]  # Comentado por error
            # dependiente = Dependiente.getDependientes()[0]  # Comentado por error
            # pass
            # except ErrorAplicacion as e:
            # outputCobrarServicio.insert(INSERT, str(e))  # Comentado por error
            pass

        FFcobrarServicio.crearBotones(aceptarCobrarServicio)

        nombreCobrarServicio.pack()
        dcrCobrarServicio.pack()
        FFcobrarServicio.pack()
        framesAMatar.append(cobrarServicio)

        # ------------------------------------------------------------------------------------------------------
        window.mainloop()


