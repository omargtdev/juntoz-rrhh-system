import uuid
from datetime import date
from .persona import Persona
from .finanzas import Beneficio, AFP, ImpuestoRenta
from typing import List

class Empleado(Persona):
    """Representa a un empleado de la empresa."""
    def __init__(self, dni: str, nombre: str, apellido: str, fecha_nacimiento: date, cargo: str, sueldo_base: float, fecha_contratacion: date):
        super().__init__(dni, nombre, apellido, fecha_nacimiento)
        self.__id_empleado = str(uuid.uuid4())[:8]
        self._cargo = cargo
        self._sueldo_base = sueldo_base
        self._fecha_contratacion = fecha_contratacion
        self._estado = "Activo"
        
        # Agregaciones / Composiciones
        self.__contratos: List = []
        self.__asistencias: List = []
        self.__vacaciones: List = []
        self.__capacitaciones: List = []
        self.__beneficios: List[Beneficio] = [AFP(), ImpuestoRenta()]

    @property
    def id_empleado(self):
        return self.__id_empleado
    
    @property
    def sueldo_base(self):
        return self._sueldo_base
        
    @sueldo_base.setter
    def sueldo_base(self, valor):
        self._sueldo_base = valor

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, nuevo_cargo):
        self._cargo = nuevo_cargo

    @property
    def estado(self):
        return self._estado
        
    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def agregar_beneficio(self, beneficio: Beneficio):
        self.__beneficios.append(beneficio)
        
    def agregar_vacaciones(self, vacaciones):
        self.__vacaciones.append(vacaciones)

    def agregar_capacitacion(self, capacitacion):
        self.__capacitaciones.append(capacitacion)
        
    def agregar_asistencia(self, asistencia):
        self.__asistencias.append(asistencia)

    def calcular_sueldo_neto(self) -> float:
        """Calcula el sueldo neto sumando/restando los beneficios."""
        sueldo_neto = self._sueldo_base
        for beneficio in self.__beneficios:
            sueldo_neto += beneficio.calcular_valor(self._sueldo_base)
        return round(sueldo_neto, 2)

    def __str__(self):
        return f"ID: {self.id_empleado} | {super().__str__()} | Cargo: {self.cargo} | Estado: {self.estado}"

class AdministradorRRHH(Empleado):
    """Un empleado con permisos especiales de RRHH."""
    def __init__(self, dni: str, nombre: str, apellido: str, fecha_nacimiento: date, sueldo_base: float, fecha_contratacion: date, credenciales: str):
        super().__init__(dni, nombre, apellido, fecha_nacimiento, "Administrador RRHH", sueldo_base, fecha_contratacion)
        self.__credenciales = credenciales

    def aprobar_vacaciones(self, vacaciones, estado="Aprobado"):
        vacaciones.estado = estado
        print(f"Vacaciones actualizadas a estado: {estado}")
