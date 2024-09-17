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

class TiendaNoAsignadaError(Exception):
    def __init__(self, message="Debe pasar por la funcionalidad 1 para asignar una tienda."):
        self.message = message
        super().__init__(self.message)

# Función que verifica si el cliente tiene una tienda asignada
def verificar_tienda_asignada(cliente):
    if cliente.get_tienda() is None:  
        raise TiendaNoAsignadaError()

class ExceptionInventada2(CategoriaPropia1):
    pass

class ExceptionInventada3(CategoriaPropia2):
    pass

class ExceptionInventada4(CategoriaPropia2):
    pass