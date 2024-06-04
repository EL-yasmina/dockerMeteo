from app.controllers.math import inc, minus, power

def test_inc():
    assert inc(3) == 4
def test_minus():
    assert minus(3) == 2   
#print(inc(3)+minus(1)+power(1,2))