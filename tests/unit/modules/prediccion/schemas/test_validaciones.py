import pytest
from app.modules.prediccion.schemas.validaciones import (
    validar_estado_civil, validar_booleano, validar_edad, validar_nota_admision,
    validar_nota_semestre, validar_positivo, validar_curso, validar_modo_aplicacion,
    validar_calificacion_previa, validar_orden_aplicacion, validar_unidades
)

def test_validar_estado_civil():
    assert validar_estado_civil(1) == 1
    assert validar_estado_civil(6) == 6
    with pytest.raises(ValueError): validar_estado_civil(0)
    with pytest.raises(ValueError): validar_estado_civil(7)

def test_validar_booleano():
    assert validar_booleano(0) == 0
    assert validar_booleano(1) == 1
    with pytest.raises(ValueError): validar_booleano(-1)
    with pytest.raises(ValueError): validar_booleano(2)

def test_validar_edad():
    assert validar_edad(15) == 15
    assert validar_edad(100) == 100
    with pytest.raises(ValueError): validar_edad(14)
    with pytest.raises(ValueError): validar_edad(101)

def test_validar_nota_admision():
    assert validar_nota_admision(0.0) == 0.0
    assert validar_nota_admision(200.0) == 200.0
    with pytest.raises(ValueError): validar_nota_admision(-0.1)
    with pytest.raises(ValueError): validar_nota_admision(200.1)

def test_validar_nota_semestre():
    assert validar_nota_semestre(0.0) == 0.0
    assert validar_nota_semestre(20.0) == 20.0
    with pytest.raises(ValueError): validar_nota_semestre(-0.1)
    with pytest.raises(ValueError): validar_nota_semestre(20.1)

def test_validar_positivo():
    assert validar_positivo(0) == 0
    assert validar_positivo(10) == 10
    with pytest.raises(ValueError): validar_positivo(-1)

def test_validar_curso():
    assert validar_curso(1) == 1
    assert validar_curso(10000) == 10000
    with pytest.raises(ValueError): validar_curso(0)
    with pytest.raises(ValueError): validar_curso(10001)

def test_validar_modo_aplicacion():
    assert validar_modo_aplicacion(1) == 1
    assert validar_modo_aplicacion(50) == 50
    with pytest.raises(ValueError): validar_modo_aplicacion(0)
    with pytest.raises(ValueError): validar_modo_aplicacion(51)

def test_validar_calificacion_previa():
    assert validar_calificacion_previa(1) == 1
    assert validar_calificacion_previa(50) == 50
    with pytest.raises(ValueError): validar_calificacion_previa(0)
    with pytest.raises(ValueError): validar_calificacion_previa(51)

def test_validar_orden_aplicacion():
    assert validar_orden_aplicacion(0) == 0
    assert validar_orden_aplicacion(9) == 9
    with pytest.raises(ValueError): validar_orden_aplicacion(-1)
    with pytest.raises(ValueError): validar_orden_aplicacion(10)

def test_validar_unidades():
    assert validar_unidades(0) == 0
    assert validar_unidades(50) == 50
    with pytest.raises(ValueError): validar_unidades(-1)
    with pytest.raises(ValueError): validar_unidades(51)
