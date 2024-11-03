import tkinter as tk
from tkinter import messagebox
from modelo.biblioteca import Biblioteca
from modelo.libro import Libro
from modelo.usuario import Usuario
from modelo.administrador import Administrador

biblioteca = Biblioteca()
admin = Administrador("Alice", 1)
usuario = Usuario("Juan", 2)

admin.agregar_libro(biblioteca, Libro("El Quijote", "Miguel de Cervantes"))
admin.agregar_libro(biblioteca, Libro("Cien Años de Soledad", "Gabriel García Márquez"))
admin.agregar_libro(biblioteca, Libro("La casa de las sombras", "Adam Nevill"))
admin.agregar_libro(biblioteca, Libro("Dispersión", "Iain Reid"))

class InterfazBiblioteca:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gestión de Biblioteca")

        self.titulo_label = tk.Label(master, text="Título del Libro:")
        self.titulo_label.pack()
        self.titulo_entry = tk.Entry(master)
        self.titulo_entry.pack()

        self.autor_label = tk.Label(master, text="Autor del Libro:")
        self.autor_label.pack()
        self.autor_entry = tk.Entry(master)
        self.autor_entry.pack()

        # Botones para funcionalidades
        self.mostrar_catalogo_button = tk.Button(master, text="Mostrar Catálogo", command=self.mostrar_catalogo)
        self.mostrar_catalogo_button.pack()

        self.buscar_por_titulo_button = tk.Button(master, text="Buscar por Título", command=self.buscar_por_titulo)
        self.buscar_por_titulo_button.pack()

        self.buscar_por_autor_button = tk.Button(master, text="Buscar por Autor", command=self.buscar_por_autor)
        self.buscar_por_autor_button.pack()

        self.reservar_libro_button = tk.Button(master, text="Reservar Libro", command=self.reservar_libro)
        self.reservar_libro_button.pack()

        self.devolver_libro_button = tk.Button(master, text="Devolver Libro", command=self.devolver_libro)
        self.devolver_libro_button.pack()

        self.ver_historial_button = tk.Button(master, text="Ver Historial de Reservas", command=self.ver_historial)
        self.ver_historial_button.pack()

        self.agregar_libro_button = tk.Button(master, text="Agregar Libro (Admin)", command=self.agregar_libro)
        self.agregar_libro_button.pack()

        self.eliminar_libro_button = tk.Button(master, text="Eliminar Libro (Admin)", command=self.eliminar_libro)
        self.eliminar_libro_button.pack()

        self.mostrar_detalle_button = tk.Button(master, text="Mostrar Detalle del Libro", command=self.mostrar_detalle)
        self.mostrar_detalle_button.pack()

        self.catalogo_text = tk.Text(master, height=15, width=50)
        self.catalogo_text.pack()

    def mostrar_catalogo(self):
        """Muestra el catálogo en el área de texto."""
        self.catalogo_text.delete(1.0, tk.END)  
        catalogo = biblioteca.mostrar_catalogo()
        if catalogo:
            for libro in catalogo:
                self.catalogo_text.insert(tk.END, f"{libro.titulo} - {libro.autor}\n")
        else:
            self.catalogo_text.insert(tk.END, "No hay libros en el catálogo.\n")

    def buscar_por_titulo(self):
        """Busca un libro por título y muestra los resultados."""
        titulo = self.titulo_entry.get()
        libros_encontrados = biblioteca.buscar_libro_por_titulo(titulo)
        self.catalogo_text.delete(1.0, tk.END)
        if libros_encontrados:
            for libro in libros_encontrados:
                self.catalogo_text.insert(tk.END, f"{libro.titulo} - {libro.autor}\n")
        else:
            self.catalogo_text.insert(tk.END, "No se encontraron libros con ese título.\n")

    def buscar_por_autor(self):
        """Busca un libro por autor y muestra los resultados."""
        autor = self.autor_entry.get()
        libros_encontrados = biblioteca.buscar_libro_por_autor(autor)
        self.catalogo_text.delete(1.0, tk.END)
        if libros_encontrados:
            for libro in libros_encontrados:
                self.catalogo_text.insert(tk.END, f"{libro.titulo} - {libro.autor}\n")
        else:
            self.catalogo_text.insert(tk.END, "No se encontraron libros de ese autor.\n")

    def reservar_libro(self):
        """Reserva un libro y muestra un mensaje."""
        titulo = self.titulo_entry.get()
        mensaje = biblioteca.reservar_libro(usuario, titulo)
        messagebox.showinfo("Reserva", mensaje)

    def devolver_libro(self):
        """Devuelve un libro y muestra un mensaje."""
        titulo = self.titulo_entry.get()
        mensaje = biblioteca.devolver_libro(usuario, titulo)
        messagebox.showinfo("Devolución", mensaje)

    def ver_historial(self):
        """Muestra el historial de reservas del usuario."""
        historial = biblioteca.ver_historial_reservas(usuario)
        self.catalogo_text.delete(1.0, tk.END)
        if historial:
            for libro in historial:
                self.catalogo_text.insert(tk.END, f"{libro.titulo} - {libro.autor}\n")
        else:
            self.catalogo_text.insert(tk.END, "No hay historial de reservas.\n")

    def agregar_libro(self):
        """Agrega un libro a la biblioteca (solo admin)."""
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        nuevo_libro = Libro(titulo, autor)
        biblioteca.agregar_libro(nuevo_libro)
        messagebox.showinfo("Agregar Libro", f"El libro '{titulo}' ha sido agregado.")

    def eliminar_libro(self):
        """Elimina un libro de la biblioteca (solo admin)."""
        titulo = self.titulo_entry.get()
        biblioteca.eliminar_libro(titulo)
        messagebox.showinfo("Eliminar Libro", f"El libro '{titulo}' ha sido eliminado.")

    def mostrar_detalle(self):
        """Muestra los detalles de un libro específico."""
        titulo = self.titulo_entry.get()
        libro = biblioteca.mostrar_detalle_libro(titulo)
        self.catalogo_text.delete(1.0, tk.END)
        if isinstance(libro, Libro):
            self.catalogo_text.insert(tk.END, f"Detalles del libro:\nTítulo: {libro.titulo}\nAutor: {libro.autor}\n")
        else:
            self.catalogo_text.insert(tk.END, libro)

def iniciar_aplicacion():
    root = tk.Tk()
    app = InterfazBiblioteca(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
