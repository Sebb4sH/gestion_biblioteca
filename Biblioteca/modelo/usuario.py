class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_reservas = []

    def reservar_libro(self, libro):
        if libro.disponible:
            libro.reservar()
            self.historial_reservas.append(libro)
        else:
            print(f"Lo siento, el libro '{libro.titulo}' no está disponible para reserva.")

    def devolver_libro(self, libro):
        if libro in self.historial_reservas:
            libro.devolver()
            self.historial_reservas.remove(libro)
        else:
            print(f"El libro '{libro.titulo}' no está en su historial de reservas.")

    def ver_historial_reservas(self):
        print(f"Historial de reservas de {self.nombre}:")
        for libro in self.historial_reservas:
            print(f"- {libro.titulo}")

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"
