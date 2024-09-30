import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Libros")
        self.master.geometry("500x400")

        self.books = []

        # Frame para entrada de datos
        self.input_frame = ttk.Frame(self.master, padding="10")
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campos de entrada
        ttk.Label(self.input_frame, text="Título:").grid(row=0, column=0, sticky=tk.W)
        self.title_entry = ttk.Entry(self.input_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(self.input_frame, text="Autor:").grid(row=1, column=0, sticky=tk.W)
        self.author_entry = ttk.Entry(self.input_frame, width=30)
        self.author_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(self.input_frame, text="Año:").grid(row=2, column=0, sticky=tk.W)
        self.year_entry = ttk.Entry(self.input_frame, width=30)
        self.year_entry.grid(row=2, column=1, padx=5, pady=2)

        # Botones
        self.add_button = ttk.Button(self.input_frame, text="Agregar Libro", command=self.add_book)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.mark_button = ttk.Button(self.input_frame, text="Marcar como Leído", command=self.mark_as_read)
        self.mark_button.grid(row=4, column=0, pady=5)

        self.delete_button = ttk.Button(self.input_frame, text="Eliminar Libro", command=self.delete_book)
        self.delete_button.grid(row=4, column=1, pady=5)

        # Lista de libros
        self.book_tree = ttk.Treeview(self.master, columns=('Title', 'Author', 'Year', 'Status'), show='headings')
        self.book_tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        self.book_tree.heading('Title', text='Título')
        self.book_tree.heading('Author', text='Autor')
        self.book_tree.heading('Year', text='Año')
        self.book_tree.heading('Status', text='Estado')

        self.book_tree.column('Title', width=150)
        self.book_tree.column('Author', width=150)
        self.book_tree.column('Year', width=50)
        self.book_tree.column('Status', width=100)

        # Configurar expansión de widgets
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()

        if title and author and year:
            self.books.append({"title": title, "author": author, "year": year, "read": False})
            self.update_book_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")

    def mark_as_read(self):
        selected_item = self.book_tree.selection()
        if selected_item:
            item = selected_item[0]
            book = self.books[int(item[1:]) - 1]
            book["read"] = not book["read"]
            self.update_book_list()

    def delete_book(self):
        selected_item = self.book_tree.selection()
        if selected_item:
            item = selected_item[0]
            del self.books[int(item[1:]) - 1]
            self.update_book_list()

    def update_book_list(self):
        self.book_tree.delete(*self.book_tree.get_children())
        for i, book in enumerate(self.books, 1):
            status = "Leído" if book["read"] else "No leído"
            self.book_tree.insert('', 'end', iid=f'I{i:03d}', values=(book["title"], book["author"], book["year"], status))

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()