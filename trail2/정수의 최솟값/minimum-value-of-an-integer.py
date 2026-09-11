a, b, c = map(int, input().split())

def min_val(i, j, k):
    min_v = i
    if j < min_v:
        min_v = j
    if k < min_v:
        min_v = k
    return min_v

print(min_val(a, b, c))