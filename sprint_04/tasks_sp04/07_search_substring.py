# Поик подстроки в строке

def search(line: str) -> int:
    if line == '':
        return 0
    
    left_idx = 0
    right_idx = 1
    # res = line[left_idx]
    max_len = 0

    while right_idx < len(line):
        if line[left_idx] == line[right_idx]:
            max_len = max(max_len, right_idx - left_idx)
            left_idx += 1
            right_idx = left_idx + 1
            continue
        right_idx += 1

    return max(max_len, right_idx - left_idx)


print(search('cbbb'))
        
            


