class Cliente:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} | Email: {self.email}"
