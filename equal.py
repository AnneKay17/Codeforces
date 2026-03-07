from collections import Counter

def lessOrEqual():
    values = list(map(int, input().split()))
    n = values[0]
    k = values[1]
    seq = list(map(int, input().split()))
    seq.sort()
    numbers = Counter(seq)
    if k > n:
        return -1
    if k == 0:
        if seq[0] >1:
            return 1

    sum = 0
    for key, value in numbers.items():
        sum +=value
        if sum == k:
            return key
        elif sum > k:
            return -1
    
print(lessOrEqual())




