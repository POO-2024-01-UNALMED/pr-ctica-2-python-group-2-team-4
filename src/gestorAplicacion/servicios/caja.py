class Caja:
    # Atributos
    def __init__(self, nombre=None, tipo=None, tienda=None):
        self._nombre = nombre
        self._estado = 2
        self._tipo = tipo
        self._tienda = tienda
        self._cajero = None
        self._cliente = None

        # Si la tienda no es None, añade esta caja a la lista de cajas de la tienda
        if tienda is not None:
            tienda.get_cajas().append(self)

    # Getters y Setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre


    def get_estado(self):
        return self._estado


    def set_estado(self, estado):
        self._estado = estado


    def get_tipo(self):
        return self._tipo


    def set_tipo(self, tipo):
        self._tipo = tipo


    def get_tienda(self):
        return self._tienda


    def set_tienda(self, tienda):
        self._tienda = tienda


    def get_cajero(self):
        return self._cajero


    def set_cajero(self, cajero):
        self._cajero = cajero


    def get_cliente(self):
        return self._cliente


    def set_cliente(self, cliente):
        self._cliente = cliente

   