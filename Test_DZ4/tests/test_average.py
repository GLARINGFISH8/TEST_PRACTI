import pytest
from src.main import average

@pytest.mark.POL_average
@pytest.mark.parametrize("list, res", [([1, 2, 3, 4, 5], 3),
                                       ([1, 2, 3], 2),
                                       ([2.5, 2.5, 2.5, 2.5], 2.5),
                                       ([3.5, 2.5, 4], 3.33),
                                       ([-1, -2, -3], -2),
                                       ([-2.5, -2.5, -2.5, -2.5], -2.5),
                                       ([-3.5, -2.5, -4], -3.33)])

def test_averageP(list, res):
    assert average(list) == res



@pytest.mark.BOUN_average
@pytest.mark.parametrize("list, res", [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123, 234, 365, 567], 96)])

def test_averageB(list, res):
    assert average(list) == res



@pytest.mark.NEG_average
@pytest.mark.parametrize("list, res", [((1, 2, 3, 4, 5), pytest.raises(TypeError)),
                                       ({1, 2, 3, 4, 5}, pytest.raises(TypeError)),
                                       ("12345", pytest.raises(TypeError)),
                                       (1, pytest.raises(TypeError)),
                                       (3.4, pytest.raises(TypeError)),
                                       (True, pytest.raises(TypeError)),
                                       (False, pytest.raises(TypeError)),
                                       ([], pytest.raises(ValueError)),
                                       (["a", "f"], pytest.raises(TypeError)),
                                       (["a", "f", 1], pytest.raises(TypeError)),
                                       ([True, True, True], pytest.raises(TypeError)),
                                       ([False, False, False], pytest.raises(TypeError))])

def test_averageN(list, res):
    with res:
        assert average(list) == list