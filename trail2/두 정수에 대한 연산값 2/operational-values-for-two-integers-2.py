def modify_num(a, b):
    bigger = max(a, b) * 2
    smaller = min(a, b) + 10

    if a < b:
        a = smaller
        b = bigger
    else:
        a = bigger
        b = smaller
    
    return a, b
        

a, b = map(int, input().split())
a, b = modify_num(a, b)
print(a, b)
