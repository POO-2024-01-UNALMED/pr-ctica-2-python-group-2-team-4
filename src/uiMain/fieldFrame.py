from tkinter import*


class FieldFrame(Frame):
    def __init__(self, master ,tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(master)
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado

        label = Label(self, text="Proceso o Consulta", bd=10)
        descripcion = Label(self, text="Descripcion proceso/consulta", bd=10)
        label.pack()
        descripcion.pack()
        self.actualizacion()
        
    def actualizacion(self):
        Label(self, text=self._tituloCriterios).pack()
        Label(self, text=self._tituloValores).pack()
        for i in range(1, len(self._valores) + 1):
            Label(self, text=self._criterios[i - 1]).pack()
            if self._criterios[i - 1] in self._habilitado:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(self, width=40, textvariable=texto, state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(self, width=40, textvariable=texto, justify="center")

            entrada.pack()
            #self._entries.append(entrada)
