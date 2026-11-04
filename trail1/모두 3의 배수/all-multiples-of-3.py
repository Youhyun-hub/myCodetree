ans = 1

for i in range(5):
    n = int(input())

    if n % 3 != 0:
        ans = 0
        break

print(ans)