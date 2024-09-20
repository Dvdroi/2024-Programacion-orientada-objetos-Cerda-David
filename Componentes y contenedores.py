import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar evento a la lista
def agregar_evento():
    fecha = date_entry.get()
    hora = time_entry.get()
    descripcion = descripcion_entry.get()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    # Agregar evento al TreeView
    tree.insert("", tk.END, values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada
    limpiar_campos()

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccion = tree.selection()
    if seleccion:
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirmacion:
            tree.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")

# Función para limpiar los campos de entrada
def limpiar_campos():
    date_entry.set_date("")
    time_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

# Configurar la ventana principal
root = tk.Tk()
root.title("Agenda Personal Modular")

# Crear Frame para los campos de entrada
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Widgets de entrada
tk.Label(input_frame, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(input_frame, width=12, background='darkblue',
                       foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Hora").grid(row=1, column=0, padx=5, pady=5)
time_entry = tk.Entry(input_frame)
time_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = tk.Entry(input_frame)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Crear Frame para los botones
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Botones para agregar y eliminar eventos
agregar_button = tk.Button(button_frame, text="Agregar Evento", command=agregar_evento)
agregar_button.grid(row=0, column=0, padx=5, pady=5)

eliminar_button = tk.Button(button_frame, text="Eliminar Evento", command=eliminar_evento)
eliminar_button.grid(row=0, column=1, padx=5, pady=5)

# Botón para salir de la aplicación
salir_button = tk.Button(button_frame, text="Salir", command=root.quit)
salir_button.grid(row=0, column=2, padx=5, pady=5)

# Crear TreeView para mostrar los eventos
tree_frame = tk.Frame(root)
tree_frame.pack(padx=10, pady=10)

tree = ttk.Treeview(tree_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Iniciar la aplicación
root.mainloop()
