import tkinter as tk

# nuevo intento 
def mostrar_miniatura(event):
    # Función para mostrar la miniatura en el cuadro grande al pasar el cursor
    imagen_miniatura = event.widget.cget("image")
    cuadro_grande.config(image=imagen_miniatura)


#viejo intento
def on_enter(event, img_label, img):
    img_label.config(image=img)



root = tk.Tk()
root.title("Ventana Principal de Inicio")
root.state('zoomed')

# Frame principal 
frame_principal = tk.Frame(root, padx=10, pady=10, bd=2, relief="solid")
frame_principal.pack(fill=tk.BOTH, expand=True)

# menú en el cuadro principal
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
frame_p3 = tk.Frame(frame_p1, height=180, padx=5, pady=5, bd=2, relief="solid")
frame_p3.pack(fill=tk.X, padx=5, pady=5)

# texto en P3
label_p3 = tk.Label(frame_p3,text="Bienvenido a My_Tiendita donde podrás realizar tus compras o administrar tus tiendas", font=("Helvetica", 10, "bold"))
label_p3.place(x=40, y=50)

frame_p4 = tk.Frame(frame_p1, padx=5, pady=5, bd=2, relief="solid")
frame_p4.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)


#imagen grande 
ruta_imagen = "imagenes/imagen2.png"
imagen = tk.PhotoImage(file=ruta_imagen).subsample(int(200 / 250))

# Crear visualizador 
cuadro_grande = tk.Label(frame_p4, image=imagen, relief="solid", borderwidth=2, width=250, height=250)
cuadro_grande.place(x=200, y=5)  # Ajusta las coordenadas según tu diseño


# #crear plaza miniaturas 
# frame_rectangulo = tk.Frame(frame_p4, bg="black", width=350, height=70)
# frame_rectangulo.place(x=150, y=260)  # Ajusta las coordenadas según tu diseño

# # Rutas de las imágenes
# ruta_imagenes = [
#     "imagenes/imagen1.png",
#     "imagenes/imagen2.png",
#     "imagenes/imagen3.png",
#     "imagenes/imagen4.png",
#     "imagenes/imagen5.png"
# ]

# # Crear miniaturas con las nuevas rutas
# ancho_imagen = 70
# altura_imagen = 70

# # Cargar las imágenes directamente en columnas específicas
# imagen1 = tk.PhotoImage(file=ruta_imagenes[0]).subsample(int(200 / ancho_imagen))
# imagen_label1 = tk.Label(frame_rectangulo, image=imagen1, borderwidth=1, relief="solid", width=ancho_imagen, height=altura_imagen)

# imagen2 = tk.PhotoImage(file=ruta_imagenes[1]).subsample(int(200 / ancho_imagen))
# imagen_label2 = tk.Label(frame_rectangulo, image=imagen2, borderwidth=1, relief="solid", width=ancho_imagen, height=altura_imagen)

# imagen3 = tk.PhotoImage(file=ruta_imagenes[2]).subsample(int(200 / ancho_imagen))
# imagen_label3 = tk.Label(frame_rectangulo, image=imagen3, borderwidth=1, relief="solid", width=ancho_imagen, height=altura_imagen)

# imagen4 = tk.PhotoImage(file=ruta_imagenes[3]).subsample(int(200 / ancho_imagen))
# imagen_label4 = tk.Label(frame_rectangulo, image=imagen4, borderwidth=1, relief="solid", width=ancho_imagen, height=altura_imagen)

# imagen5 = tk.PhotoImage(file=ruta_imagenes[4]).subsample(int(200 / ancho_imagen))
# imagen_label5 = tk.Label(frame_rectangulo, image=imagen5, borderwidth=1, relief="solid", width=ancho_imagen, height=altura_imagen)

# # Ubicar las etiquetas en el grid dentro del frame_rectangulo
# imagen_label1.grid(row=0, column=0)
# imagen_label2.grid(row=0, column=1)
# imagen_label3.grid(row=0, column=2)
# imagen_label4.grid(row=0, column=3)
# imagen_label5.grid(row=0, column=4)




    
# Divisiones P5 y P6 en P2
frame_p5 = tk.Frame(frame_p2, height=180, padx=5, pady=5, bd=2, relief="solid")
frame_p5.pack(fill=tk.X, padx=5, pady=5)

frame_p6 = tk.Frame(frame_p2, padx=5, pady=5, bd=2, relief="solid")
frame_p6.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()










