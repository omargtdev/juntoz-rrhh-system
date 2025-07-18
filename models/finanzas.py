from abc import ABC, abstractmethod

class Beneficio(ABC):
    """Clase abstracta para representar beneficios o descuentos."""
    def __init__(self, tipo: str):
        self._tipo = tipo

    @abstractmethod
    def calcular_valor(self, sueldo_base: float) -> float:
        pass

class AFP(Beneficio):
    """Descuento de AFP. Retorna un valor negativo."""
    def __init__(self, porcentaje_descuento: float = 10.0):
        super().__init__("AFP")
        self.__porcentaje_descuento = porcentaje_descuento

    def calcular_valor(self, sueldo_base: float) -> float:
        return - (sueldo_base * self.__porcentaje_descuento / 100)

class ImpuestoRenta(Beneficio):
    """Descuento de Impuesto a la Renta. Retorna un valor negativo."""
    def __init__(self, porcentaje_retencion: float = 8.0):
        super().__init__("Impuesto a la Renta")
        self.__porcentaje_retencion = porcentaje_retencion

    def calcular_valor(self, sueldo_base: float) -> float:
        if sueldo_base > 3000:
            return - (sueldo_base * self.__porcentaje_retencion / 100)
        return 0.0

class Bonificacion(Beneficio):
    """Bonificación fija. Retorna un valor positivo."""
    def __init__(self, monto_fijo: float):
        super().__init__("Bonificación")
        self.__monto_fijo = monto_fijo

    def calcular_valor(self, sueldo_base: float) -> float:
        return self.__monto_fijo
