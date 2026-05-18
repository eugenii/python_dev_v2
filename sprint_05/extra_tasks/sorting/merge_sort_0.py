# Merge sort level 0

def merge_sort_0(left: list[int], right: list[int]) -> list[int]:

    left_len = len(left)
    right_len = len(right)

    res = []
    try:
        if right_len == 0:
            return left
        if left_len == 0:
            return left
        min_range = min(left_len, right_len)
        for i in range(min_range):
            if left[i] < right[i]:
                res.append(left[i])
            else:
                res.append(right[i])
        if right_len > left_len:
            res.append(right[right_len:])
        if left_len > right_len:
            res.append(left[right_len:])
    except TypeError:
        pass
    return res


print(merge_sort_0([1, [], 2, 3], [4, 5, 6]))