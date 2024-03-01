import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, -1) == 0
