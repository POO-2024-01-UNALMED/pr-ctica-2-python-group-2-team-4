class Proveedor:
    # Atributos estáticos
    seis_proveedores = []

    def __init__(self, nombre=None, entrega=None, tipo=None, tiendas=None, productos_proveedor=None):
        # Atributos de instancia
        self.nombre = nombre
        self.entrega = entrega if entrega is not None else []
        self.tipo = tipo
        self.tiendas = tiendas if tiendas is not None else []
        if productos_proveedor is None:
            self.productos_proveedor = []  # Corregido el nombre del atributo
        else:
            self.productos_proveedor = productos_proveedor  
        #     for tienda in self.tiendas:
        #         tienda.get_proveedores().append(self)

        # Proveedor.seis_proveedores.append(self)

    # Getters y setters

    def get_productos_proveedor(self):
        return self.productos_proveedor  # Corregido aquí

    def set_productos_proveedor(self, productos):
        self.productos_proveedor = productos

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
    @classmethod
    def listar_proveedores(cls):
        n=1
        s=list()
        for proveedor in cls.seis_proveedores:
            s.append("\n"+n+"."+proveedor.nombre)
            s.append("     ")
            s.append(proveedor.tipo)
            n+=1
        return str(s)
            
    def __str__(self):
        return f"{self.nombre} con categoría: {self.tipo.lower()}" if self.tipo else self.nombre

