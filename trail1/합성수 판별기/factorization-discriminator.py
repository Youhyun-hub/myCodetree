N = int(input())
ans = "N"

for i in range(2, N):
    if N % i == 0:
        ans = "C"

print(ans)