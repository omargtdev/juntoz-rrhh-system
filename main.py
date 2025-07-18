from datetime import date, datetime, time
from services.sistema_rrhh import SistemaRRHH
from models.empleado import Empleado, AdministradorRRHH
from models.gestion import Vacaciones, Capacitacion, Asistencia
from models.finanzas import Bonificacion

def inicializar_datos(sistema: SistemaRRHH):
    """Crea datos de ejemplo para probar el sistema."""
    # Empleados de ejemplo
    emp1 = Empleado("12345678", "Juan", "Perez", date(1990, 5, 15), "Desarrollador", 4500.0, date(2022, 1, 10))
    emp1.agregar_beneficio(Bonificacion(300))
    emp1.agregar_vacaciones(Vacaciones(date(2024, 8, 1), date(2024, 8, 15)))
    emp1.agregar_capacitacion(Capacitacion("Python Avanzado", date(2023, 11, 20), 40))
    
    emp2 = Empleado("87654321", "Maria", "Gomez", date(1995, 8, 20), "Diseñadora UX", 4200.0, date(2023, 3, 15))
    
    admin = AdministradorRRHH("11223344", "Carlos", "Santana", date(1985, 2, 1), 6000.0, date(2020, 5, 1), "admin123")

    sistema.registrar_empleado(emp1)
    sistema.registrar_empleado(emp2)
    sistema.registrar_empleado(admin)
    print("\n--- Datos de ejemplo cargados ---")

def menu_principal():
    print("\n=====================================")
    print("  SISTEMA DE GESTIÓN DE RRHH")
    print("=====================================")
    print("1. Registrar nuevo empleado")
    print("2. Buscar empleado")
    print("3. Calcular sueldo neto de un empleado")
    print("4. Registrar vacaciones")
    print("5. Registrar capacitación")
    print("6. Registrar asistencia")
    print("7. Generar reporte")
    print("8. Modificar datos de empleado")
    print("9. Eliminar empleado (marcar como inactivo)")
    print("10. Listar todos los empleados")
    print("0. Salir")
    print("=====================================")
    return input("Seleccione una opción: ")

def main():
    sistema = SistemaRRHH()
    inicializar_datos(sistema)

    while True:
        opcion = menu_principal()

        if opcion == '1':
            print("\n--- Registro de Nuevo Empleado ---")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            fnac_str = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            cargo = input("Cargo: ")
            sueldo = float(input("Sueldo Base: "))
            fcon_str = input("Fecha de Contratación (YYYY-MM-DD): ")
            nuevo_empleado = Empleado(dni, nombre, apellido, date.fromisoformat(fnac_str), cargo, sueldo, date.fromisoformat(fcon_str))
            sistema.registrar_empleado(nuevo_empleado)

        elif opcion == '2':
            termino = input("Ingrese DNI o nombre del empleado a buscar: ")
            empleado = sistema.buscar_empleado(termino)
            if empleado:
                print("\n--- Información del Empleado ---")
                print(empleado)
            else:
                print("\n❌ Empleado no encontrado.")

        elif opcion == '3':
            dni = input("Ingrese DNI del empleado para calcular sueldo: ")
            empleado = sistema.buscar_empleado(dni)
            if empleado:
                print(f"\n💵 El sueldo neto de {empleado.nombre_completo} es: S/ {empleado.calcular_sueldo_neto()}")
            else:
                print("\n❌ Empleado no encontrado.")
        
        elif opcion == '4':
            dni = input("Ingrese DNI del empleado para registrar vacaciones: ")
            empleado = sistema.buscar_empleado(dni)
            if empleado:
                inicio_str = input("Fecha de inicio (YYYY-MM-DD): ")
                fin_str = input("Fecha de fin (YYYY-MM-DD): ")
                vac = Vacaciones(date.fromisoformat(inicio_str), date.fromisoformat(fin_str))
                empleado.agregar_vacaciones(vac)
                print("\n✅ Vacaciones registradas.")
            else:
                print("\n❌ Empleado no encontrado.")

        elif opcion == '5':
            dni = input("Ingrese DNI del empleado para registrar vacaciones: ")
            empleado = sistema.buscar_empleado(dni)
            if empleado:
                nombre_curso = input("Nombre del curso: ")
                inicio_str = input("Fecha de inicio (YYYY-MM-DD): ")
                duracion_horas = int(input("Horas: "))
                capacitacion = Capacitacion(nombre_curso, date.fromisoformat(inicio_str), duracion_horas)
                empleado.agregar_capacitacion(capacitacion)
                print("\n✅ Capacitación registrada.")
            else:
                print("\n❌ Empleado no encontrado.")
        
        elif opcion == '6':
            dni = input("Ingrese DNI del empleado para registrar asistencia: ")
            empleado = sistema.buscar_empleado(dni)
            if empleado:
                fecha_str = input("Fecha (YYYY-MM-DD): ")
                entrada_str = input("Hora de entrada (HH:MM): ")
                salida_str = input("Hora de salida (HH:MM): ")
                asist = Asistencia(date.fromisoformat(fecha_str), time.fromisoformat(entrada_str), time.fromisoformat(salida_str))
                empleado.agregar_asistencia(asist)
                print(f"\n✅ Asistencia registrada. Horas trabajadas: {asist.calcular_horas():.2f}")
            else:
                print("\n❌ Empleado no encontrado.")

        elif opcion == '7':
            dni = input("Ingrese DNI del empleado para generar el reporte: ")
            tipo = input("Tipo de reporte ('sueldo' o 'vacaciones'): ").lower()
            reporte = sistema.generar_reporte(dni, tipo)
            print(reporte)
        
        elif opcion == '8':
            dni = input("Ingrese DNI del empleado a modificar: ")
            empleado = sistema.buscar_empleado(dni)
            if empleado:
                print(f"Modificando a: {empleado.nombre_completo}")
                nuevo_cargo = input(f"Nuevo cargo (actual: {empleado.cargo}): ")
                nuevo_sueldo = float(input(f"Nuevo sueldo (actual: {empleado.sueldo_base}): "))
                sistema.modificar_empleado(dni, nuevo_cargo, nuevo_sueldo)
            else:
                print("\n❌ Empleado no encontrado.")

        elif opcion == '9':
            dni = input("Ingrese DNI del empleado a eliminar: ")
            sistema.eliminar_empleado(dni)
            
        elif opcion == '10':
            print("\n--- Listado de Empleados ---")
            sistema.listar_empleados()

        elif opcion == '0':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
