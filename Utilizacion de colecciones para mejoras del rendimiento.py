from typing import List, Tuple, Dict, Set

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self.info: Tuple[str, str] = (titulo, autor)
        self.categoria: str = categoria
        self.isbn: str = isbn

    @property
    def titulo(self) -> str:
        return self.info[0]

    @property
    def autor(self) -> str:
        return self.info[1]

    def __str__(self) -> str:
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[Libro] = []

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios: Set[str] = set()
        self.prestamos: Dict[str, List[Libro]] = {}

    def agregar_libro(self, libro: Libro) -> None:
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn: str) -> None:
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro removido: {libro}")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.prestamos[usuario.id_usuario] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("ID de usuario ya existe.")

    def dar_baja_usuario(self, id_usuario: str) -> None:
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.prestamos[id_usuario]
            print(f"Usuario dado de baja: {id_usuario}")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn: str, id_usuario: str) -> None:
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            self.prestamos[id_usuario].append(libro)
            print(f"Libro prestado: {libro} a Usuario ID: {id_usuario}")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn: str, id_usuario: str) -> None:
        if id_usuario in self.prestamos:
            for libro in self.prestamos[id_usuario]:
                if libro.isbn == isbn:
                    self.prestamos[id_usuario].remove(libro)
                    print(f"Libro devuelto: {libro} por Usuario ID: {id_usuario}")
                    return
        print("Préstamo no encontrado.")

    def buscar_libros(self, criterio: str, valor: str) -> List[Libro]:
        resultados = []
        for libro in self.libros.values():
            if criterio == 'titulo' and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario: str) -> List[Libro]:
        if id_usuario in self.prestamos:
            return self.prestamos[id_usuario]
        else:
            print("Usuario no encontrado.")
            return []

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro("1984", "George Orwell", "Ficción", "9780451524935")
    libro2 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "9780547928227")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Ana García", "U001")
    usuario2 = Usuario("Carlos López", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("9780451524935", "U001")
    biblioteca.prestar_libro("9780547928227", "U002")

    # Buscar libros
    print("\nBúsqueda de libros por autor 'Orwell':")
    for libro in biblioteca.buscar_libros('autor', 'Orwell'):
        print(libro)

    # Listar libros prestados
    print("\nLibros prestados a Ana García:")
    for libro in biblioteca.listar_libros_prestados("U001"):
        print(libro)

    # Devolver un libro
    biblioteca.devolver_libro("9780451524935", "U001")

    # Dar de baja a un usuario
    biblioteca.dar_baja_usuario("U002")