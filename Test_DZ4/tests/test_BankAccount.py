import pytest
from src.main import BankAccount




@pytest.mark.POL_deposit
@pytest.mark.parametrize("val, returns, res", [(30.5, None, 30.5),
                                               (30, None, 30),
                                               (50, None, 50),
                                               (50.5, None, 50.5)])


def test_depositP(val, returns, res):
    b = BankAccount()
    assert b.deposit(val) == returns
    assert b.balance == res




@pytest.mark.BOUN_deposit
@pytest.mark.parametrize("val, returns, res", [(123456789123456, None, 123456789123456)])

def test_deposit(val, returns, res):
    b = BankAccount()
    assert b.deposit(val) == returns
    assert b.balance == res



@pytest.mark.NEG_deposit
@pytest.mark.parametrize("val, returns", [("FJK", pytest.raises(TypeError)),
                                          (-50, pytest.raises(ValueError)),
                                          (-50.5, pytest.raises(ValueError)),
                                          (0, pytest.raises(ValueError)),
                                          (None, pytest.raises(TypeError))])

def test_deposit_N(val, returns):
    b = BankAccount()
    with returns:
        assert b.deposit(val) == returns




@pytest.mark.POL_withdraw
@pytest.mark.parametrize("val, returns, res", [(30, None, 70),
                                               (30.5, None, 69.5),
                                               (10, None, 90),
                                               (10.5, None, 89.5),])

def test_withdrawP(val, returns, res):
    b = BankAccount()
    b.deposit(100)
    assert b.withdraw(val) == returns
    assert b.balance == res



@pytest.mark.BOUN_withdraw
@pytest.mark.parametrize("val, returns, res", [(0, None, 100)])

def test_withdrawB(val, returns, res):
    b = BankAccount()
    b.deposit(100)
    assert b.withdraw(val) == returns
    assert b.balance == res


#Error?
@pytest.mark.NEG_withdraw
@pytest.mark.parametrize("val, returns", [("FJK", pytest.raises(TypeError)),
                                               (-10, pytest.raises(ValueError)),
                                               (-10.5, pytest.raises(ValueError)),
                                               (123456789123456, pytest.raises(ValueError)),
                                               (None, pytest.raises(ValueError))])

def test_withdrawN(val, returns):
    b = BankAccount()
    b.deposit(100)
    with returns:
        assert b.withdraw(val) == returns