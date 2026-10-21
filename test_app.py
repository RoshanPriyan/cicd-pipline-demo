from app import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 3) == 6

def test_subtract():
    from app import subtract
    assert subtract(5, 3) == 2
    