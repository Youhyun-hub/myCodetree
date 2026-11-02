n, a = map(int, input().split())
s = 1
while s <= n:
    if s % a == 0:
        print(1)
    else:
        print(0)
    s += 1