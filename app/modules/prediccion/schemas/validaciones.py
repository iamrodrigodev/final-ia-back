def validar_estado_civil(v: int) -> int:
    if not (1 <= v <= 6):
        raise ValueError('El Estado Civil debe estar entre 1 y 6')
    return v

def validar_booleano(v: int) -> int:
    if v not in (0, 1):
        raise ValueError('Este campo debe ser 0 o 1')
    return v

def validar_edad(v: int) -> int:
    if not (15 <= v <= 100):
        raise ValueError('La edad debe estar entre 15 y 100')
    return v

def validar_nota_admision(v: float) -> float:
    if not (0.0 <= v <= 200.0):
        raise ValueError('La nota de admisión debe estar entre 0.0 y 200.0')
    return v

def validar_nota_semestre(v: float) -> float:
    if not (0.0 <= v <= 20.0):
        raise ValueError('La nota debe estar entre 0.0 y 20.0')
    return v

def validar_positivo(v: int) -> int:
    if v < 0:
        raise ValueError('El valor no puede ser negativo')
    return v

def validar_curso(v: int) -> int:
    if not (1 <= v <= 10000):
        raise ValueError('El curso debe estar entre 1 y 10000')
    return v

def validar_modo_aplicacion(v: int) -> int:
    if not (1 <= v <= 50):
        raise ValueError('El modo de aplicación debe estar entre 1 y 50')
    return v

def validar_calificacion_previa(v: int) -> int:
    if not (1 <= v <= 50):
        raise ValueError('La calificación previa debe estar entre 1 y 50')
    return v

def validar_orden_aplicacion(v: int) -> int:
    if not (0 <= v <= 9):
        raise ValueError('El orden de aplicación debe estar entre 0 y 9')
    return v

def validar_unidades(v: int) -> int:
    if not (0 <= v <= 50):
        raise ValueError('Las unidades deben estar entre 0 y 50')
    return v
