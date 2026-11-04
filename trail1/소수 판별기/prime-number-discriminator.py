N = int(input())
ans = "P"

for i in range(2, N):
    if N % i == 0:
        ans = "C"
        break

print(ans)