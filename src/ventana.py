import tkinter as tk
from tkinter import messagebox

def mostrar_mensage():
    messagebox.showinfo("Aviso", "¡Boton precinado!")
ventana= tk.Tk() #crea la ventana principal
ventana.title("Ventana simple") #Le damos un titulo

label= tk.Label(ventana, text="Preciona el boton para ver un mensaje")
label.pack(pady=10)
    
boton= tk. Button(ventana, text="Haz cick aqui", command=mostrar_mensage)
boton.pack(pady=10)
    


import tkinter as tk

ventana.mainloop()  #Muestra la ventana y la mantiene activa hasta que el ususario le de click en salir. 