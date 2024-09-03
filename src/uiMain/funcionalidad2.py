import sys




class Funcionalidad2:
    def __init__(self):
        from gestorAplicacion.servicios.carrito import Carrito
        from gestorAplicacion.servicios.tienda import Tienda
        from gestorAplicacion.sujetos.cliente import Cliente
        self.productos = []
        self.cliente = Cliente(Tienda(), Carrito())

    @classmethod
    def imprimir_producto(cls,mayorn, mayorm, mayorp, mayorc, cantidad, producto):
        nombre = producto.getNombre().ljust(mayorn)
        marca_tamano = f"{producto.getMarca()} {producto.getTamano()}".ljust(mayorm)
        precio = f"{producto.getPrecio():.2f}".rjust(mayorp)
        return f"{nombre} | {marca_tamano} | {precio} | {cantidad}"

    def buscarProductos(self, categoria):
        # Implementar la búsqueda de productos por categoría
        pass

    def recomendarProductos(self, seleccionado):
        # Implementar la recomendación de productos
        pass

    def lineas(self):
        print("-" * 80)

    def print(self, message=""):
        sys.stdout.write(message + "\n")

    def escaner(self, opciones=None):
        try:
            if opciones:
                seleccion = int(input())
                if 1 <= seleccion <= opciones:
                    return seleccion
                else:
                    print("Opción no válida.")
                    return self.escaner(opciones)
            else:
                return int(input())
        except ValueError:
            print("Entrada no válida.")
            return self.escaner(opciones)

    @classmethod
    def cuadriculaProductos(cls,cliente, productos, inferior, superior):
        from uiMain.main import Main
        Main.lineas()
        mayorN = mayorM = mayorP = 0

        for p in productos[inferior:superior]:
            if p.getNombre():
                mayorN = max(mayorN, len(p.getNombre()))
            if p.getMarca():
                tamano_len = len(p.getTamaño()) if p.getTamaño() else 0
                mayorm = max(mayorM, len(p.getMarca()) + tamano_len + 1)
            mayorp = max(mayorP, len(f"{p.getPrecio()}"))

        mayorn = max(mayorN, 6)
        mayorm = max(mayorM, 12)
        mayorp = max(mayorP, 6)

        mayorc = 8
        print("")
        print("-" * (mayorm + mayorn + mayorp + 30))
        print(f"    Nombre{' ' * (mayorn - 4)}|  Marca/Tamaño{' ' * (mayorm - 10)}|  Precio{' ' * (mayorp - 4)}|  Cantidad  ")
        print("|" + "-" * (mayorm + mayorn + mayorp + 30) + "|")

        contador = 1
        for p in productos[inferior:superior]:
            cantidad = cliente.getTienda().cantidadProducto(p)
            print(f"{contador}. {Funcionalidad2.imprimir_producto(mayorn, mayorm, mayorp, mayorc, cantidad, p)}")
            contador += 1

        print("-" * (mayorM + mayorN + mayorP + 30))
        print("")
        print(" 1/2/3/4/Texto. ¿Desea alguno de estos productos?, si es asi escojalo")
        print(" 5. Si desea volver escriba 5")
        if superior > 4:
            print(" [A] pag. Si desea imprimir los 4 productos anteriores, escriba A")
        if len(productos) - superior > 0:
            print(" [S] pag. Si desea imprimir los 4 proximos productos, escriba S")
        print("")

    def impresionSeleccionCategoria(self, productos, categoria, malSeleccionado):
        inferior = 0
        superior = 4
        seleccionado = None

        while True:
            if (len(productos) - superior) < 0:
                superior = len(productos)

            if not malSeleccionado:
                self.cuadriculaProductos(productos, inferior, superior)

            seleccion = input("Seleccione una opción: ").strip()
            seleccionado = None
            malSeleccionado = False
            texto = False

            try:
                numero = int(seleccion)
            except ValueError:
                texto = True

            if texto:
                for k in productos:
                    if k.getNombre().lower() == seleccion.lower():
                        seleccionado = k
                        break

                if seleccion.lower() == "s":
                    inferior = superior
                    superior += 4
                    continue
                if seleccion.lower() == "a":
                    superior = inferior
                    inferior -= 4
                    continue

                if seleccionado is None:
                    print("")
                    print("Este producto no se encuentra:")
                    print(" 1. Desea copiar otra opcion")
                    print(" 2. Desea mirar si puede pedir reabastecer el producto")
                    print("Escoja una opción: ")
                    malSeleccionado = True
                    continue
            else:
                if 1 <= numero <= 4:
                    if numero + inferior - 1 < len(productos):
                        seleccionado = productos[numero + inferior - 1]
                    else:
                        print("Ese número está fuera del rango")
                        malSeleccionado = True
                        continue
                elif numero == 5:
                    self.busquedaCategoria(categoria, productos, seleccionado)
                    return None
                else:
                    print("Ese número está fuera del rango")
                    malSeleccionado = True
                    continue

            if seleccionado is not None:
                return seleccionado

    def impresionSeleccionNombre(self, productos, seleccionado):
        inferior = 0
        superior = 4
        malSeleccionado = False

        while True:
            if (len(productos) - superior) < 0:
                superior = len(productos)

            if not malSeleccionado:
                self.cuadriculaProductos(productos, inferior, superior)

            malSeleccionado = False
            seleccion = input()
            texto = False

            try:
                numero = int(seleccion)
            except ValueError:
                texto = True

            if texto:
                for k in productos:
                    if k.getNombre().lower() == seleccion.lower():
                        seleccionado = k
                        break

                if seleccion.lower() == "s":
                    inferior = superior
                    superior += 4
                    continue
                if seleccion.lower() == "a":
                    superior = inferior
                    inferior -= 4
                    continue

                if seleccionado is None:
                    print("")
                    print("Este producto no se encuentra, escriba otro o selecione otra opcion: ")
                    malSeleccionado = True
                    continue
            else:
                if 1 <= numero <= 4:
                    seleccionado = productos[numero + inferior - 1]
                elif numero == 5:
                    self.busquedaNombre(productos, seleccionado)
                    return None

            return seleccionado

    def busquedaCategoria(self, categoria, productos, seleccionado):
        from gestorAplicacion.servicios.enums import Categoria
        Main.lineas()
        print("Estas son las categorias de los productos de nuestras tiendas: ")
        print("")
        enumerado = 1
        for tipo in Categoria:
            print(f" {enumerado}. {tipo.texto}")
            enumerado += 1
        print(f" {enumerado}. Volver")
        print("")
        decisionCategoria = Main.escaner(enumerado)
        if decisionCategoria == enumerado:
            self.elegirTipoBusqueda()
            return

        categoria = Categoria(decisionCategoria)
        productos = self.buscarProductos(categoria)

        while len(productos) == 0:
            print("No hay productos disponibles de esa categoria, escoja otro por favor")
            decisionCategoria = self.escaner(enumerado)
            if decisionCategoria == enumerado:
                self.elegirTipoBusqueda()
                return
            categoria = Categoria(decisionCategoria)
            productos = self.buscarProductos(categoria)

        seleccionado = self.impresionSeleccionCategoria(productos, categoria, False)
        self.lineas()
        self.dondeSeAgreganProductos(seleccionado)

    def busquedaNombre(self, productos, seleccionado):
        self.lineas()
        print("Introduzca el nombre del producto que desea buscar\nO escoja [3]. [Volver] para regresar: ")
        nombre = input()
        string = True

        try:
            number = int(nombre)
        except ValueError:
            string = False

        if string and number == 3:
            self.elegirTipoBusqueda()
            return

        if nombre.lower() == "volver":
            self.elegirTipoBusqueda()
            return

        productos = self.buscarProductos(nombre)
        seleccionado = self.impresionSeleccionNombre(productos, seleccionado)

        if seleccionado is not None:
            self.dondeSeAgreganProductos(seleccionado)
        else:
            self.elegirTipoBusqueda()

    def dondeSeAgreganProductos(self, seleccionado):
        self.lineas()
        print(f"Usted ha seleccionado el producto {seleccionado.getNombre()}")
        print("¿Cómo desea continuar?:")
        print(" 1. Añadir al carrito")
        print(" 2. Recomendar productos similares")
        print(" 3. Volver")
        decision = self.escaner(3)

        if decision == 1:
            cantidad = self.escaner()
            self.cliente.getCarrito().agregarAlCarrito(seleccionado, cantidad)
        elif decision == 2:
            self.recomendarProductos(seleccionado)
        else:
            self.elegirTipoBusqueda()

    def elegirTipoBusqueda(self,cliente):
        self.lineas()
        print("Seleccione el tipo de búsqueda:")
        print(" 1. Buscar por categoría")
        print(" 2. Buscar por nombre")
        print(" 3. Volver")
        decision = self.escaner(3)

        if decision == 1:
            self.busquedaCategoria(None, [], None)
        elif decision == 2:
            self.busquedaNombre([], None)
        else:
            # Regresar al menú principal o salir
            pass

if __name__ == "__main__":
    funcionalidad = Funcionalidad2()
    funcionalidad.elegirTipoBusqueda()
