import pytest
from src.main import factorial


@pytest.mark.POL_factorial
@pytest.mark.parametrize("num, res", [(3, 6),
                                      (4, 24)])

def test_factorialP(num, res):
    assert factorial(num) == res



@pytest.mark.BOUN_factorial
@pytest.mark.parametrize("num, res", [(10, 3628800),
                                      (0, 1)])

def test_factorialB(num, res):
    assert factorial(num) == res



@pytest.mark.NEG_factorial
@pytest.mark.parametrize("num, res", [("2", pytest.raises(TypeError)),
                                      (3.5, pytest.raises(TypeError)),
                                      (-4, pytest.raises(ValueError))])

def test_factorialN(num, res):
    with res:
        assert factorial(num) == res



