class ErrorAplicacion(Exception):
    pass

class CategoriaPropia1(ErrorAplicacion):
    pass

class CategoriaPropia2(ErrorAplicacion):
    pass

class ExceptionInventada1(CategoriaPropia1):
    pass

class ExceptionInventada2(CategoriaPropia1):
    pass

class ExceptionInventada3(CategoriaPropia2):
    pass

class ExceptionInventada4(CategoriaPropia2):
    pass