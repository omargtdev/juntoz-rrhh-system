from models.empleado import Empleado
from typing import List, Optional
from .generador_reportes import ReporteSueldo, ReporteVacaciones

class SistemaRRHH:
    """Clase que gestiona todas las operaciones de RRHH."""
    def __init__(self):
        self.__empleados: List[Empleado] = []

    def registrar_empleado(self, empleado: Empleado):
        self.__empleados.append(empleado)
        print(f"\n✅ Empleado '{empleado.nombre_completo}' registrado con éxito con ID: {empleado.id_empleado}")

    def buscar_empleado(self, termino: str) -> Optional[Empleado]:
        termino = termino.lower()
        for emp in self.__empleados:
            if emp.dni == termino or termino in emp.nombre_completo.lower():
                return emp
        return None

    def listar_empleados(self):
        if not self.__empleados:
            print("No hay empleados registrados.")
            return
        for emp in self.__empleados:
            print(emp)

    def modificar_empleado(self, dni: str, nuevo_cargo: str, nuevo_sueldo: float):
        empleado = self.buscar_empleado(dni)
        if empleado:
            empleado.cargo = nuevo_cargo
            empleado.sueldo_base = nuevo_sueldo
            print("\n✅ Datos del empleado actualizados.")
            return True
        print("\n❌ Empleado no encontrado.")
        return False

    def eliminar_empleado(self, dni: str):
        empleado = self.buscar_empleado(dni)
        if empleado:
            empleado.estado = "Inactivo" # Borrado lógico
            # self.__empleados.remove(empleado) # Para borrado físico
            print(f"\n✅ Empleado '{empleado.nombre_completo}' ha sido marcado como Inactivo.")
            return True
        print("\n❌ Empleado no encontrado.")
        return False

    def generar_reporte(self, dni: str, tipo_reporte: str) -> Optional[str]:
        empleado = self.buscar_empleado(dni)
        if not empleado:
            return "❌ Empleado no encontrado."
            
        if tipo_reporte == 'sueldo':
            generador = ReporteSueldo()
        elif tipo_reporte == 'vacaciones':
            generador = ReporteVacaciones()
        else:
            return "❌ Tipo de reporte no válido."
            
        return generador.generar_contenido(empleado)
