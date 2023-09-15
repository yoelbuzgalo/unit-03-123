import activities
import random

def test_squared_8():
    # setup
    x = 8
    expected = 64
    
    # invoke
    result = activities.squared(x)
    
    # analyze
    assert result == expected

def test_cubed_2():
    # setup
    x = 2
    expected = 8

    # invoke
    result = activities.cubed(x)
    
    #analyze
    assert result == expected

def test_even_40():
    # setup
    x = 40
    expected = "even"

    # invoke
    result = activities.even_or_odd(x)

    #analyze
    assert result == expected

def test_odd_25():
    # setup
    x = 25
    expected = "false"

    # invoke
    result = activities.even_or_odd(x)

    # analyze
    assert result == expected

def test_coin_toss_heads():
    # setup
    random.seed(1)
    expected = "heads"

    # invoke
    result = activities.coin_toss()

    # analyze
    assert result == expected