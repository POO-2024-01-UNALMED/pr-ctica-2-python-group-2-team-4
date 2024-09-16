import tkinter as tk
from tkinter import Tk, messagebox

#from interfaz import FieldFrame_p
# from gestorAplicacion.servicios.enums import Genero
# from gestorAplicacion.sujetos.administrador import Administrador
# from gestorAplicacion.sujetos.cliente import Cliente
# from gestorAplicacion.sujetos.persona import Persona

from tkinter import Frame, Label, Entry, Button, Tk

from uiMain.fieldFrame import FieldFrame


#from gestorAplicacion.sujetos.administrador import Administrador
#from gestorAplicacion.sujetos.cliente import Cliente
#from uiMain.fieldFrame import FieldFrame  

class Identidad:
    def __init__(self):
        pass

    @classmethod
    def identificar_persona(cls):
        from gestorAplicacion.sujetos.administrador import Administrador
        from gestorAplicacion.sujetos.cliente import Cliente
        from gestorAplicacion.servicios.enums import Genero
        from gestorAplicacion.sujetos.persona import Persona
        from uiMain.main import Main
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
        
    ## intento version fieldframe #
#--------------------------------------------------------------------
# class Identidad2:
#     def __init__(self, window):
#         self.window = window
#         self.frame_actual = None

#     def mostrar_frame(self, titulo, descripcion, criterios, valores, habilitado, callback):
#         # Destruir el frame actual si existe
#         if self.frame_actual is not None:
#             self.frame_actual.destroy()
        
#         # Crear un nuevo FieldFrame
#         from fieldFrame import FieldFrame
#         self.frame_actual = FieldFrame(
#             master=self.window,
#             tituloCriterios=titulo,
#             criterios=criterios,
#             tituloValores="Valores",
#             valores=valores,
#             habilitado=habilitado,
#             titulo="Identificación",
#             descripcion=descripcion
#         )
#         self.frame_actual.pack(pady=20, padx=20, fill='both', expand=True)
#         self.frame_actual.aceptar.config(command=callback)
#         #self.frame_actual.borrar.config(command=self.frame_actual.borrar)

#     def identificar_persona(self):
        
#         def identificar():
#             p = self.frame_actual._entrys[0].get()  # Suponiendo que el ID está en el primer Entry
#             from gestorAplicacion.sujetos.persona import Persona
#             for persona in Persona.get_personas():
#                 if p == persona.get_id():
#                     self.mostrar_mensaje(f"Bienvenido {persona.get_nombre()}")
#                     return persona
            
#             self.mostrar_registro()

#         criterios = ["ID"]
#         valores = [""]
#         habilitado = [True]
#         self.mostrar_frame(
#             titulo="Ingrese su documento",
#             descripcion="Ingrese el ID para buscar su registro.",
#             criterios=criterios,
#             valores=valores,
#             habilitado=habilitado,
#             callback=identificar
#         )
#     def mostrar_registro(self):
#         def registrar():
#             nombre = self.frame_actual._entrys[0].get()
#             id=self.frame_actual._entrys[1].get()
#             edad = self.frame_actual._entrys[2].get()
#             genero = self.frame_actual._entrys[3].get()
#             decision = self.frame_actual._entrys[4].get()
            
#             if decision == "1":
#                 from gestorAplicacion.sujetos.cliente import Cliente
#                 persona = Cliente(nombre, id, edad, genero)
#             else:
#                 from gestorAplicacion.sujetos.administrador import Administrador
#                 dinero = float(self.frame_actual._entrys[4].get())
#                 persona = Administrador(nombre, id, edad, genero, dinero)
            
#             self.mostrar_mensaje(f"Usuario creado con éxito. Bienvenido {nombre}")
#             return persona

#         criterios = [
#             "Nombre",
#             "Id",
#             "Edad",
#             "Género (1: Masculino, 2: Femenino)",
#             "Tipo de Usuario (1: Comprar productos, 2: Administrar tiendas)",
#             "Dinero (si aplica)"
#         ]
#         valores = ["","", "", "", "", ""]
#         habilitado = [True,True, True, True, True, False]  # Solo habilitado el último campo si es necesario

#         self.mostrar_frame(
#             titulo="Registro de Usuario",
#             descripcion="El id no se encuentra en la base de datos. Complete los datos para registrar un nuevo usuario.",
#             criterios=criterios,
#             valores=valores,
#             habilitado=habilitado,
#             callback=registrar
#         )

#     def mostrar_mensaje(self, mensaje):
#         # Se muestra un mensaje usando un label en el frame actual
#         if self.frame_actual:
#             self.frame_actual.destroy()
        
#         self.frame_actual = Frame(self.window, bg="light blue")
#         self.frame_actual.pack(pady=20, padx=20, fill='both', expand=True)
#         Label(self.frame_actual, text=mensaje, font=("Arial", 20), bg="light blue").pack(pady=20, padx=20)
#         Button(self.frame_actual, text="Aceptar", command=self.frame_actual.destroy).pack(pady=10)
class Identidad2:
    def __init__(self, window):
        self.window = window
        self.frame_actual = None
        self.resultado = None

    def mostrar_frame(self, titulo, descripcion, criterios, valores, habilitado, callback):
        # Destruir el frame actual si existe
        if self.frame_actual:
            self.frame_actual.destroy()
        
        # Crear un nuevo FieldFrame
        self.frame_actual = FieldFrame(
            master=self.window,
            tituloCriterios=titulo,
            criterios=criterios,
            tituloValores="Valores",
            valores=valores,
            habilitado=habilitado,
            titulo="Identificación",
            descripcion=descripcion
        )
        self.frame_actual.pack(pady=20, padx=20, fill='both', expand=True)
        self.frame_actual.aceptar.config(command=callback)

    def identificar_persona(self):
        def identificar():
            for entry in self.frame_actual._entrys:
                if entry.get()=="":
                    messagebox.showerror("Error","Faltan campos por completar")
                    return
            p = self.frame_actual._entrys[0].get()  # Suponiendo que el ID está en el primer Entry
            
            from gestorAplicacion.sujetos.persona import Persona
            personas = Persona.get_personas()
            persona_encontrada = next((p for p in personas if p.get_id() == p), None)

            if persona_encontrada:
                self.resultado = persona_encontrada
                self.mostrar_mensaje(f"Bienvenido {persona_encontrada.get_nombre()}")
            else:
                self.mostrar_alerta(p)

        criterios = ["ID"]
        valores = [""]
        habilitado = [True]
        self.mostrar_frame(
            titulo="Ingrese su documento",
            descripcion="Ingrese el ID para buscar su registro.",
            criterios=criterios,
            valores=valores,
            habilitado=habilitado,
            callback=identificar
        )
        return self.resultado  # Retorna la persona identificada si existe

    def mostrar_alerta(self, id):
        def registrarme():
            self.mostrar_registro(id)
            alerta.destroy()
        
        def cancelar():
            if self.frame_actual:
                self.frame_actual.destroy()
            alerta.destroy()
        
        alerta = tk.Toplevel(self.window)
        alerta.title("Alerta")
        alerta.geometry("300x150")
        alerta.grab_set()  # Hace que la ventana emergente sea modal

        mensaje = Label(alerta, text="No se ha encontrado una persona con el ID proporcionado", font=("Arial", 12))
        mensaje.pack(pady=20, padx=20)

        boton_registrarme = Button(alerta, text="Registrarme", command=registrarme)
        boton_registrarme.pack(side=tk.LEFT, padx=10, pady=10)

        boton_cancelar = Button(alerta, text="Cancelar", command=cancelar)
        boton_cancelar.pack(side=tk.RIGHT, padx=10, pady=10)

    def mostrar_registro(self, id):
        def registrar():
            nombre = self.frame_actual._entrys[0].get()
            id = self.frame_actual._entrys[1].get()
            edad = self.frame_actual._entrys[2].get()
            genero = self.frame_actual._entrys[3].get()
            decision = self.frame_actual._entrys[4].get()
            dinero = self.frame_actual._entrys[5].get()

            if decision == "1":
                # Importar Cliente solo cuando sea necesario
                from gestorAplicacion.sujetos.cliente import Cliente
                persona = Cliente(nombre, id, edad, genero)
                self.resultado = persona
                self.mostrar_mensaje(f"Usuario Cliente creado con éxito. Bienvenido {nombre}")
            else:
                # Importar Administrador solo cuando sea necesario
                from gestorAplicacion.sujetos.administrador import Administrador
                dinero = float(dinero) if dinero else 0.0
                persona = Administrador(nombre, id, edad, genero, dinero)
                self.resultado = persona
                self.mostrar_mensaje(f"Usuario Admin creado con éxito. Bienvenido {nombre}")
            # Mostrar mensaje de éxito y actualizar resultado
           
            
            # Print en consola para verificar
            print(f"Persona registrada exitosamente: ID = {id}, Nombre = {nombre}")

        criterios = [
            "Nombre",
            "Id",
            "Edad",
            "Género (1: Masculino, 2: Femenino)",
            "Tipo de Usuario (1: Comprar productos, 2: Administrar tiendas)",
            "Dinero (si aplica)"
        ]
        valores = ["", "", "", "", "", ""]
        habilitado = [True, True, True, True, True, False]  # Solo habilitado el último campo si es necesario

        self.mostrar_frame(
            titulo="Registro de Usuario",
            descripcion="Complete los datos para registrar un nuevo usuario.",
            criterios=criterios,
            valores=valores,
            habilitado=habilitado,
            callback=registrar
        )

    def mostrar_mensaje(self, mensaje):
        # Se muestra un mensaje usando un label en el frame actual
        if self.frame_actual:
            self.frame_actual.destroy()
        
        self.frame_actual = Frame(self.window, bg="light blue")
        self.frame_actual.pack(pady=20, padx=20, fill='both', expand=True)
        Label(self.frame_actual, text=mensaje, font=("Arial", 20), bg="light blue").pack(pady=20, padx=20)
        Button(self.frame_actual, text="Aceptar", command=self.frame_actual.destroy).pack(pady=10)



        