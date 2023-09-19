import calculator

def test_add_4():
    # Setup
    x = 5
    y = 7
    expected = "5 + 7 = 12"

    # Invoke
    result = calculator.add(x,y)

    # Analyze
    assert result == expected


def test_subtract_20():
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