from src.saludo import saludar

def test_saludar():
    assert saludar("Juan") == "Hola Juan"