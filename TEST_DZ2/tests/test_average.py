import pytest
from src.main import average


@pytest.mark.POL_average
@pytest.mark.parametrize("lst, res", [([1, 2, 3], 2),
                                      ([1, 2, 3], 2),
                                      ([1.5, 1.5], 1.5),
                                      ([1.5, 1.5, 3], 2)])

def test_averageBOUN(lst, res):
    assert average(lst) == res


@pytest.mark.BOUN_average
@pytest.mark.parametrize("lst, res", [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5)])

def test_averageB(lst, res):
    assert average(lst) == res




@pytest.mark.NEG_average
@pytest.mark.parametrize("lst, res", [({1, 2, 3}, pytest.raises(TypeError)),
                                      ((1, 2, 3), pytest.raises(TypeError)),
                                      ([], pytest.raises(ValueError))])
def test_averageN(lst, res):
    with res:
        assert average(lst) == res




