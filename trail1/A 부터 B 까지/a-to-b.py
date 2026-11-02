a, b = map(int, input().split())
ans = []
while a <= b:
    if a % 2 != 0:  #  홀수
        ans.append(a)
        a *= 2
    elif a % 2 == 0:           #  짝수
        ans.append(a)
        a += 3
print(*ans)