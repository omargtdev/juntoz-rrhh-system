from datetime import date, datetime

class Contrato:
    def __init__(self, tipo_contrato: str, fecha_inicio: date, fecha_fin: date):
        self.tipo_contrato = tipo_contrato
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def validar_contrato(self) -> bool:
        return date.today() <= self.fecha_fin

class Asistencia:
    def __init__(self, fecha: date, hora_entrada: datetime.time, hora_salida: datetime.time):
        self.fecha = fecha
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida

    def calcular_horas(self) -> float:
        entrada = datetime.combine(self.fecha, self.hora_entrada)
        salida = datetime.combine(self.fecha, self.hora_salida)
        return (salida - entrada).total_seconds() / 3600

class Vacaciones:
    def __init__(self, fecha_inicio: date, fecha_fin: date, estado: str = "Aprobado"):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def calcular_dias(self) -> int:
        return (self.fecha_fin - self.fecha_inicio).days + 1

class Capacitacion:
    def __init__(self, nombre_curso: str, fecha: date, duracion_horas: int):
        self.nombre_curso = nombre_curso
        self.fecha = fecha
        self.duracion_horas = duracion_horas
