from tkinter import*


class FieldFrame(Frame):
    def __init__(self, master ,tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(master,bg="light blue")
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado

        nombreProceso=Frame(self,relief="solid",bg="orange")
        proceso=Label(nombreProceso, text="Proceso o Consulta",font=("Arial",30), bd=10)
        proceso.pack()
        nombreProceso.pack(fill="x",pady=20,padx=400)

        descripProceso = Frame(self,relief="solid")
        descripcion = Label(descripProceso, text="Descripcion proceso/consulta", font=("Arial",20),bg="orange", bd=10)
        descripcion.pack()
        descripProceso.pack(fill="x",pady=20,padx=150)

        self.actualizacion()
        
    def actualizacion(self):
        campos=Frame(self,relief="solid")
        Label(campos, text=self._tituloCriterios).grid(padx=80, column=0, row=0)
        Label(campos, text=self._tituloValores).grid(padx=80, column=1, row=0)
        for i in range(1, len(self._valores) + 1):
            Label(campos, text=self._criterios[i - 1]).grid(padx=80, pady=2, column=0, row=i)
            if self._criterios[i - 1] in self._habilitado:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(campos, width=40, textvariable=texto, state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i - 1])
                entrada = Entry(campos, width=40, textvariable=texto, justify="center")

            entrada.grid(pady=2, column=1, row=i)
            #self._entries.append(entrada)
        #campos.grid(row=2,columnspan=10)
        campos.pack(fill=BOTH,pady=70,padx=300,expand=True)
