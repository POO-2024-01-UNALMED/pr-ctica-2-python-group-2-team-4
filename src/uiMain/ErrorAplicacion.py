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

class ExceptionInventada1(CategoriaPropia1):
    pass

class ExceptionInventada2(CategoriaPropia1):
    pass

class ExceptionInventada3(CategoriaPropia2):
    pass

class ExceptionInventada4(CategoriaPropia2):
    pass