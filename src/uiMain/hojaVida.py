import os
import pathlib
from tkinter import BOTH, INSERT, X, Frame, Label, PhotoImage, Text


class HojaVida(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, window):
        super().__init__(window)

        self.frame_p5 = Frame(window, height=180, padx=5, pady=5, bd=2, relief="solid",bg="#69a0ce")
        self.frame_p5.pack(fill=BOTH, padx=5, pady=5)

        self.frame_p6 = Frame(window, padx=5, pady=5, bd=2, relief="solid",bg="#69a0ce")
        self.frame_p6.pack(fill=BOTH, expand=True, padx=5, pady=5)

        self._text = None
        self._next_hv = 0
        self._photos = [None, None, None, None]
        self._labels = []
        self.cargar_hv(0)

        for i in range(0, 4):
            label = Label(self.frame_p6)
            (r, c) = HojaVida._posicion_imagen[i]
            label.grid(row=r, column=c, padx=5, pady=5)
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

        try:
            path = os.path.realpath('src\\assets\\'+png+'.png')
            photo = PhotoImage(file=path)
            # Redimensionar la imagen usando subsample
            photo = photo.subsample(2, 2)  # Ajusta los valores según sea necesario

            self._photos[numero] = photo  # Mantén la referencia a la imagen
            self._labels[numero].configure(image=photo)
            #self._labels[numero].image = photo
        except:
            try:
                path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src', 'assets',
                                    png + '.png')
                photo = PhotoImage(file=path)
                # Redimensionar la imagen usando subsample
                photo = photo.subsample(2, 2)  # Ajusta los valores según sea necesario

                self._photos[numero] = photo  # Mantén la referencia a la imagen
                self._labels[numero].configure(image=photo)
                #self._labels[numero].image = photo
            except:
                pass
        #if not os.path.exists(path):
        #    raise FileNotFoundError(f"Image file not found at path: {path}")


    def cargar_hv(self, numero):
        self._text = Text(self.frame_p5, height=10, width=77, bg="light blue", font=("Serif", 10, "bold"), wrap="word")
        self._text.pack(fill=BOTH)
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
        try:
            with open(os.path.realpath('src\\assets\\' + txt + ".txt"), "r+") as hv_text:
                self._text.insert(INSERT, hv_text.read())
        except:
            try:
                with open(os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),
                                       'src\\assets\\' + txt + ".txt"), "r+") as hv_text:
                    self._text.insert(INSERT, hv_text.read())
            except:
                pass

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