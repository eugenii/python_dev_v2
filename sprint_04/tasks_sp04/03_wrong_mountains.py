# Неправильные горы 
from array import array
import sys



def valid_mountain_array(data: array) -> bool:
    valid = False
    if not data:
        return valid
    if len(data) < 3:
        return valid
    if data[0] > data[1]:
        return False
    pos = 1

    while pos < len(data) - 1:
        if data[pos] < data[pos + 1]:
            pos += 1
            continue
        elif data[pos] == data[pos + 1]:
            return valid
        else:
            valid = True
            pos +=1 
            break
    else:
        return valid
    while pos < len(data) - 1:
        if data[pos] <= data[pos + 1]:
            return False
        pos += 1
        continue

    return valid

     
data = array( 'b', map(int, sys.stdin.read().split()))

print(valid_mountain_array(data))