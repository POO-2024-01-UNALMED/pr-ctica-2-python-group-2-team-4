import tkinter as tk

root = tk.Tk()
root.title("Ventana Principal de Inicio")

# Frame principal con padding superior
frame_principal = tk.Frame(root, padx=10, pady=10, bd=2, relief="solid")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Crear el menú en el cuadro principal
menu_button = tk.Menubutton(frame_principal, text="Inicio", fg="red", relief="raised")
menu_button.menu = tk.Menu(menu_button, tearoff=0)
menu_button["menu"] = menu_button.menu

menu_button.menu.add_command(label="Opción 1")
menu_button.menu.add_command(label="Opción 2")

menu_button.pack(anchor="nw", padx=5, pady=5)

# Divisiones P1 y P2
frame_p1 = tk.Frame(frame_principal, padx=5, pady=5, bd=2, relief="solid")
frame_p1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

frame_p2 = tk.Frame(frame_principal, padx=5, pady=5, bd=2, relief="solid")
frame_p2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Divisiones P3 y P4 en P1
frame_p3 = tk.Frame(frame_p1, height=100, padx=5, pady=5, bd=2, relief="solid")
frame_p3.pack(fill=tk.X, padx=5, pady=5)

frame_p4 = tk.Frame(frame_p1, padx=5, pady=5, bd=2, relief="solid")
frame_p4.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Divisiones P5 y P6 en P2
frame_p5 = tk.Frame(frame_p2, height=100, padx=5, pady=5, bd=2, relief="solid")
frame_p5.pack(fill=tk.X, padx=5, pady=5)

frame_p6 = tk.Frame(frame_p2, padx=5, pady=5, bd=2, relief="solid")
frame_p6.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()

