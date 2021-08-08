import pytest
import actions as act
diccionarios=[
    {'nombre':'juan','edad':8},
    {'nombre':'toño','edad':10},
    {'nombre':'ana','edad':5},
    {'nombre':'sofia','edad':19},
    {'nombre':'erick','edad':22},
]
def test_act():
    assert act.ordenar() ==  "correcto"
    assert act.diccionario(diccionarios) == 2