import pytest

from merge_sort_0 import merge_sort_0


@pytest.mark.parametrize("left, right, expected", [
    ([2, 4, 7], [1, 3, 5], [1, 2, 3, 4, 5, 7]),
    ([], [1, 2], [1, 2]),
    ([1, 5], [2, 3, 6], [1, 2, 3, 5, 6]),
])
def test_merge_sort(left, right, expected):
    """Проверка слияния двух сортированных списков"""
    assert merge_sort_0(left, right) == expected
