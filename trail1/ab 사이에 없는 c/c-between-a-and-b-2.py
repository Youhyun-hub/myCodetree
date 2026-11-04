a, b, c = map(int, input().split())

for i in range(a, b+1):
    if i % c != 0:  # 배수가 없으면
        ans = "YES"
    else:
        ans = "NO"
        break
print(ans)