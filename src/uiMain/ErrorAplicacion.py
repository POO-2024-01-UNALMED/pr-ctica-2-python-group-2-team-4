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
class TiendaNoAsignadaError(Exception):
    def __init__(self, cliente, message="Debe pasar por la funcionalidad 1 para asignar una tienda."):
        self.cliente = cliente
        self.message = f"Cliente {cliente.get_nombre()}: {message}"  # Incluir el nombre del cliente en el mensaje
        super().__init__(self.message)

# Función que verifica si el cliente tiene una tienda asignada
def verificar_tienda_asignada(cliente):
    if cliente.get_tienda() is None:  # Asume que 'None' significa que no hay tienda asignada
        raise TiendaNoAsignadaError(cliente)


class ExceptionInventada2(CategoriaPropia1):
    pass

class ExceptionInventada3(CategoriaPropia2):
    pass

class ExceptionInventada4(CategoriaPropia2):
    pass