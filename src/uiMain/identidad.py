class Identidad:
    def __init__(self):
        pass

    @classmethod
    def identificar_persona(cls):
        from gestorAplicacion.sujetos.administrador import Administrador
        from gestorAplicacion.sujetos.cliente import Cliente
        from gestorAplicacion.servicios.enums import Genero
        from gestorAplicacion.sujetos.persona import Persona
        from .main import Main
        print("Digite su documento: ")
        p = Main.escaner()
        for persona in Persona.get_personas():
            if p == persona.get_id():
                print(f"Bienvenido {persona.get_nombre()}")
                return persona
        
        print("No se ha encontrado el usuario", p)
        print("¿Qué desea hacer?")
        print("1. Digitar otra vez mi documento")
        print("2. Registrar usuario")
        print("Seleccione una opción: ") 
        seleccion = Main.escaner_con_rango(2)
        
        if seleccion == 1:
            return Identidad.identificar_persona()
        
        print("Digite su nombre: ")
        while True:
            nombre = input("Ingresa tu nombre: ")

            if not nombre.isalpha() and not all(char.isalpha() or char.isspace() for char in nombre):
                print("El nombre no puede contener números ni caracteres especiales. Intenta de nuevo.")
            else:
                break

        print("Escoja su género")
        print("1. Masculino")
        print("2. Femenino")
        print("¿Cuál de los dos?: ")
        genero = Main.escaner_con_rango(2)
        genero1 = Genero.H if genero == 1 else Genero.M
        
        print("Digite su edad: ")
        edad = Main.escaner()
        
        print("Desea comprar productos o administrar tiendas:")
        print("1. Comprar productos")
        print("2. Administrar tiendas")
        print("Seleccione una: ")
        decision = Main.escaner_con_rango(2)
        
        if decision == 1:
            persona = Cliente(nombre, p, edad, genero1)
        else:
            print("¿Cuánto dinero desea para hacer su administración?: ")
            dinero = float(input())
            persona = Administrador(nombre, p, edad, genero1, dinero)
        
        print("Usuario creado con éxito")
        print(f"Bienvenido {nombre}")
        return persona