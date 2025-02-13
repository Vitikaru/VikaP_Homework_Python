import pytest
from string_utils import StringUtils

StringUtils = StringUtils


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("HELLO", "Hello"),
        ("hELLo", "Hello"),
        ("12345", "12345"),
        ("hello, world", "Hello, world"),
        ("hello, WORLD!", "Hello, world!"),
        ("", "")
    ]
)
def test_capitilize_positive_and_negative(input_text, expected_output):
    utils = StringUtils
    assert utils.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("    Hello", "Hello"),
        (" Hello, world!", "Hello, world!"),
        (" ", "")
    ]
)
def test_trim_positive_and_negative(input_text, expected_output):
    utils = StringUtils
    assert utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, delimeter, expected_output",
    [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("1-2-3-4", "-", ["1", "2", "3", "4"]),
        ("", "", [])
    ]
)
def test_to_list_positive_and_negative(input_text, delimeter, expected_output):
    utils = StringUtils
    assert utils.to_list(input_text, delimeter) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "U", False),
        ("Skyro", "a", False),
        ("Hello, world!", ",",  True),
        ("Hello, world!", ".", False),
        ("", "", True),
        ("123456789", "5", True),
        ("123456789", "0", False)
    ]
)
def test_contains_positive_and_negative(input_text, symbol, expected_output):
    utils = StringUtils
    assert utils.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("Hello, world!", ",", "Hello world!"),
        ("", "", ""),
        ("abcabc", "a", "bcbc"),
        ("   ", " ", "")
    ]
)
def test_delete_symbol_positive_and_negative(input_text, symbol,
                                             expected_output):
    utils = StringUtils
    assert utils.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "P", False),
        ("12345", "1", True),
        ("12345", "5", False),
        ("Hello, world!", "H", True),
        ("Hello, world!", "!", False),
        ("", "", True),
        ("", " ", False)
    ]
)
def test_starts_with_positive_and_negative(input_text, symbol,
                                           expected_output):
    utils = StringUtils
    assert utils.starts_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("SkyPro", "o", True),
        ("SkyPro", "y", False),
        ("12345", "5", True),
        ("12345", "0", False),
        ("Hello, world!", "!", True),
        ("Hello, world!", "H", False),
        ("", "", True),
        ("", " ", False)
    ]
)
def test_end_with_positive_and_negative(input_text, symbol, expected_output):
    utils = StringUtils
    assert utils.end_with(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", True),
        (" ", True),
        ("     ", True),
        ('SkyPro', False),
        ("12345", False),
        ("Hello, world!", False)
    ]
)
def test_is_empty_positive_and_negative(input_text, expected_output):
    utils = StringUtils
    assert utils.is_empty(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, joiner, expected_output",
    [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        (["Sky", "Pro"], "-", "Sky-Pro"),
        (["Hello", "world"], ", ", "Hello, world"),
        ([], "", "")
    ]
)
def test_list_to_string_positive_and_negative(input_text, joiner,
                                              expected_output):
    utils = StringUtils
    assert utils.list_to_string(input_text, joiner) == expected_output
