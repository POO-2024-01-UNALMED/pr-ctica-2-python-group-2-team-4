from tkinter import Frame, Label
class FieldFrame(Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__()
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
    def crearProceso(self):
        proceso = Frame(self)
        label = Label(self, text="Proceso o Consulta", bd=10)
        descripcion = Label(self, text="Descripcion proceso/consulta", bd=10)
        label.pack()
        descripcion.pack()
        #criterio = FieldFrame_2(self, None, ["ID Servicio"], None, [None], [], [1])
        #outputRepararProducto = Text(self, height=3)
        #framesAMatar.append(outputRepararProducto)
