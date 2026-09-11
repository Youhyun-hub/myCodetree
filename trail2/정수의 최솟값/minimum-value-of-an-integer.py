a, b, c = map(int, input().split())

def min_val(i, j, k):
    min_v = 0
    if i < j and i < k:
        min_v = i
    elif i > j and j < k:
        min_v = j
    elif i > k and j > k:
        min_v = k
    return min_v

print(min_val(a, b, c))