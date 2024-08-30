from gestorAplicacion.sujetos.persona import Persona
from gestorAplicacion.servicios.enums import Genero
from gestorAplicacion.sujetos.cliente import Cliente
from gestorAplicacion.sujetos.administrador import Administrador

class Identidad:
    @staticmethod
    def identificar_persona():
        print("Digite su documento: ")
        p = int(input())
        for persona in Persona.get_personas():
            if p == persona.get_id():
                print(f"Bienvenido {persona.get_nombre()}")
                return persona
        
        print("No se ha encontrado el usuario", p)
        print("¿Qué desea hacer?")
        print("1. Digitar otra vez mi documento")
        print("2. Registrar usuario")
        print("Seleccione una opción: ")
        seleccion = int(input())
        
        if seleccion == 1:
            return Identidad.identificar_persona()
        
        print("Digite su nombre: ")
        nombre = input()
        
        print("Escoja su género")
        print("1. Masculino")
        print("2. Femenino")
        print("¿Cuál de los dos?: ")
        genero = int(input())
        genero1 = Genero.M if genero == 1 else Genero.F
        
        print("Digite su edad: ")
        edad = int(input())
        
        print("Desea comprar productos o administrar tiendas:")
        print("1. Comprar productos")
        print("2. Administrar tiendas")
        print("Seleccione una: ")
        decision = int(input())
        
        if decision == 1:
            persona = Cliente(nombre, p, edad, genero1)
        else:
            print("¿Cuánto dinero desea para hacer su administración?: ")
            dinero = float(input())
            persona = Administrador(nombre, p, edad, genero1, dinero)
        
        print("Usuario creado con éxito")
        print(f"Bienvenido {nombre}")
        return persona