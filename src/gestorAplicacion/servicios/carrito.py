from datetime import date


class Carrito:
    # Atributos
    def __init__(self, cliente=None, pagado=False, tipo_carrito=None, tienda=None):
        self._productos = []
        self._caja = None
        self._tienda = tienda
        self._tipo_carrito = tipo_carrito
        self._proveedor = None
        self._pagado = pagado
        self._precio_total = 0.0
        self._fecha_facturacion = date.today()
        self._cliente = cliente
        if cliente is not None:
            cliente.get_facturas().append(self)
        if tienda:
            tienda.get_facturas().append(self)

    # Getters y Setters
    def get_productos(self):
        return self._productos

    def set_productos(self, productos):
        self._productos = productos

    def get_caja(self):
        return self._caja

    def set_caja(self, caja):
        self._caja = caja

    def get_precio_total(self):
        return self._precio_total

    def set_precio_total(self, precio_total):
        self._precio_total = precio_total

    def get_proveedor(self):
        return self._proveedor

    def set_proveedor(self, proveedor):
        self._proveedor = proveedor

    def get_pagado(self):
        return self._pagado

    def set_pagado(self, pagado):
        self._pagado = pagado

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_tienda(self):
        return self._tienda

    def set_tienda(self, tienda):
        self._tienda = tienda

    def get_tipo_carrito(self):
        return self._tipo_carrito

    def set_tipo_carrito(self, tipo_carrito):
        self._tipo_carrito = tipo_carrito

    def get_fecha_facturacion(self):
        return self._fecha_facturacion

    def set_fecha_facturacion(self, fecha_facturacion):
        self._fecha_facturacion = fecha_facturacion

    # Métodos
    def agregar_al_carrito(self, seleccionado, cantidad):
        from gestorAplicacion.servicios.enums import Edades
        tamano_maximo = 15 if self._tipo_carrito == Edades.ADULTOS else 5
        monto_actual = sum(p.get_precio() for p in self._productos)

        if not self._cliente.mayor_edad() and seleccionado.get_edades() == Edades.ADULTOS:
            return "Producto no agregado, no tienes la edad valida para este producto"

        if len(self._productos) >= tamano_maximo:
            return "Producto no agregado, ya no tienes espacio en el carrito"

        if self._cliente.get_dinero() - monto_actual - (seleccionado.get_precio() * cantidad) < 0:
            return "Producto/Productos no agregados, ya no tienes dinero para agregar este producto" if cantidad == 1 else "Productos no agregados, ya no tienes dinero para agregar estos productos"

        if self._cliente.get_tienda().cantidad_producto(seleccionado) < cantidad:
            return f"Productos no agregados, no hay cantidad de productos suficientes, le podemos ofrecer\n{seleccionado.cantidad_producto()} productos de ese tipo solamente"

        tienda = self._tienda
        pasillo = seleccionado.get_pasillo()  # Obtener el pasillo del producto seleccionado

        # Buscar el pasillo en la tienda que coincida con el pasillo del producto seleccionado
        pasillo_encontrado = None
        for p in tienda.get_pasillos():
            if p == pasillo:
                pasillo_encontrado = p
                break

        # Ahora que tienes el pasillo correcto, intenta eliminar el producto
        if pasillo_encontrado:
            for _ in range(cantidad):
                if seleccionado in pasillo_encontrado.get_productos():
                    pasillo_encontrado.get_productos().remove(seleccionado)
                    self._productos.append(seleccionado.clone())  # Agregar el producto eliminado a la lista de productos
                else:
                    break

        return f"Producto/Productos {seleccionado.get_nombre()} agregado con exito a su carrito"

    def contar_repeticiones(self, producto_buscado):
        return sum(1 for producto in self._productos if producto == producto_buscado)

    def eliminar_productos(self, seleccionado, cantidad):
        tienda = self._tienda
        pasillo = seleccionado.get_pasillo()

        for p in tienda.get_pasillos():
            if p == pasillo:
                pasillo = p
                break

        for _ in range(cantidad):
            if self._productos.remove(seleccionado):
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
        for i, producto in enumerate(self._productos, 1):
            detalles.append(f"| {i:<3} | {producto.get_nombre():<18} | {producto.get_marca():<13} | {producto.get_tamaño().get_tamaño():<8} | {producto.get_categoria().get_texto():<10} | {producto.get_precio():<8.2f} |")
        detalles.append("+-----+--------------------+---------------+----------+------------+----------+")

        detalles.append(f"Descuento por membresía: {descuento_membresia * 100:.2f}%")
        if gano_juego:
            detalles.append("Descuento adicional por ganar el juego: 10%")

        precio_final = self.calcular_total(self._productos) * (1 - descuento_membresia) * (0.9 if gano_juego else 1.0)
        detalles.append(f"Precio final: {precio_final:.2f}")

        return "\n".join(detalles)

    def eliminar_carrito(self):
        for producto in self._productos:
            producto.get_pasillo().get_productos().append(producto)
        self._productos.clear()
        self._precio_total = 0.0
        self._pagado = False

    def incrementar_costo(self, numero):
        self._precio_total += numero