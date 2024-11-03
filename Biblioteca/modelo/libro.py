class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True 
    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido reservado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para reserva.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto y ahora está disponible.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        return f"{self.titulo} de {self.autor} - {'Disponible' if self.disponible else 'Reservado'}"
