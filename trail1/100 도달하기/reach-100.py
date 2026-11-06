N = int(input())
s = 1

total = [s, N]
while True:
    total.append(total[-1] + total[-2])
    if total[-1] + total[-2] >= 100:
        total.append(total[-1] + total[-2])
        break
print(*total)