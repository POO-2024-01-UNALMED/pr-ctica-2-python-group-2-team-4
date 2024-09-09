import os
import pathlib
from tkinter import *
from tkinter import scrolledtext
from tkinter.font import Font


def iniciar_ventana_usuario():
    # Ventana principal
    window = Tk()
    window.state('zoomed')
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

        self.frame_p5 = Frame(self, height=180, padx=5, pady=5, bd=2, relief="solid")
        self.frame_p5.pack(fill=X, padx=5, pady=5)

        self.frame_p6 = Frame(self, padx=5, pady=5, bd=2, relief="solid")
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

    def cargar_hv_imagen(self, hv_num, numero):
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src', 'assets', 'jhorman.png')
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
        self._text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\jhorman.txt'.format(numero))

        with open(path, "r+") as hv_text:
            self._text.insert(INSERT, hv_text.read())

    def proximo(self, _):
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
        self.frame_p3 = Frame(self._window, height=180, padx=5, pady=5, bd=2, relief="solid")
        self.frame_p3.pack(fill=X, padx=5, pady=10)

        self.frame_p4 = Frame(self._window, height=500, padx=5, pady=5, bd=2, relief="solid")
        self.frame_p4.pack(fill=BOTH, expand=True, padx=5, pady=(0, 5), anchor='s')

        self._next_el = 0

        saludo = Label(self.frame_p3, text="Bienvenido a My_Tiendita donde podrás realizar tus compras o administrar tus tiendas", font=("Helvetica", 10, "bold"))
        saludo.pack(pady=5)

        

        frame_aux =Frame(self.frame_p3, height=120)
        frame_aux.pack(fill=BOTH, expand=True, pady=5)

        # self.saludo2.pack(fill=BOTH, expand=True, pady=5)
        self.saludo2 = scrolledtext.ScrolledText(frame_aux, height=8, width=77, padx=5, pady=5)
        self.saludo2.tag_configure("center", justify="center")
        self.saludo2.insert(INSERT, "Descripcion texto largo de software My_Tiendita")


        self._pantallazos = []
        for i in range(0, 5):
            path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\pantallazo.png'.format(i))
            pantallazo = PhotoImage(file=path)
            self._pantallazos.append(pantallazo)

        self._label = Label(self.frame_p4, image=self._pantallazos[0], height=350, width=600)
        self._label.bind('<Enter>', self.proximo)
        self._label.pack(pady=5)

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
        self._window.master.destroy()
        iniciar_ventana_usuario()

class VentanaInicio(Tk):
    def __init__(self):
        super().__init__()

        self.title("Ventana Principal de Inicio")
        self.state("zoomed")

        # Frame principal
        frame_principal = Frame(self, padx=10, pady=10, bd=2, relief="solid")
        frame_principal.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)
        inicio = Menu(self.menubar)
        inicio.add_command(label="Descripcion", font=Font(family="Georgia", size=8, weight="bold"), command=lambda: self.bienvenida.saludo2.pack(fill=BOTH, expand=True, pady=5))
        inicio.add_command(label="Salir", font=Font(family="Georgia", size=8, weight="bold"), command=lambda: self.destroy())

        self.menubar.add_cascade(label="Inicio", menu=inicio)
        self.config(menu=self.menubar)

        # Divisiones P1 y P2
        frame_p1 = Frame(frame_principal, padx=5, pady=5, bd=2, relief="solid")
        frame_p1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        frame_p2 = Frame(frame_principal, padx=5, pady=5, bd=2, relief="solid")
        frame_p2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

        self.bienvenida = Bienvenida(frame_p1)
        self.hoja_vida = HojaVida(frame_p2)
        self.bienvenida.pack(fill=BOTH, expand=True)
        self.hoja_vida.pack(fill=BOTH, expand=True)

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