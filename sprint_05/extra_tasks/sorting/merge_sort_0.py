# Merge sort level 0

def merge(left: list[int], right: list[int]) -> list[int]:

    if not all(isinstance(x, int) for x in left) or not all(isinstance(x, int) for x in right):
        raise TypeError("Списки содержат элементы несовместимых типов!")

    left_idx = 0
    right_idx = 0
    res = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1

    res += left[left_idx:] + right[right_idx:]
 
    return res

