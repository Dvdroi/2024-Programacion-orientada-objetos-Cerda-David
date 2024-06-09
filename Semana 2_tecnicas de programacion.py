class ItemBiblioteca:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Código:", self.codigo)
        estado = "Disponible" if self.disponible else "No disponible"
        print("Estado:", estado)


class Libro(ItemBiblioteca):
    def __init__(self, titulo, autor, codigo, genero):
        super().__init__(titulo, autor, codigo)
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print("Género:", self.genero)


class Pelicula(ItemBiblioteca):
    def __init__(self, titulo, autor, codigo, duracion):
        super().__init__(titulo, autor, codigo)
        self.duracion = duracion

    def mostrar_info(self):
        super().mostrar_info()
        print("Duración:", self.duracion, "minutos")


# Crear algunos ítems de la biblioteca
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "L001", "Realismo mágico")
pelicula1 = Pelicula("El Padrino", "Francis Ford Coppola", "P001", 175)
libro2 = Libro("1984", "George Orwell", "L002", "Ciencia ficción")
pelicula2 = Pelicula("Pulp Fiction", "Quentin Tarantino", "P002", 154)

# Mostrar información de los ítems de la biblioteca
print("Información del Libro 1:")
libro1.mostrar_info()
print("\nInformación de la Película 1:")
pelicula1.mostrar_info()
print("\nInformación del Libro 2:")
libro2.mostrar_info()
print("\nInformación de la Película 2:")
pelicula2.mostrar_info()
