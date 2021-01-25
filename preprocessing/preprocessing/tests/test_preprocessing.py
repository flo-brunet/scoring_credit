from preprocessing.core import is_rich, get_notation


def test_notation_in_abc():

    abc = ['A', 'B', 'C']

    assert get_notation(1) in abc
    assert get_notation(0.5) in abc
    assert get_notation(0.1) in abc

def test_is_rich():

    assert is_rich(0) == False
    assert is_rich(10000000) == True
