from datetime import date


class Carrito:
    # Atributos
    def __init__(self, cliente=None, pagado=False, tienda=None, tipo_carrito=None):
        self.productos = []
        self.cliente = cliente
        self.caja = None
        self.tienda = tienda
        self.tipo_carrito = tipo_carrito
        self.proveedor = None
        self.pagado = pagado
        self.precio_total = 0.0
        self.fecha_facturacion = date.today()

        if tienda:
            tienda.get_facturas().append(self)

    # Getters y Setters
    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = productos

    @property
    def caja(self):
        return self._caja

    @caja.setter
    def caja(self, caja):
        self._caja = caja

    @property
    def precio_total(self):
        return self._precio_total

    @precio_total.setter
    def precio_total(self, precio_total):
        self._precio_total = precio_total

    @property
    def proveedor(self):
        return self._proveedor

    @proveedor.setter
    def proveedor(self, proveedor):
        self._proveedor = proveedor

    @property
    def pagado(self):
        return self._pagado

    @pagado.setter
    def pagado(self, pagado):
        self._pagado = pagado

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def tienda(self):
        return self._tienda

    @tienda.setter
    def tienda(self, tienda):
        self._tienda = tienda

    @property
    def tipo_carrito(self):
        return self._tipo_carrito

    @tipo_carrito.setter
    def tipo_carrito(self, tipo_carrito):
        self._tipo_carrito = tipo_carrito

    @property
    def fecha_facturacion(self):
        return self._fecha_facturacion

    @fecha_facturacion.setter
    def fecha_facturacion(self, fecha_facturacion):
        self._fecha_facturacion = fecha_facturacion

    # Métodos
    def agregar_al_carrito(self, seleccionado, cantidad):
        monto_actual = sum(p.get_precio() for p in self.productos)
        tamano_maximo = 15 if self.tipo_carrito == 'ADULTOS' else 5

        if not self.cliente.mayor_edad() and seleccionado.get_edades() == 'ADULTOS':
            return "Producto no agregado, no tienes la edad válida para este producto"
        if len(self.productos) >= tamano_maximo:
            return "Producto no agregado, ya no tienes espacio en el carrito"
        if self.cliente.get_dinero() - monto_actual - (seleccionado.get_precio() * cantidad) < 0:
            return "Producto no agregado, ya no tienes dinero para agregar este producto"

        if self.cliente.get_tienda().cantidad_producto(seleccionado) < cantidad:
            return f"Productos no agregados, no hay cantidad de productos suficientes, te podemos ofrecer {seleccionado.cantidad_producto()} productos de ese tipo solamente"

        for _ in range(cantidad):
            tienda = self.tienda
            pasillo = seleccionado.get_pasillo()

            for p in tienda.get_pasillos():
                if p == pasillo:
                    pasillo = p
                    break

            if pasillo.get_productos().remove(seleccionado):
                self.productos.append(seleccionado.clone())
            else:
                break
        return f"Producto/Productos {seleccionado.get_nombre()} agregado con éxito a su carrito"

    def contar_repeticiones(self, producto_buscado):
        return sum(1 for producto in self.productos if producto == producto_buscado)

    def eliminar_productos(self, seleccionado, cantidad):
        tienda = self.tienda
        pasillo = seleccionado.get_pasillo()

        for p in tienda.get_pasillos():
            if p == pasillo:
                pasillo = p
                break

        for _ in range(cantidad):
            if self.productos.remove(seleccionado):
                pasillo.get_productos().append(seleccionado.clone())
            else:
                print("No hay suficientes productos en el carrito para eliminar.")
                break

    @staticmethod
    def calcular_total(carrito):
        return sum(producto.get_precio() for producto in carrito)

    def generar_detalles_factura(self, descuento_membresia, gano_juego):
        detalles = ["Factura:", "+-----+--------------------+---------------+----------+------------+----------+",
                    "| No. | Producto           | Marca         | Tamaño   | Categoría  | Precio   |",
                    "+-----+--------------------+---------------+----------+------------+----------+"]
        for i, producto in enumerate(self.productos, 1):
            detalles.append(f"| {i:<3} | {producto.get_nombre():<18} | {producto.get_marca():<13} | {producto.get_tamaño().get_tamaño():<8} | {producto.get_categoria().get_texto():<10} | {producto.get_precio():<8.2f} |")
        detalles.append("+-----+--------------------+---------------+----------+------------+----------+")

        detalles.append(f"Descuento por membresía: {descuento_membresia * 100:.2f}%")
        if gano_juego:
            detalles.append("Descuento adicional por ganar el juego: 10%")

        precio_final = self.calcular_total(self.productos) * (1 - descuento_membresia) * (0.9 if gano_juego else 1.0)
        detalles.append(f"Precio final: {precio_final:.2f}")

        return "\n".join(detalles)

    def eliminar_carrito(self):
        for producto in self.productos:
            producto.get_pasillo().get_productos().append(producto)
        self.productos.clear()
        self.precio_total = 0.0
        self.pagado = False

    def incrementar_costo(self, numero):
        self.precio_total += numero