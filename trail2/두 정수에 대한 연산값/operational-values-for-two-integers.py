a, b = map(int, input().split())

def get_value(n, m):
    if n > m:
        n += 25
        m *= 2
    else:
        n *= 2
        m += 25
    print(n, m)

get_value(a, b)