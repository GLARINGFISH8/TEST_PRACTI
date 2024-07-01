import pytest
from src.main import is_palindrome


@pytest.mark.POL_is_palindrome
@pytest.mark.parametrize("string, res", [("АННА", True),
                                       ("Kara", False),
                                       ("ARA", True),
                                       ("1234567", False),
                                       ("1111111111", True),
                                       ("lsjfslkfjlfksjfj34ur3u987398y3n389", False),
                                       ("111ara111", True),
                                       ("+-*///", False),
                                       ("+++", True),
                                       ("slkjf09458+--//J***", False),
                                       ("111**ara**111", True)])

def test_is_palindromeP(string, res):
    assert is_palindrome(string) == res





@pytest.mark.BOUN_is_palindrome
@pytest.mark.parametrize("string, res", [("klsjffjslkjfslkjfjlfjslkfjsdlkfjsdkfjsdjfkljsdfjflksjffjalksfjlksjflksdfjsdf", False),
                                       ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", True),
                                       (" ", True)])

def test_is_palindromeB(string, res):
    assert is_palindrome(string) == res




@pytest.mark.NEG_is_palindrome
@pytest.mark.parametrize("string, res", [([1, 2, 3], pytest.raises(TypeError)),
                                       ({1, 2, 3}, pytest.raises(TypeError)),
                                       (1, pytest.raises(TypeError)),
                                       (2.3, pytest.raises(TypeError)),
                                       (True, pytest.raises(TypeError)),
                                       (False, pytest.raises(TypeError))])

def test_is_palindromeN(string, res):
    with res:
        assert is_palindrome(string) == res




