import pytest
from src.main import Array


@pytest.mark.POL_sum
@pytest.mark.parametrize("list, res", [([1, 2, 3], 6),
                                       ([-1, -2, -3], -6),
                                       ([1, -2, 3], 2)])

def test_sumP(list, res):
    ar = Array(list)
    assert ar.sum() == res


@pytest.mark.BOUN_sum
@pytest.mark.parametrize("list, res", [([], 0),
                                       ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55)])
def test_sumB(list, res):
    ar = Array(list)
    assert ar.sum() == res



@pytest.mark.NEG_sum
@pytest.mark.parametrize("list, res", [({1, 2, 3}, pytest.raises(TypeError)),
                                       ((1, 2, 3), pytest.raises(TypeError))])
def test_sumN(list, res):
    ar = Array(list)

    with res:
        assert ar.sum() == res






@pytest.mark.POL_multiplys
@pytest.mark.parametrize("list, res", [([1, 2, 3], 6),
                                       ([-1, -2, -3], -6),
                                       ([1, -2, 3], -6)])

def test_multiplysP(list, res):
    ar = Array(list)
    assert ar.multiplys() == res





@pytest.mark.BOUN_multiplys
@pytest.mark.parametrize("list, res", [([], 0),
                                       ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3628800)])

def test_multiplysB(list, res):
    ar = Array(list)
    assert ar.multiplys() == res



@pytest.mark.NEG_multiplys
@pytest.mark.parametrize("list, res", [({1, 2, 3}, pytest.raises(TypeError)),
                                       ((1, 2, 3), pytest.raises(TypeError))])
def test_multiplysN(list, res):
    ar = Array(list)

    with res:
        assert ar.multiplys() == res





@pytest.mark.POL_averages
@pytest.mark.parametrize("list, res", [([1, 2, 3], 2),
                                       ([1, 2, 3, 4, 5, 6, 7, 8 ,9, 10], 5.5),
                                       ([-1, -2, -3], -2),
                                       ([1, -2, 3], 0.6666666666666666)])

def test_averagesP(list, res):
    ar = Array(list)
    assert ar.averages() == res



@pytest.mark.BOUN_averages
@pytest.mark.parametrize("list, res", [([1, 2, 3, 4, 5, 6, 7, 8 ,9, 10], 5.5)])

def test_averagesB(list, res):
    ar = Array(list)
    assert ar.averages() == res



@pytest.mark.NEG_averages
@pytest.mark.parametrize("list, res", [({1, 2, 3}, pytest.raises(TypeError)),
                                       ((1, 2, 3), pytest.raises(TypeError))])
def test_multiplysN(list, res):
    ar = Array(list)

    with res:
        assert ar.averages() == res
