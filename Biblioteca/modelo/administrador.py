from modelo.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)

    def agregar_libro(self, biblioteca, libro):
        biblioteca.agregar_libro(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado al catálogo.")

    def eliminar_libro(self, biblioteca, libro):
        biblioteca.eliminar_libro(libro)
        print(f"El libro '{libro.titulo}' ha sido eliminado del catálogo.")
