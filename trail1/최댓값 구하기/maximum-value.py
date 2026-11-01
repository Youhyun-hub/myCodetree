a, b, c = map(int, input().split())

if a > b and a > c:  # a 최대
    print(a)
elif b > a and b > c:  # b 최대
    print(b)
else:
    print(c)