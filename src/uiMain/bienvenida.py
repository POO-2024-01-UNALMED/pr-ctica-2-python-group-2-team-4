
import os
import pathlib
from tkinter import BOTH, INSERT, X, Button, Frame, Label, PhotoImage, scrolledtext

from uiMain.interfaz import Iniciar_ventana_usuario


class Bienvenida(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window

        # Divisiones P3 y P4 en P1
        self.frame_p3 = Frame(self._window, height=180, padx=5, pady=5, bd=2, relief="solid",bg="#69a0ce")
        self.frame_p3.pack(fill=X, padx=5, pady=5)

        self.frame_p4 = Frame(self._window, height=500, padx=5, pady=5, bd=2, relief="solid",bg="#69a0ce")
        self.frame_p4.pack(fill=BOTH, expand=True, padx=5, pady=(5,0), anchor='s')

        self._next_el = 0

        saludo = Label(self.frame_p3, text="Bienvenido a My_Tiendita donde podrás realizar tus compras o administrar tus tiendas", font=("Helvetica", 10, "bold"),bg="#69a0ce")
        saludo.pack(pady=5)

        self.frame_aux =Frame(self.frame_p3, height=120,bg="#69a0ce")
        self.frame_aux.pack(fill=BOTH, expand=True)

        # self.saludo2.pack(fill=BOTH, expand=True, pady=5)
        self.saludo2 = scrolledtext.ScrolledText(self.frame_aux, height=8, width=77, padx=5)
        self.saludo2.tag_configure("center", justify="center")
        self.saludo2.insert(INSERT, "My_tiendita_2.0 es una aplicación de gestión avanzada de tiendas y compras en línea que ofrece una interfaz gráfica moderna y fácil de usar para una experiencia de usuario óptima. Los clientes pueden buscar productos de manera eficiente, ya sea por categoría o por nombre, lo que les permite encontrar rápidamente lo que necesitan. La aplicación facilita la gestión del carrito de compras, permitiendo agregar o eliminar productos con facilidad y pagar facturas de manera rápida y segura. Los usuarios tienen la flexibilidad de seleccionar entre distintas tiendas, adaptando su experiencia de compra a sus preferencias. Además, los propietarios de tiendas pueden administrar sus establecimientos de manera efectiva, gestionando productos y monitoreando el estado de las ventas. My_tiendita_2.0 combina funcionalidades avanzadas con un diseño intuitivo para proporcionar una solución completa en la gestión de tiendas y en la experiencia de compra en línea.")


        self._pantallazos = []
        for i in range(0,5):
            try:
                path = os.path.realpath('src\\assets\\pantallazos\\pantallazo'+str(i+1)+'.png')
                pantallazo = PhotoImage(file=path)
                self._pantallazos.append(pantallazo)
            except:
                try:
                    path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'src\\assets\\pantallazos\\pantallazo'+str(i+1)+'.png')
                    pantallazo = PhotoImage(file=path)
                    self._pantallazos.append(pantallazo)
                except:
                    pass
        self._label = Label(self.frame_p4, image=self._pantallazos[0], height=350, width=600,bg="#69a0ce")
        self._label.bind('<Leave>', self.proximo)
        self._label.pack(pady=5,fill="both", expand=True)

        button = Button(self.frame_p4, text="Inicio de aplicacion", command=self.abrir_ventana_principal)
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
        Iniciar_ventana_usuario()