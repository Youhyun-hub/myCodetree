a, b, c = map(int, input().split())

def min_val(i, j, k):
    min_v = i
    if i > j:
        min_v = j
    elif i > k:
        min_v = k
    return min_v

print(min_val(a, b, c))