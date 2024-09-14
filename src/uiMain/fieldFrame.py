
import os
import pathlib
import tkinter
from tkinter import*
from tkinter import messagebox

import sys
sys.path.append('C:\\Users\\js682\\OneDrive\\Documentos\\pr-ctica-2-python-group-2-team-4\\src')

from identidad import Identidad, Identidad2


class FieldFrame(Frame):
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
            
        def identi():
            id=self._entrys[0].get()

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



