import pytest
from animals.tiger import roar

def test_tiger_roar():
    res = roar()
    assert res == 0
