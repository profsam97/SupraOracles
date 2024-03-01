import calculator

def test_add():
    # custom error message
    result1 = calculator.add(2, 3)
    assert result1 == 5, f"Expected result of 2 + 3 to be 5, but got {result1}"
    result = calculator.add(2,5)
    assert result == 5, f"Expected result of 2 + 5 to be 7, but got {result}"


def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, -1) == 0
