class Login:
    def __init__(self):
        self.usuarios = {
            "usuario": "123456",
            "admin": "admin123"
        }

    def verificar_login(self, username, password):
        """Verifica el login del usuario."""
        if username in self.usuarios and self.usuarios[username] == password:
            return username == "admin" 
        return False
