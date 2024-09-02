import sys

class Funcionalidad2:
    def __init__(self):
        self.productos = []
        self.cliente = Cliente(Tienda(), Carrito())

    @staticmethod
    def imprimirProducto(mayorN, mayorM, mayorP, mayorC, cantidad, producto):
        nombre = producto.getNombre().ljust(mayorN)
        marca_tamaño = f"{producto.getMarca()} {producto.getTamaño()}".ljust(mayorM)
        precio = f"{producto.getPrecio():.2f}".rjust(mayorP)
        return f"{nombre} | {marca_tamaño} | {precio} | {cantidad}"

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

    def cuadriculaProductos(self, productos, inferior, superior):
        self.lineas()
        mayorN = mayorM = mayorP = 0

        for p in productos[inferior:superior]:
            if p.getNombre():
                mayorN = max(mayorN, len(p.getNombre()))
            if p.getMarca():
                tamaño_len = len(p.getTamaño()) if p.getTamaño() else 0
                mayorM = max(mayorM, len(p.getMarca()) + tamaño_len + 1)
            mayorP = max(mayorP, len(f"{p.getPrecio()}"))

        mayorN = max(mayorN, 6)
        mayorM = max(mayorM, 12)
        mayorP = max(mayorP, 6)

        mayorC = 8
        print("")
        print("-" * (mayorM + mayorN + mayorP + 30))
        print(f"    Nombre{' ' * (mayorN - 4)}|  Marca/Tamaño{' ' * (mayorM - 10)}|  Precio{' ' * (mayorP - 4)}|  Cantidad  ")
        print("|" + "-" * (mayorM + mayorN + mayorP + 30) + "|")

        contador = 1
        for p in productos[inferior:superior]:
            cantidad = self.cliente.getTienda().cantidadProducto(p)
            print(f"{contador}. {self.imprimirProducto(mayorN, mayorM, mayorP, mayorC, cantidad, p)}")
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
        self.lineas()
        print("Estas son las categorias de los productos de nuestras tiendas: ")
        print("")
        enumerado = 1
        for tipo in Categoria:
            print(f" {enumerado}. {tipo.texto}")
            enumerado += 1
        print(f" {enumerado}. Volver")
        print("")
        decisionCategoria = self.escaner(enumerado)
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

    def elegirTipoBusqueda(self):
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
