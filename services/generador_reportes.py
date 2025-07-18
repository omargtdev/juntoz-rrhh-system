from abc import ABC, abstractmethod
from models.empleado import Empleado

class Reporte(ABC):
    @abstractmethod
    def generar_contenido(self, empleado: Empleado) -> str:
        pass

class ReporteSueldo(Reporte):
    def generar_contenido(self, empleado: Empleado) -> str:
        sueldo_neto = empleado.calcular_sueldo_neto()
        contenido = f"""
        **************************************
        * REPORTE DE SUELDO           *
        **************************************
        Empleado: {empleado.nombre_completo} (ID: {empleado.id_empleado})
        Cargo: {empleado.cargo}
        --------------------------------------
        Sueldo Base:      S/ {empleado.sueldo_base:.2f}
        Sueldo Neto:      S/ {sueldo_neto:.2f}
        **************************************
        """
        return contenido

class ReporteVacaciones(Reporte):
    def generar_contenido(self, empleado: Empleado) -> str:
        contenido = f"""
        **************************************
        * REPORTE DE VACACIONES         *
        **************************************
        Empleado: {empleado.nombre_completo} (ID: {empleado.id_empleado})
        --------------------------------------
        """
        if not empleado._Empleado__vacaciones:
            contenido += "No hay registros de vacaciones.\n"
        else:
            for vac in empleado._Empleado__vacaciones:
                contenido += f"- Del {vac.fecha_inicio} al {vac.fecha_fin} ({vac.calcular_dias()} días) | Estado: {vac.estado}\n"
        
        contenido += "**************************************\n"
        return contenido
