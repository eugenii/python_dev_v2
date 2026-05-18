import pytest

from merge_sort_0 import merge


@pytest.mark.parametrize("left, right, expected", [
    ([2, 4, 7], [1, 3, 5], [1, 2, 3, 4, 5, 7]),
    ([], [1, 2], [1, 2]),
    ([1, 5], [2, 3, 6], [1, 2, 3, 5, 6]),
])
def test_merge(left, right, expected):
    """Проверка слияния двух сортированных списков"""
    assert merge(left, right) == expected


@pytest.mark.parametrize("invalid_left, invalid_right", [
    ([1, "два", 3], [4, 5]),  # строка вместо числа
    ([1, 2], [4, [5, 6]]),    # список вместо числа
    ([1, None], [3, 4]),      # None вместо числа
])
def test_merge_invalid_types(invalid_left, invalid_right):
    """Проверяем, что функция выбрасывает TypeError при неверных типах элементов."""
    with pytest.raises(TypeError):
        merge(invalid_left, invalid_right)