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