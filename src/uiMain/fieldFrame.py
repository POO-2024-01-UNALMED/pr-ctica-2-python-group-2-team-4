from tkinter import*


class FieldFrame(Frame):
    def __init__(self, master ,tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(master,bg="orange")
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado

        nombreProceso=Frame(self,relief=SOLID,bd=2)
        proceso=Label(nombreProceso, text="Proceso o Consulta",font=("Arial",30),bg="light blue")
        proceso.pack(fill=BOTH)
        nombreProceso.pack(fill=BOTH,padx=400,pady=20, anchor=N)

        descripProceso = Frame(self,relief=SOLID,bd=2)
        descripcion = Label(descripProceso, text="Descripcion proceso/consulta\npapap\n", font=("Arial",20),bg="light blue")
        descripcion.pack(fill=BOTH)
        descripProceso.pack(fill=BOTH,padx=150)

        self.actualizacion()
        
    def actualizacion(self):
        campos=Frame(self,relief=SOLID,bd=2)
        Label(campos, text=self._tituloCriterios,font=("Arial",20)).grid(padx=80, column=0, row=0)
        Label(campos, text=self._tituloValores,font=("Arial",20)).grid(padx=80, column=1, row=0)
        for i in range(1, len(self._valores) + 1):
            Label(campos, text=self._criterios[i - 1],font=("Arial",20)).grid(padx=80, pady=2, column=0, row=i)
            if self._criterios[i - 1] in self._habilitado:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(campos, width=40, textvariable=texto,font=("Arial",15), state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(campos, width=40, textvariable=texto,font=("Arial",15), justify="center")

            entrada.grid(pady=2, column=1, row=i)
            #self._entries.append(entrada)
        #campos.grid(row=2,columnspan=10)
        campos.pack(fill=BOTH,padx=300,pady=70,expand=True)
        aceptar = Button(campos, text="Aceptar",font=("Arial",15)).grid(pady = 50, column = 0, row = len(self._criterios)+1)
        borrar = Button(campos, text="Borrar",font=("Arial",15)).grid(pady = 50, column = 1, row = len(self._criterios)+1)

