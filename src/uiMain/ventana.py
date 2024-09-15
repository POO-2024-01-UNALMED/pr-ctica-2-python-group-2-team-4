from tkinter import*
from tkinter.font import Font

class Ventana(Tk):
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

        from .bienvenida import Bienvenida
        from .hojaVida import HojaVida
        self.bienvenida = Bienvenida(frame_p1)
        self.hoja_vida = HojaVida(frame_p2)