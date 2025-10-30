# test_hola.py
from hola import mensaje

def test_mensaje_default():
    assert mensaje() == "Hola, DevOps Class 🚀"

def test_mensaje_nombre():
    assert mensaje("Mauricio") == "Hola, Mauricio 🚀"
