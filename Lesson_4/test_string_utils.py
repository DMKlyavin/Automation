import pytest

from string_utils import StringUtils

string_util = StringUtils()
# Test Case 1: Тестирование функциональности "capitalize"


@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    ("denis", "Denis"),
    ("denIs", "Denis"),
    ("klyavin Denis", "Klyavin denis"),
    ("de'nis", "De'nis"),
    ("denis1", "Denis1"),
    ("denis-1", "Denis-1"),
    # Негативные проверки:
    ("", ""),
    ("Denis", "Denis"),
    ("MEGA", "Mega"),
    ("123qwerty", "123qwerty"),
    ("  white widow", "  white widow"),
    ("white widow  ", "White widow  ")
])
def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 2: Тестирование функциональности "trim"


@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    (" qwerty", "qwerty"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),
    (" Denis", "Denis"),
    ("   Denis123", "Denis123"),
    # Негативные проверки:
    ("", ""),
    ("denis klyavin", "denis klyavin"),
    ("mega", "mega"),
    ("123  ", "123  ")

])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 3: Тестирование функциональности "to_list"


@pytest.mark.parametrize('string, divider, result', [
    # Позитивные проверки:
    ("cat,dog,kittens,puppies", ",", ["cat", "dog", "kittens", "puppies"]),
    ("one1,two2,three3", ",", ["one1", "two2", "three3"]),
    ("cat;dog;kittens;puppies", ";", ["cat", "dog", "kittens", "puppies"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("!|@|#|$|%|^|&|*", "|", ["!", "@", "#", "$", "%", "^", "&", "*"]),
    ("1/q2/q3/q4/q5", "/q", ["1", "2", "3", "4", "5"]),
    # Негативные проверки:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ("cat,dog,kittens puppies", None, ["cat", "dog", "kittens puppies"]),
])
def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")

    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)

    print(f"Actual result: {res}")

    assert res == result

# Test Case 4: Тестирование функциональности "contains"


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("denis", "d", True),
    (" test", "t", True),
    ("macos  ", "s", True),
    ("denis-klyavin", "-", True),
    ("1234", "1", True),
    ("MEGA", "A", True),
    ("", "", True),
    # Негативные проверки:
    ("home", "w", False),
    ("world", "P", False),
    ("hello", "w", False),
    ("hello", "!", False),
    ("", "q", False),
    ("hello", "privet", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 5: Тестирование функциональности "delete_symbol"


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("script", "t", "scrip"),
    ("Monday", "y", "Monda"),
    ("Tuesday", "T", "uesday"),
    ("12345678", "1", "2345678"),
    ("monday-tuesday", "-", "mondaytuesday"),
    ("Yandex", "dex", "Yan"),
    # Негативные проверки:
    ("denis", "q", "denis"),
    ("", "", ""),
    ("", "q", ""),
    ("cofe", "", "cofe"),
    ("cinnamon  ", "n", "ciamo  ")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

# Test Case 6: Тестирование функциональности "starts_with"


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("test", "t", True),
    ("", "", True),
    ("Denis", "D", True),
    (" Klyavin", "", True),
    ("Skypro  ", "S", True),
    ("Film", "F", True),
    ("Skyeng+Skypro", "S", True),
    ("123", "1", True),
    # Негативные проверки:
    ("Denis", "d", False),
    ("skypro", "S", False),
    ("", "q", False),
    ("Test", "t", False),
    ("one", "e", False),
    ("two", "w", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

# Test Case 7: Тестирование функциональности "end_with"


@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("denis", "s", True),
    ("Klyavin", "n", True),
    ("", "", True),
    ("qwe ", "", True),
    ("123", "3", True),
    ("Sky-pro", "o", True),
    ("Sky pro", "o", True),
    ("QA50", "0", True),
    ("test", "", True),
    # Негативные проверки:
    ("one", "P", False),
    ("morning", "P", False),
    ("World", "Q", False),
    ("", "a", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

# Test Case 8: Тестирование функциональности "is_empty"


@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    ("", True),
    (" ", True),
    ("  ", True),
    # Негативные проверки:
    ("dog", False),
    (" cat", False),
    ("123", False),
    ("world ", False)
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

# Test Case 9: Тестирование функциональности "list_to_string"


@pytest.mark.parametrize('lst, joiner, result', [
    # Позитивные проверки:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Sky", "pro"], "", "Skypro"),
    (["Denis", "Klyavin"], "-", "Denis-Klyavin"),
    # Негативные проверки:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result
