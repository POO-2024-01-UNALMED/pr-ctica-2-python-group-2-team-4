class Tienda:

    tiendas = []
    desempleados = []

    def __init__(self):
        pass

    def __init__(self, nit=None, dueno=None, nombre=None, saldo=0, estado="cerrado"):
        self.nit = nit
        self.dueno = dueno
        self.nombre = nombre
        self.saldo = saldo
        self.estado = estado
        self.carrito = None
        self.facturas = []
        self.proveedores = []
        self.cajas = []
        self.empleados = []
        self.pasillos = []
        self.productos_vencidos = []
        self.productos_devueltos = []
        Tienda.tiendas.append(self)

#COMO QUE IF DUENO, dueño no es un booleano
        if dueno:
            dueno.tiendas.append(self)

    # Getters and Setters

    def get_cajas(self):
        return self.cajas

    def set_cajas(self, cajas):
        self.cajas = cajas

    def get_nit(self):
        return self.nit

    def set_nit(self, nit):
        self.nit = nit

    def get_dueno(self):
        return self.dueno

    def set_dueno(self, dueno):
        self.dueno = dueno

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_empleados(self):
        return self.empleados

    def set_empleados(self, empleados):
        self.empleados = empleados

    def get_pasillos(self):
        return self.pasillos

    def set_pasillos(self, pasillos):
        self.pasillos = pasillos

    def get_proveedores(self):
        return self.proveedores

    def set_proveedores(self, proveedores):
        self.proveedores = proveedores

    @staticmethod
    def get_tiendas():
        return Tienda.tiendas

    @staticmethod
    def set_tiendas(tiendas):
        Tienda.tiendas = tiendas

    @staticmethod
    def get_desempleados():
        return Tienda.desempleados

    @staticmethod
    def set_desempleados(desempleados):
        Tienda.desempleados = desempleados

    def get_productos_vencidos(self):
        return self.productos_vencidos

    def set_productos_vencidos(self, productos_vencidos):
        self.productos_vencidos = productos_vencidos

    def get_facturas(self):
        return self.facturas

    def set_facturas(self, facturas):
        self.facturas = facturas

    def get_carrito(self):
        return self.carrito

    def set_carrito(self, carrito):
        self.carrito = carrito

    def get_productos_devueltos(self):
        return self.productos_devueltos

    def set_productos_devueltos(self, productos_devueltos):
        self.productos_devueltos = productos_devueltos

    # Métodos

    def subir_saldo(self, cantidad):
        self.saldo += cantidad

    def bajar_saldo(self, cantidad):
        self.saldo -= cantidad

    @staticmethod
    def buscar_tienda_categoria(categoria):
        tiendas_revisadas = Tienda.revision_tienda(Tienda.tiendas)
        tiendas_disp = [tienda for tienda in tiendas_revisadas if any(pasillo.categoria == categoria for pasillo in tienda.pasillos)]
        return len(tiendas_disp) > 0

    @staticmethod
    def buscar_tienda():
        if len(Tienda.tiendas) > 0:
            tiendas_revisadas = Tienda.revision_tienda(Tienda.tiendas)
            return len(tiendas_revisadas) > 0
        else:
            return False

    @staticmethod
    def categoria_tienda(categoria):
        tiendas_revisadas = Tienda.revision_tienda(Tienda.tiendas)
        tiendas_disp = [tienda for tienda in tiendas_revisadas if any(pasillo.categoria == categoria for pasillo in tienda.pasillos)]
        return tiendas_disp

    @staticmethod
    def revision_tienda(tienda_disp):
        return [tienda for tienda in tienda_disp if len(tienda.empleados) > 0 and tienda.disponibilidad_productos()]

    @staticmethod
    def tiendas_con_cliente(cliente):
        tiendas_con_cliente = {tienda for tienda in Tienda.tiendas for carrito in tienda.facturas if carrito.cliente == cliente}
        return list(tiendas_con_cliente)

    def buscar_producto(self, n):
        return "\n".join(f"{n}.{producto}" for pasillo in self.pasillos for producto in pasillo.productos)

    @staticmethod
    def buscar_productos(cliente, categoria, productos):
        ids = []
        for pasillo in cliente.tienda.pasillos:
            for producto in pasillo.productos:
                if producto.categoria == categoria and producto.id not in ids:
                    productos.append(producto)
                    ids.append(producto.id)
        return productos

    @staticmethod
    def buscar_productos_por_nombre(cliente, nombre):
        productos = []
        for pasillo in cliente.tienda.pasillos:
            for producto in pasillo.productos:
                if producto.nombre.lower().find(nombre.lower()) != -1 and producto.id not in [p.id for p in productos]:
                    productos.append(producto)
        return productos

    def disponibilidad_productos(self):
        return any(len(pasillo.productos) > 0 for pasillo in self.pasillos)

    def agregar_producto(self, producto):
        for pasillo in self.pasillos:
            if pasillo.categoria == producto.categoria:
                pasillo.agregar_producto(producto)
                return

    def agregar_producto_a_pasillo(self, producto, nombre_pasillo):
        for pasillo in self.pasillos:
            if pasillo.nombre == nombre_pasillo:
                pasillo.productos.append(producto)
                producto.tienda = self

    def obtener_todos_los_productos(self):
        return [producto for pasillo in self.pasillos for producto in pasillo.productos]

    @staticmethod
    def imprimir_producto(mayorn, mayorm, mayorp, mayorc, cantidad, producto):
        texto = f"  {producto.nombre}".ljust(mayorn + 4)
        texto += f"|  {producto.marca}/{producto.tamaño}".ljust(mayorm + 2)
        texto += f"|  {producto.precio}".ljust(mayorp + 2)
        texto += f"|  {cantidad}".ljust(mayorc + 2)
        return texto

    def cantidad_producto(self, producto):
        return sum(1 for pasillo in self.pasillos for prod in pasillo.productos if prod.id == producto.id)
