import os
import pathlib
from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.font import Font

from identidad import Identidad2

def iniciar_ventana_usuario():

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


    # Abre la pestana de dialogo con los nombres de los integrantes del equipo
    def open_popup():
        messagebox.showinfo("Titulo","Integrantes del equipo:\n- Jhorman Shair Ramirez Henao\n- Juan Esteban Pineda Henao\n- Juan Diego Ordoñez Londoño\n- Jordan Sanchez Torres")

    # Abre la pestana de dialogo con la informacion del programa y su funcionalidad.
    def aplicacion_popup():
        textonimo = "La aplicación My_Tiendita_2.0 es un software que permite la gestión de una tienda de tecnología. \n "
        messagebox.showinfo("Titulo descriptivo", textonimo)
    # ----------------------------------------------------------------------------------
    def salir():
        framesAMatar = []
        window.destroy()
        ventana = FieldFrame_2()
        ventana.crearVentana1()
        ventana.mainloop()

    def evento():
        pass

    def aceptarRepararProducto():
        #try:
            # servicio = Servicio.getServicios()[int(FFrepararProducto.getValue("ID Servicio"))]  # Comentado por error
            #pass
        #except ErrorAplicacion as e:
            # outputRepararProducto.insert(INSERT, str(e))  # Comentado por error
            pass

    # Ventana principal
    window = Tk()
    window.state('zoomed')
    window.title("My_Tiendita_2.0")

    # Icono de la ventana
    window.iconbitmap(os.path.join(pathlib.Path(__file__).parent.parent, 'assets', 'jhorman.ico'))
    window.option_add("*tearOff", FALSE)

    # Métodos sin argumentos para poder ejecutarlos-------------------------------------

    framesAMatar = []

    # Output de Generar cliente
    outputGenerarCliente = Text(window, height=3)
    framesAMatar.append(outputGenerarCliente)
    
    # Output de Liquidar el periodo
    outputLiquidarPeriodo = Text(window, height=6)
    framesAMatar.append(outputLiquidarPeriodo)
    
    #frame_a = Frame()  # master = window

    #frame_a.pack()
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

    zona2 = FieldFrame(window, "Criterios", ["Documento", "citerio2", "criterio3"], "Datos", ["Hola", None, None], ["normal","normal","normal"])
    def func2():
        matarloTodo(zona2)
    menuprocesos.add_command(label="Funcionalidad 2", command=func2)
    menuprocesos.add_command(label="Funcionalidad 4", command=func2)
    menuprocesos.add_command(label="identificarse", command=Identidad2(window).identificar_persona)
    
    menuayuda.add_command(label="Acerca de", command=open_popup)

    window['menu'] = menubar

    # Frame de creacion manual del cliente ------------------------------------------------------------
    window.resizable(True, True)

    cliente_manual = Frame(window, bd=10)
    nombre = Label(cliente_manual, text="Crear cliente manualmente", bd=10)
    # ----------------------------------------------------------------------------------

    descripcion = Label(cliente_manual,
                        text="Diligenciar la siguiente información para el correcto ingreso del cliente al sistema: ",
                        bd=10)

    output = Text(cliente_manual, height=3)
    framesAMatar.append(output)
    
    nombre.pack()
    # texto.pack()  # Comentado por error
    descripcion.pack()
    #crearCliente.pack(fill=BOTH, expand=True)
    framesAMatar.append(cliente_manual)

    # frame de funcionalidad 4-------------------------------------------------------------------

    frame_func4 = Frame(window)
    titilo_rol = Label(frame_func4, text="seleccion de rol", bd=10)
    seleccionId = Label(frame_func4, text="Ingrese su ID ", bd=10)
    
    # Frame de Reparar un producto-----------------------------------------------------
    repararProducto = Frame(window)
    nombreRepararProducto = Label(repararProducto, text="Reparar un producto", bd=10)
    dcrRepararProducto = Label(repararProducto, text="Ingrese el ID del servicio a reparar", bd=10)
    #FFrepararProducto = FieldFrame(repararProducto, None, ["ID Servicio"], None, [None], [], [1])
    outputRepararProducto = Text(repararProducto, height=3)
    framesAMatar.append(outputRepararProducto)

    def aceptarRepararProducto():
            # try:
            # servicio = Servicio.getServicios()[int(FFrepararProducto.getValue("ID Servicio"))]  # Comentado por error
            # pass
            # except ErrorAplicacion as e:
            # outputRepararProducto.insert(INSERT, str(e))  # Comentado por error
            pass

    #FFrepararProducto.crearBotones(aceptarRepararProducto)

    nombreRepararProducto.pack()
    dcrRepararProducto.pack()
    #FFrepararProducto.pack()
    framesAMatar.append(repararProducto)
    # ------------------------------------------------------------------------------------------------------
    window.mainloop()

class HojaVida(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, window):
        super().__init__(window)

        self.frame_p5 = Frame(window, height=180, padx=5, pady=5, bd=2, relief="solid",bg="light blue")
        self.frame_p5.pack(fill=X, padx=5, pady=5)

        self.frame_p6 = Frame(window, padx=5, pady=5, bd=2, relief="solid",bg="light blue")
        self.frame_p6.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self._text = None
        self._next_hv = 0
        self._photos = [None, None, None, None]
        self._labels = []
        self.cargar_hv(0)

        for i in range(0, 4):
            label = Label(self.frame_p6)
            (r, c) = HojaVida._posicion_imagen[i]
            label.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            self.frame_p6.grid_rowconfigure(r, weight=1)
            self.frame_p6.grid_columnconfigure(c, weight=1)
            self._labels.append(label)
            self.cargar_hv_imagen(0, i)
        self.pack()

    def cargar_hv_imagen(self, hv_num, numero):
        if self._next_hv==0:
            png="jhorman/foto"+str(numero+1)
        elif self._next_hv==1:
            png="juanes/foto"+str(numero+1)
        elif self._next_hv == 2:
            png = "juanDiego/foto"+str(numero+1)
        else:
            png="jordan/foto"+str(numero+1)
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src', 'assets', png+'.png')
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found at path: {path}")

        # Redimensionar la imagen usando subsample
        photo = PhotoImage(file=path)
        photo = photo.subsample(2, 2)  # Ajusta los valores según sea necesario

        self._photos[numero] = photo  # Mantén la referencia a la imagen
        self._labels[numero].configure(image=photo)
        self._labels[numero].image = photo

    def cargar_hv(self, numero):
        self._text = Text(self.frame_p5, height=10, width=77)
        self._text.pack(fill=BOTH, expand=True)
        self._text.bind('<Button>', self.proximo)

        #path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\jhorman.txt'.format(numero))
        if self._next_hv==0:
            txt="jhorman"
        elif self._next_hv==1:
            txt="juanes"
        elif self._next_hv == 2:
            txt = "juanDiego"
        else:
            txt="jordan"

        with open(os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\'+txt+".txt"), "r+") as hv_text:
            self._text.insert(INSERT, hv_text.read())

    def proximo(self, _):
        self._text.destroy()
        if self._next_hv < 3:
            self._next_hv = self._next_hv + 1
        else:
            self._next_hv = 0

        self._photos = [None, None, None, None]
        self.cargar_hv(self._next_hv)
        for i in range(0, 4):
            self.cargar_hv_imagen(self._next_hv, i)

class Bienvenida(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window

        # Divisiones P3 y P4 en P1
        self.frame_p3 = Frame(self._window, height=180, padx=5, pady=5, bd=2, relief="solid",bg="light blue")
        self.frame_p3.pack(fill=X, padx=5, pady=5)

        self.frame_p4 = Frame(self._window, height=500, padx=5, pady=5, bd=2, relief="solid",bg="light blue")
        self.frame_p4.pack(fill=BOTH, expand=True, padx=5, pady=(5,0), anchor='s')

        self._next_el = 0

        saludo = Label(self.frame_p3, text="Bienvenido a My_Tiendita donde podrás realizar tus compras o administrar tus tiendas", font=("Helvetica", 10, "bold"),bg="light blue")
        saludo.pack(pady=5)

        self.frame_aux =Frame(self.frame_p3, height=120,bg="light blue")
        self.frame_aux.pack(fill=BOTH, expand=True)

        # self.saludo2.pack(fill=BOTH, expand=True, pady=5)
        self.saludo2 = scrolledtext.ScrolledText(self.frame_aux, height=8, width=77, padx=5)
        self.saludo2.tag_configure("center", justify="center")
        self.saludo2.insert(INSERT, "Descripcion texto largo de software My_Tiendita")


        self._pantallazos = []
        for i in range(0,5):
            path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\pantallazos\\pantallazo'+str(i+1)+'.png')
            pantallazo = PhotoImage(file=path)
            self._pantallazos.append(pantallazo)

        self._label = Label(self.frame_p4, image=self._pantallazos[0], height=350, width=600)
        self._label.bind('<Leave>', self.proximo)
        self._label.pack(pady=5,fill="both", expand=True)

        button = Button(self.frame_p4, text="Aca se ira a la otra ventana", command=self.abrir_ventana_principal)
        button.pack(side="bottom", pady=5)

    # Actualiza el proximo pantallazo de la aplicacion
    def proximo(self, _):
        if self._next_el < 4:
            self._next_el = self._next_el + 1
        else:
            self._next_el = 0

        self._label.configure(image=self._pantallazos[self._next_el])
        self._label.image = self._pantallazos[self._next_el]

    # Carga la ventana principal del admin y cierra la ventana actual
    def abrir_ventana_principal(self):
        self._window.master.master.destroy()
        iniciar_ventana_usuario()

class FieldFrame_2(Tk):
    def poner_descripcion(self):
        saludo2 = self.bienvenida.saludo2
        if self.confirmacion:
            saludo2.pack_forget()
            self.confirmacion = False
        else:
            saludo2.pack(fill=BOTH, expand=True, pady=5)
            self.confirmacion = True
    
    def __init__(self):
        super().__init__()
    def crearVentana1(self):
        self.title("Ventana Principal de Inicio")
        self.state("zoomed")

        # Frame principal
        frame_principal = Frame(self, padx=10, pady=10, bd=2, relief="solid",bg="orange")
        frame_principal.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)
        inicio = Menu(self.menubar)
        self.confirmacion=False
        inicio.add_command(label="Descripcion", font=Font(family="Georgia", size=8, weight="bold"), command=self.poner_descripcion)
        inicio.add_command(label="Salir", font=Font(family="Georgia", size=8, weight="bold"), command=lambda: self.destroy())

        self.menubar.add_cascade(label="Inicio", menu=inicio)
        self.config(menu=self.menubar)

        # Divisiones P1 y P2
        frame_p1 = Frame(frame_principal,padx=5, pady=5, bd=2, relief="solid",bg="light blue")
        frame_p1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        frame_p2 = Frame(frame_principal, padx=5, pady=5, bd=2, relief="solid",bg="light blue")
        frame_p2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

        self.bienvenida = Bienvenida(frame_p1)
        self.hoja_vida = HojaVida(frame_p2)

if __name__ == "__main__":
    from fieldFrame import FieldFrame
    ventana = FieldFrame_2()
    ventana.crearVentana1()
    ventana.mainloop()

