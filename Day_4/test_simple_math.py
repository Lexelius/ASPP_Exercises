import numpy as np
import simple_math as sm
import pytest


@pytest.mark.parametrize("n, m, expected", [(1, 1, 2), (3, 2, 5)])
def test_simple_add(n, m, expected):
    assert sm.simple_add(n, m) == expected
    assert sm.simple_add(n, m) == sm.simple_add(m, n)


def test_simple_sub():
    assert sm.simple_sub(1, 3) == -2
    assert sm.simple_sub(1, -3) == 4


@pytest.mark.parametrize("n, m, expected", [(0, 123, 0), (-3, -2, 6), (5, -3, -15)])
def test_simple_mult(n, m, expected):
    assert sm.simple_mult(n, m) == expected


@pytest.mark.parametrize("n, m, expected", [(0, 123, 0), (7, -2, np.divide(7, -2))])
def test_simple_div(n, m, expected):
    assert sm.simple_div(n, m) == expected


@pytest.mark.parametrize("x, n0, n1, expected", [
    (np.arange(-2, 3), 5, 2, np.array([1, 3, 5, 7, 9])),
    (np.arange(-2, 3), -3, 4, np.array([-11, -7, -3, 1, 5]))
])
def test_poly_first(x, n0, n1, expected):
    assert (sm.poly_first(x, n0, n1) == expected).all()
    assert (sm.poly_first(x, n0, -n1) == sm.poly_first(x, n0, n1)[::-1]).all()


@pytest.mark.parametrize("x, n0, n1, n2, expected", [
    (np.arange(-2, 3), 5, 2, 2, np.array([1+(2*4), 3+(2*1), 5+(2*0), 7+(2*1), 9+(2*4)]))
])
def test_poly_second(x, n0, n1, n2, expected):
    assert (sm.poly_second(x, n0, n1, n2) == expected).all()


#%% Extra: testing out other ways to set up tests

###########################################################################################
@pytest.fixture
def addfix1():
    n, m = np.random.random(2)
    expected = sum((n, m))
    return n, m, expected

def test_simple_addfix(addfix1):
    n, m, expected = addfix1
    assert sm.simple_add(n, m) == expected
    assert sm.simple_add(n, m) == sm.simple_add(m, n)


###########################################################################################
@pytest.fixture(params=[(20, 30), (-3, 7)])
def addfix2(request):
    a, b = request.param
    print(f'a={a}, type(a)={type(a)},    b={b}, type(b)={type(b)}')
    expected = sum((a, b))
    return a, b, expected

def test_simple_addfix2(addfix2):
    n, m, expected = addfix2
    assert sm.simple_add(n, m) == expected
    assert sm.simple_add(n, m) == sm.simple_add(m, n)


