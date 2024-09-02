class Proveedor:
    # Atributos estáticos
    seis_proveedores = []

    def __init__(self, nombre=None, entrega=None, tipo=None, tiendas=None):
        # Atributos de instancia
        self.nombre = nombre
        self.entrega = entrega if entrega is not None else []
        self.tipo = tipo
        self.tiendas = tiendas if tiendas is not None else []

        if self.tiendas:
            for tienda in self.tiendas:
                tienda.proveedores.append(self)

        Proveedor.seis_proveedores.append(self)

    # Getters y setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_entrega(self):
        return self.entrega

    def set_entrega(self, entrega):
        self.entrega = entrega

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tiendas(self):
        return self.tiendas

    def set_tiendas(self, tiendas):
        self.tiendas = tiendas

    @classmethod
    def get_seis_proveedores(cls):
        return cls.seis_proveedores

    @classmethod
    def set_seis_proveedores(cls, provs):
        cls.seis_proveedores = provs

    # Métodos adicionales
    def __str__(self):
        return f"{self.nombre} con categoría: {self.tipo.lower()}" if self.tipo else self.nombre

