a, b, c = map(int, input().split())

if a <= b and a <= c:  # a가 최소
    print(a)
elif b <= a and b <= c: # b가 최소
    print(b)
elif c <= a and c <= b: # c가 최소
    print(c)