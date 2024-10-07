import tkinter as tk
from tkinter import ttk, messagebox

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Contactos")
        self.master.geometry("500x400")

        self.contacts = []

        # Frame para entrada de datos
        self.input_frame = ttk.Frame(self.master, padding="10")
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campos de entrada
        ttk.Label(self.input_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.input_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(self.input_frame, text="Teléfono:").grid(row=1, column=0, sticky=tk.W)
        self.phone_entry = ttk.Entry(self.input_frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(self.input_frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.email_entry = ttk.Entry(self.input_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=2)

        # Botones
        self.add_button = ttk.Button(self.input_frame, text="Añadir Contacto", command=self.add_contact)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)

        self.edit_button = ttk.Button(self.input_frame, text="Editar Contacto", command=self.edit_contact)
        self.edit_button.grid(row=3, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.input_frame, text="Eliminar Contacto", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, padx=5, pady=5)

        self.search_entry = ttk.Entry(self.input_frame, width=20)
        self.search_entry.grid(row=4, column=1, padx=5, pady=5)
        self.search_button = ttk.Button(self.input_frame, text="Buscar", command=self.search_contact)
        self.search_button.grid(row=4, column=2, padx=5, pady=5)

        # Lista de contactos
        self.contact_listbox = tk.Listbox(self.master, width=70, height=15)
        self.contact_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Atajos de teclado
        self.master.bind('<Return>', lambda event: self.add_contact())
        self.master.bind('<Control-e>', lambda event: self.edit_contact())
        self.master.bind('<Delete>', lambda event: self.delete_contact())
        self.master.bind('<Control-f>', lambda event: self.search_entry.focus())
        self.master.bind('<Escape>', lambda event: self.master.quit())

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone:
            contact = f"{name} - {phone} - {email}"
            self.contacts.append(contact)
            self.update_contact_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Datos incompletos", "Por favor, ingrese al menos nombre y teléfono.")

    def edit_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            old_contact = self.contacts[index]
            new_name = self.name_entry.get() or old_contact.split(' - ')[0]
            new_phone = self.phone_entry.get() or old_contact.split(' - ')[1]
            new_email = self.email_entry.get() or old_contact.split(' - ')[2]
            self.contacts[index] = f"{new_name} - {new_phone} - {new_email}"
            self.update_contact_list()
            self.clear_entries()
        except IndexError:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un contacto para editar.")

    def delete_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            del self.contacts[index]
            self.update_contact_list()
        except IndexError:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione un contacto para eliminar.")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        if search_term:
            results = [contact for contact in self.contacts if search_term in contact.lower()]
            self.contact_listbox.delete(0, tk.END)
            for contact in results:
                self.contact_listbox.insert(tk.END, contact)
        else:
            self.update_contact_list()

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()