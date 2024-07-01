import pytest
from src.main import Calculator


@pytest.mark.POL_add
@pytest.mark.parametrize("arg1, arg2, res", [(1, 2, 3),
                                       (3.5, 3.5, 7),
                                       (5, -2, 3),
                                       (2, 3.5, 5.5)])

def test_addP(arg1, arg2, res):
    calc = Calculator()
    assert calc.add(arg1, arg2) == res




@pytest.mark.BOUN_add
@pytest.mark.parametrize("arg1, arg2, res", [(100000, 100000, 200000),
                                             (0, 0, 0)])

def test_addB(arg1, arg2, res):
    calc = Calculator()
    assert calc.add(arg1, arg2) == res




@pytest.mark.NEG_add
@pytest.mark.parametrize("arg1, arg2, res", [("a", "a", pytest.raises(TypeError))])

def test_addN(arg1, arg2, res):
    calc = Calculator()

    with res:
        assert calc.add(arg1, arg2) == res





@pytest.mark.POL_subtract
@pytest.mark.parametrize("arg1, arg2, res", [(2, 1, 1),
                                             (3.5, 0.5, 3),
                                             (5, -2, 7),
                                             (2.5, 2, 0.5)])

def test_subtractP(arg1, arg2, res):
    calc = Calculator()
    assert calc.subtract(arg1, arg2) == res



@pytest.mark.BOUN_subtract
@pytest.mark.parametrize("arg1, arg2, res", [(100000, 100000, 0),
                                             (0, 0, 0)])

def test_subtractB(arg1, arg2, res):
    calc = Calculator()
    assert calc.subtract(arg1, arg2) == res




@pytest.mark.NEG_subtract
@pytest.mark.parametrize("arg1, arg2, res", [("a", "a", pytest.raises(TypeError))])

def test_subtractN(arg1, arg2, res):
    calc = Calculator()

    with res:
        assert calc.subtract(arg1, arg2) == res



@pytest.mark.POL_multiply
@pytest.mark.parametrize("arg1, arg2, res", [(2, 1, 2),
                                             (3.5, 0.5, 1.75),
                                             (-5, 2, -10),
                                             (2.5, 2, 5)])

def test_multiplyP(arg1, arg2, res):
    calc = Calculator()
    assert calc.multiply(arg1, arg2) == res





@pytest.mark.BOUN_multiply
@pytest.mark.parametrize("arg1, arg2, res", [(100000, 100000, 10000000000),
                                             (0, 0, 0)])

def test_multiplyB(arg1, arg2, res):
    calc = Calculator()
    assert calc.multiply(arg1, arg2) == res



@pytest.mark.NEG_multiply
@pytest.mark.parametrize("arg1, arg2, res", [("a", "a", pytest.raises(TypeError))])

def test_multiplyN(arg1, arg2, res):
    calc = Calculator()

    with res:
        assert calc.multiply(arg1, arg2) == res




@pytest.mark.POL_divide
@pytest.mark.parametrize("arg1, arg2, res", [(2, 1, 2),
                                             (3.5, 0.5, 7),
                                             (-6, 2, -3),
                                             (6.5, 1, 6.5)])

def test_divideP(arg1, arg2, res):
    calc = Calculator()
    assert calc.divide(arg1, arg2) == res





@pytest.mark.BOUN_divide
@pytest.mark.parametrize("arg1, arg2, res", [(100000, 100000, 1)])

def test_divideB(arg1, arg2, res):
    calc = Calculator()
    assert calc.divide(arg1, arg2) == res



@pytest.mark.NEG_divide
@pytest.mark.parametrize("arg1, arg2, res", [("a", "a", pytest.raises(TypeError)),
                                             (0, 0, pytest.raises(ZeroDivisionError))])

def test_divideN(arg1, arg2, res):
    calc = Calculator()

    with res:
        assert calc.divide(arg1, arg2) == res