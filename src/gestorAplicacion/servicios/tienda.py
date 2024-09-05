
class Tienda:

    tiendas = []
    desempleados = []
    def __init__(self, nombre=None, pasillos=None, nit=None, dueno=None, saldo=0, estado="cerrado"):
        self._nit = nit
        self._dueno = dueno
        if dueno is  not None:
            dueno.tiendas.append(self)
        self._nombre = nombre
        self._saldo = saldo
        self._estado = estado
        self._carrito = None
        self._facturas = []
        self._proveedores = []
        self._cajas = []
        self._empleados = []
        if pasillos is None:
            self._pasillos = []
        else:
            self._pasillos = pasillos
            for pasillo in pasillos:
                pasillo.set_tienda(self)
        self._productos_vencidos = []
        self._productos_devueltos = []
        Tienda.tiendas.append(self)

#COMO QUE IF DUENO, dueño no es un booleano
        if dueno is not None:
            dueno.get_tiendas().append(self)

    # Getters and Setters

    def get_cajas(self):
        return self._cajas

    def set_cajas(self, cajas):
        self._cajas = cajas

    def get_nit(self):
        return self._nit

    def set_nit(self, nit):
        self._nit = nit

    def get_dueno(self):
        return self._dueno

    def set_dueno(self, dueno):
        self._dueno = dueno

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_empleados(self):
        return self._empleados

    def set_empleados(self, empleados):
        self._empleados = empleados

    def get_pasillos(self):
        return self._pasillos

    def set_pasillos(self, pasillos):
        self._pasillos = pasillos

    def get_proveedores(self):
        return self._proveedores

    def set_proveedores(self, proveedores):
        self._proveedores = proveedores

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
        return self._productos_vencidos

    def set_productos_vencidos(self, productos_vencidos):
        self._productos_vencidos = productos_vencidos

    def get_facturas(self):
        return self._facturas

    def set_facturas(self, facturas):
        self._facturas = facturas

    def get_carrito(self):
        return self._carrito

    def set_carrito(self, carrito):
        self._carrito = carrito

    def get_productos_devueltos(self):
        return self._productos_devueltos

    def set_productos_devueltos(self, productos_devueltos):
        self._productos_devueltos = productos_devueltos

    # Métodos

    def subir_saldo(self, cantidad):
        self._saldo += cantidad

    def bajar_saldo(self, cantidad):
        self._saldo -= cantidad

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
        return "\n".join(f"{n}.{producto}" for pasillo in self._pasillos for producto in pasillo.productos)

    @staticmethod
    def buscar_productos(cliente, categoria):
        productos=[]
        ids = []
        for pasillo in cliente.get_tienda().get_pasillos():
            for producto in pasillo.productos:
                if producto.get_categoria() == categoria and producto.get_id() not in ids:
                    productos.append(producto)
                    ids.append(producto.get_id())
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
        return any(len(pasillo.productos) > 0 for pasillo in self._pasillos)

    def agregar_producto(self, producto):
        for pasillo in self._pasillos:
            if pasillo.categoria == producto.categoria:
                pasillo.agregar_producto(producto)
                return

    def agregar_producto_a_pasillo(self, producto, nombre_pasillo):
        for pasillo in self._pasillos:
            if pasillo.nombre == nombre_pasillo:
                pasillo.productos.append(producto)
                producto.tienda = self

    def obtener_todos_los_productos(self):
        return [producto for pasillo in self._pasillos for producto in pasillo.productos]

    @staticmethod
    def imprimir_producto(mayorn, mayorm, mayorp, mayorc, cantidad, producto):
        texto = f"  {producto.get_nombre()}".ljust(mayorn + 4)
        texto += f"|  {producto.get_marca()}/{producto.get_tamano().get_tamano()}".ljust(mayorm + 2)
        texto += f"|  {producto.get_precio()}".ljust(mayorp + 2)
        texto += f"|  {cantidad}".ljust(mayorc + 2)
        return texto

    def cantidad_producto(self, producto):
        return sum(1 for pasillo in self._pasillos for prod in pasillo.get_productos() if prod.get_id() == producto.get_id())

    def anadir_pasillo(self, x2, nom):
        from gestorAplicacion.servicios.enums import Categoria  # Importar la enumeración Categoria si es necesario
        from gestorAplicacion.servicios.pasillo import Pasillo
        Pasillo(nom,None, list(Categoria)[x2 - 1], self)

    def mostrar_pasillos(self):
        if len(self._pasillos) == 0:
            return "La tienda " + self.get_nombre() + " no tiene pasillos"
        else:
            s = "  Pasillo     Categoria \n"
            for i in self._pasillos:
                s += "    "
                s += i.get_nombre()
                s += "        "
                s += str(i.get_categoria()) + "\n"
            return s
    @classmethod
    def mostrar_desempleados(cls):
        n=1
        s=list()
        for desempleado in cls.desempleados:
            s.append("\n"+n+"."+desempleado.nombre)
            s.append("     ")
            s.append(desempleado.tipo)
            n+=1
        return str(s)

    def __str__(self):
        return self._nombre + self._saldo.__str__()