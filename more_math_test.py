import more_math
import math

def test_fact_5():
    # Setup
    x = 5
    expected = 120

    # Invoke
    result = more_math.fact(x)

    # Analyze
    assert result == expected

def test_root_4():
    # Setup
    x = 4.0
    expected = 2.0

    # Invoke
    result = more_math.root(x)

    # Analyze
    assert math.isclose(result, expected)

def test_trunk_2():
    # Setup
    x = 2.0
    expected = 2

    # Invoke
    result = more_math.trunk(x)

    # Analyze
    assert result == expected