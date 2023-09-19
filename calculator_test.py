import calculator

def test_add_12():
    # Setup
    x = 5
    y = 7
    expected = "5 + 7 = 12"

    # Invoke
    result = calculator.add(x,y)

    # Analyze
    assert result == expected


def test_subtract_15():
    # Setup
    x = 2
    y = 17
    expected = "2 - 17 = -15"

    # Invoke
    result = calculator.subtract(x,y)

    # Analyze
    assert result == expected

def test_multiply_27():
    # Setup
    x = 3
    y = 9
    expected = "3 * 9 = 27"

    # Invoke
    result = calculator.multiply(x,y)

    # Analyze
    assert result == expected

def test_divide_2():
    # Setup
    x = 12
    y = 6
    expected = "12 / 6 = 2.0"

    # Invoke
    result = calculator.divide(x, y)

    # Analyze
    assert result == expected

def test_divide_NaN():
    # Setup
    x = 100
    y = 0
    expected = "100 / 0 = NaN"

    # Invoke
    result = calculator.divide(x, y)

    # Analyze
    assert result == expected

def test_exponent_1000():
    # Setup
    x = 10
    y = 3
    expected = "10^3 = 1000.0"

    # Invoke
    result = calculator.exponent(x, y)

    # Analyze
    assert result == expected