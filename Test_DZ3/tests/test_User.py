import pytest
from src.main import User


@pytest.mark.get_name
@pytest.mark.parametrize("name, age, res", [("f", None, "f"),
                                       (1, None,  1)])

def test_get_name(name, age, res):
    u = User(name, age)
    assert u.get_name() == res


@pytest.mark.get_age
@pytest.mark.parametrize("name, age, res", [(None, "r", "r"),
                                            (None, 2, 2)])
def test_get_age(name, age, res):
    u = User(name, age)
    assert u.get_age() == res


@pytest.mark.NEG_up_age
@pytest.mark.parametrize("name, age, res", [("f", "r", pytest.raises(TypeError))])

def test_up_ageN(name, age, res):
    u = User(name, age)

    with res:
        assert u.up_age() == res


@pytest.mark.POL_up_age
@pytest.mark.parametrize("name, age, res", [(None, 2, 3)])

def test_up_ageP(name, age, res):
    u = User(name, age)
    assert u.up_age() == 3
