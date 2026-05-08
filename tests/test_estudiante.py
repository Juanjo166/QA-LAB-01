from src.estudiante import verificar_aprobacion


def test_estudiante_aprobado():
    assert verificar_aprobacion(11) == "aprobado"


def test_estudiante_aprobado_con_nota_mayor():
    assert verificar_aprobacion(15) == "aprobado"


def test_estudiante_desaprobado():
    assert verificar_aprobacion(10) == "desaprobado"


def test_estudiante_desaprobado_con_nota_baja():
    assert verificar_aprobacion(11) == "desaprobado"