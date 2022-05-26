import pytest
from code_challenges.roman_numerals import total_roman_numeral

def test_one():
    num = 'I'
    actual = total_roman_numeral(num)
    expected = 1
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_two():
    num = 'II'
    actual = total_roman_numeral(num)
    expected = 2
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_four():
    num = 'IV'
    actual = total_roman_numeral(num)
    expected = 4
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_seven():
    num = 'VII'
    actual = total_roman_numeral(num)
    expected = 7
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_ten():
    num = 'X'
    actual = total_roman_numeral(num)
    expected = 10
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_40():
    num = 'XL'
    actual = total_roman_numeral(num)
    expected = 40
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_70():
    num = 'LXX'
    actual = total_roman_numeral(num)
    expected = 70
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_150():
    num = 'CXLX'
    actual = total_roman_numeral(num)
    expected = 150
    assert actual == expected