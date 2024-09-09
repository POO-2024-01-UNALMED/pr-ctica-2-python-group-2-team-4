import os
import pathlib
from tkinter import *
from tkinter import scrolledtext
from tkinter.font import Font


def iniciar_ventana_usuario():
    # Ventana principal
    window = Tk()
    window.geometry("750x680")
    window.title("My_Tiendita_2.0")
    window.option_add("*tearOff", FALSE)

    # Métodos sin argumentos para poder ejecutarlos-------------------------------------

    framesAMatar = []


    def matarloTodo(frameUtilizado):

        for frame in framesAMatar:
            frame.pack_forget()
        frameUtilizado.pack(fill=BOTH, expand=True)

class Inicio(Frame):
    def __init__(self, window):
        super().__init__(window)
        text = scrolledtext.ScrolledText(self)
        path = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),"instrucciones.txt")
        with open(path, "r+") as instrucciones:
            text.insert(INSERT, instrucciones.read())
        text.tag_configure('center', justify='center')
        text.pack()

class HojaVida(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]
    def __init__(self, window):
        super().__init__(window)
        self._p5 = Frame(self,background="purple",bd=3, relief="solid",pady=10,padx=10)
        self._p6 = Frame(self,background="green",bd=3, relief="solid",pady=10,padx=10)
        self._text = None
        self._next_hv = 0
        self._photos = [None, None, None, None]
        self._labels = []
        self.cargar_hv(0)
        for i in range(0, 4):
            label = Label(self._p6, width=300, height=261)
            (r, c) = HojaVida._posicion_imagen[i]
            label.grid(row=r, column=c)
            self._labels.append(label)
            # Se cargan las primeras imagenes
            self.cargar_hv_imagen(0, i)
        self._p5.grid(sticky="nsew")
        self._p6.grid(sticky="nsew")


    # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    def proximo(self, _):
        if self._next_hv < 3:
            self._next_hv = self._next_hv + 1
        else:
            self._next_hv = 0

        self._photos = [None, None, None, None]
        self.cargar_hv(self._next_hv)
        for i in range(0, 4):
            self.cargar_hv_imagen(self._next_hv, i)

    # Carga el component imagen que sirve para mostrar las fotos
    def cargar_hv_imagen(self, hv_num, numero):
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src', 'assets', 'jhorman.png')
        photo = PhotoImage(file=path)
        self._photos[numero] = photo  # Mantén la referencia a la imagen
        self._labels[numero].configure(image=photo)
        self._labels[numero].image = photo

    # Carga el texto para la hoja de vida respecto al numero asignado
    def cargar_hv(self, numero):
        self._text = Text(self._p5,height=5)
        self._text.grid(row=1, column=0,sticky="nsew")
        self._text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\jhorman.txt'.format(numero))

        with open(path, "r+") as hv_text:
            self._text.insert(INSERT, hv_text.read())

class Bienvenida(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._p3 = Frame(self,background="blue",bd=3, relief="solid",padx=10,height=110,width=780)
        self._p4 = Frame(self,background="red",bd=3, relief="solid",pady=5,padx=10)
        self._next_el = 0
        saludo = Entry(self._p3, width=128)
        self.saludo2 = scrolledtext.ScrolledText(self._p3, height=5, width=94)
        self.saludo2.tag_configure("center", justify="center")
        saludo.insert(INSERT, "Bienvenido al software de My_Tiendita")
        self.saludo2.insert(INSERT, "Descripcion texto largo de sowftware My_Tiendita")
        saludo.place(x=-10, y=0)
        self._pantallazos = []
        for i in range(0, 5):
            path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\assets\\pantallazo.png'.format(i))
            pantallazo = PhotoImage(file=path)
            self._pantallazos.append(pantallazo)

        self._label = Label(self._p4, image=self._pantallazos[0], height=500, width=750)
        self._label.bind('<Enter>', self.proximo)
        self._label.pack(pady=5)

        button = Button(self._p4, text="Aca se ira a la otra ventana", command=self.abrir_ventana_principal)
        button.pack(side="bottom")
        self._p3.grid()
        self._p4.grid()

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
        self._window.master.destroy()
        iniciar_ventana_usuario()

class VentanaInicio(Tk):
    def __init__(self):
        super().__init__()
        self.title('Ventana Principal de Inicio')
        self.option_add("*tearOff", False)
        self.menubar = Menu(self)
        inicio = Menu(self.menubar)
        inicio.add_command(label="Descripcion",font=Font(family="Georgia", size=8, weight="bold"), command=lambda: self.bienvenida.saludo2.place(x=-10, y=20))
        inicio.add_command(label="Salir",font=Font(family="Georgia", size=8, weight="bold"), command=lambda: self.destroy())

        self.menubar.add_cascade(label="Inicio", menu=inicio)
        self.config(menu=self.menubar)
        frame1 = Frame(self,bd=3, relief="solid")
        frame2 = Frame(self,bd=3, relief="solid")
        frame1.pack(side="left",fill="both",pady=20,padx=20)
        frame2.pack(side="right",fill="both",pady=20,padx=20)
        self.bienvenida = Bienvenida(frame1)
        self.hoja_vida = HojaVida(frame2)
        self.bienvenida.pack()
        self.hoja_vida.pack()

class FieldFrame(Frame):
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

if __name__ == "__main__":
    ventana = VentanaInicio()
    ventana.mainloop()