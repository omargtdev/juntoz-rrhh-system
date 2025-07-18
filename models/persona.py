from abc import ABC, abstractmethod
from datetime import date

class Persona(ABC):
    """Clase abstracta que representa a una persona."""
    def __init__(self, dni: str, nombre: str, apellido: str, fecha_nacimiento: date):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def dni(self):
        return self._dni

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre_completo}"
