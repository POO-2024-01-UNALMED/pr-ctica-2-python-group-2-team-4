class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje

class CategoriaPropia1(ErrorAplicacion):
    def __init__(self,mensaje):
        super().__init__(mensaje)

class CategoriaPropia2(ErrorAplicacion):
    def __init__(self,mensaje):
        super().__init__(mensaje)

# Definir la excepción personalizada que recibe un cliente
class TiendaNoAsignadaError(CategoriaPropia1):
    def __init__(self, cliente, message="Debe pasar por la funcionalidad 1 para asignar una tienda."):
        self.cliente = cliente
        self.message = f"Cliente {cliente.get_nombre()}: {message}"  # Incluir el nombre del cliente en el mensaje
        super().__init__(self.message)

# Función que verifica si el cliente tiene una tienda asignada
def verificar_tienda_carrito_asignada(cliente):
    if cliente.get_tienda() is None or cliente.get_carrito() is None:  # Asume que 'None' significa que no hay tienda asignada
        raise TiendaNoAsignadaError(cliente)


class SaldoInsuficienteError(CategoriaPropia2):
    def __init__(self, cliente, message="No tienes suficiente dinero para realizar la compra."):
        self.cliente = cliente
        self.message = f"Cliente {cliente.get_nombre()}: {message}"
        super().__init__(self.message)

# Función para verificar si el cliente tiene suficiente dinero
def verificar_saldo(cliente, monto_compra):
    if cliente.get_dinero() == 0:
        raise SaldoInsuficienteError(cliente, "Tu saldo es 0. No puedes realizar compras.")
    elif cliente.get_dinero() < monto_compra:
        raise SaldoInsuficienteError(cliente, "No tienes suficiente dinero para esta compra.")


# Excepción personalizada para cuando el objeto no es de tipo Cliente
class ObjetoNoEsClienteError(CategoriaPropia2):
    def __init__(self, message="El objeto proporcionado no es un cliente."):
        self.message = message
        super().__init__(self.message)


# Función que solo acepta objetos de tipo Cliente
def procesar_cliente(cliente):
    from gestorAplicacion.sujetos.cliente import Cliente
    # Verificar si el objeto es de tipo Cliente
    if not isinstance(cliente, Cliente):
        raise ObjetoNoEsClienteError("Se esperaba un objeto de tipo Cliente, pero se recibió otro tipo.")

    # Si es un cliente, se continúa con la operación
    print(f"Procesando cliente: {cliente.get_nombre()}")




# Excepción personalizada para cuando el objeto no es de tipo Administrador
class ObjetoNoEsAdministradorError(CategoriaPropia1):
    def __init__(self, message="El objeto proporcionado no es un administrador."):
        self.message = message
        super().__init__(self.message)


# Función que solo acepta objetos de tipo Administrador
def procesar_administrador(administrador):
    from gestorAplicacion.sujetos.administrador import Administrador
    # Verificar si el objeto es de tipo Administrador
    if not isinstance(administrador, Administrador):
        raise ObjetoNoEsAdministradorError("Se esperaba un objeto de tipo Administrador, pero se recibió otro tipo.")

    # Si es un administrador, se continúa con la operación
    print(f"Procesando administrador: {administrador.get_nombre()}")