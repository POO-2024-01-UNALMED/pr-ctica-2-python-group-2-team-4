import tkinter as tk
from tkinter import messagebox

from gestorAplicacion.servicios.enums import Genero
from gestorAplicacion.sujetos.administrador import Administrador
from gestorAplicacion.sujetos.cliente import Cliente
from gestorAplicacion.sujetos.persona import Persona


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
    
    # identificar usuario version tkinter 
    def identificar_persona(root, frame_func4):
    # Limpiar frame_func4
        for widget in frame_func4.winfo_children():
            widget.destroy()

    # Función para procesar el documento ingresado
    def procesar_documento():
        p = entry_doc.get()
        if not p.isdigit():
            messagebox.showerror("Error", "El documento debe ser un número.")
            return

        p = int(p)
        for persona in Persona.get_personas():
            if p == persona.get_id():
                messagebox.showinfo("Bienvenido", f"Bienvenido {persona.get_nombre()}")
                return

        # Si no encuentra al usuario
        mostrar_opciones_no_usuario(p)

    # Mostrar opciones si no se encuentra el usuario
    def mostrar_opciones_no_usuario(p):
        for widget in frame_func4.winfo_children():
            widget.destroy()

        label_no_user = tk.Label(frame_func4, text=f"No se ha encontrado el usuario con documento {p}")
        label_no_user.pack(pady=5)

        label_opciones = tk.Label(frame_func4, text="¿Qué desea hacer?")
        label_opciones.pack(pady=5)

        boton_digitar_otro = tk.Button(frame_func4, text="Digitar otra vez mi documento", command=lambda: identificar_persona(root, frame_func4))
        boton_digitar_otro.pack(pady=5)

        boton_registrar = tk.Button(frame_func4, text="Registrar usuario", command=lambda: registrar_usuario(p))
        boton_registrar.pack(pady=5)

    # Función para registrar un nuevo usuario
    def registrar_usuario(p):
        for widget in frame_func4.winfo_children():
            widget.destroy()

        label_nombre = tk.Label(frame_func4, text="Digite su nombre:")
        label_nombre.pack(pady=5)

        entry_nombre = tk.Entry(frame_func4)
        entry_nombre.pack(pady=5)

        label_genero = tk.Label(frame_func4, text="Escoja su género:")
        label_genero.pack(pady=5)

        var_genero = tk.IntVar()
        radio_masc = tk.Radiobutton(frame_func4, text="Masculino", variable=var_genero, value=1)
        radio_masc.pack()
        radio_fem = tk.Radiobutton(frame_func4, text="Femenino", variable=var_genero, value=2)
        radio_fem.pack()

        label_edad = tk.Label(frame_func4, text="Digite su edad:")
        label_edad.pack(pady=5)

        entry_edad = tk.Entry(frame_func4)
        entry_edad.pack(pady=5)

        label_decision = tk.Label(frame_func4, text="Desea comprar productos o administrar tiendas:")
        label_decision.pack(pady=5)

        var_decision = tk.IntVar()
        radio_comprar = tk.Radiobutton(frame_func4, text="Comprar productos", variable=var_decision, value=1)
        radio_comprar.pack()
        radio_admin = tk.Radiobutton(frame_func4, text="Administrar tiendas", variable=var_decision, value=2)
        radio_admin.pack()

        def procesar_registro():
            nombre = entry_nombre.get()
            if not nombre.isalpha() or not all(char.isalpha() or char.isspace() for char in nombre):
                messagebox.showerror("Error", "El nombre no puede contener números ni caracteres especiales.")
                return

            try:
                edad = int(entry_edad.get())
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número.")
                return

            if var_genero.get() == 1:
                genero1 = Genero.MASCULINO
            elif var_genero.get() == 2:
                genero1 = Genero.FEMENINO
            else:
                messagebox.showerror("Error", "Debe seleccionar un género.")
                return

            if var_decision.get() == 1:
                persona = Cliente(nombre, p, edad, genero1)
            elif var_decision.get() == 2:
                label_dinero = tk.Label(frame_func4, text="¿Cuánto dinero desea para administrar?:")
                label_dinero.pack(pady=5)

                entry_dinero = tk.Entry(frame_func4)
                entry_dinero.pack(pady=5)

                def confirmar_dinero():
                    try:
                        dinero = float(entry_dinero.get())
                        persona = Administrador(nombre, p, edad, genero1, dinero)
                        messagebox.showinfo("Usuario creado", f"Bienvenido {nombre}")
                        Persona.personas.append(persona)
                    except ValueError:
                        messagebox.showerror("Error", "El dinero debe ser un número.")

                boton_confirmar_dinero = tk.Button(frame_func4, text="Confirmar dinero", command=confirmar_dinero)
                boton_confirmar_dinero.pack(pady=10)

        boton_confirmar = tk.Button(frame_func4, text="Registrar", command=procesar_registro)
        boton_confirmar.pack(pady=10)

    # Limpiar frame_func4 para mostrar el primer paso (entrada del documento)
    label_doc = tk.Label(frame_func4, text="Digite su documento:")
    label_doc.pack(pady=5)

    entry_doc = tk.Entry(frame_func4)
    entry_doc.pack(pady=5)

    boton_siguiente = tk.Button(frame_func4, text="Siguiente", command=procesar_documento)
    boton_siguiente.pack(pady=10)