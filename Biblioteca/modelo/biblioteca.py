from modelo.libro import Libro
from modelo.usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.catalogo_libros = []  
        self.reservas = {}  
    
    def agregar_libro(self, libro):
        """Agrega un libro al catálogo."""
        self.catalogo_libros.append(libro)
    
    def eliminar_libro(self, titulo):
        """Elimina un libro del catálogo según su título."""
        self.catalogo_libros = [libro for libro in self.catalogo_libros if libro.titulo != titulo]

    def buscar_libro_por_titulo(self, titulo):
        """Busca libros por título."""
        return [libro for libro in self.catalogo_libros if titulo.lower() in libro.titulo.lower()]

    def buscar_libro_por_autor(self, autor):
        """Busca libros por autor."""
        return [libro for libro in self.catalogo_libros if autor.lower() in libro.autor.lower()]

    def reservar_libro(self, usuario, titulo):
        """Permite a un usuario reservar un libro."""
        libro = next((libro for libro in self.catalogo_libros if libro.titulo == titulo), None)
        if libro:
            self.catalogo_libros.remove(libro)
            if usuario not in self.reservas:
                self.reservas[usuario] = []
            self.reservas[usuario].append(libro)
            return f"El libro '{titulo}' ha sido reservado."
        return f"El libro '{titulo}' no está disponible."

    def devolver_libro(self, usuario, titulo):
        """Permite a un usuario devolver un libro reservado."""
        if usuario in self.reservas:
            libro = next((libro for libro in self.reservas[usuario] if libro.titulo == titulo), None)
            if libro:
                self.reservas[usuario].remove(libro)
                self.catalogo_libros.append(libro)
                return f"El libro '{titulo}' ha sido devuelto."
        return f"No se encontró una reserva del libro '{titulo}' para el usuario."

    def ver_historial_reservas(self, usuario):
        """Devuelve el historial de reservas de un usuario."""
        if usuario in self.reservas:
            return self.reservas[usuario]
        return []

    def mostrar_catalogo(self):
        """Devuelve una lista de todos los libros en el catálogo."""
        return self.catalogo_libros

    def mostrar_detalle_libro(self, titulo):
        """Devuelve el detalle de un libro específico."""
        libro = next((libro for libro in self.catalogo_libros if libro.titulo == titulo), None)
        return libro if libro else f"No se encontró el libro '{titulo}'."
