import pytest

from reverse_string import reverse_string


@pytest.mark.parametrize("input_str, expected", [
    ['hello', 'olleh',],
    ("a", "a"),
    ("", ""),
    ("python", "nohtyp"),
    ['1234', '4321']
    ])
def test_reverse_string(input_str, expected):
    """Тестируем рекурсивный разворот строки на разных кейсах."""
    assert reverse_string(input_str) == expected


# используем контекстный менеджер pytest.raises для проверки того, 
# что функция правильно генерирует ошибку при неверных типах данных 
# (число, список, словарь)
@pytest.mark.parametrize("invalid_input", [
    12345,        # число
    ['h', 'e'],   # список
    {'key': 'val'} # словарь
])
def test_reverse_string_exceptions(invalid_input):
    """Проверяем, что функция выбрасывает TypeError на некорректные типы."""
    with pytest.raises(TypeError):
        reverse_string(invalid_input)