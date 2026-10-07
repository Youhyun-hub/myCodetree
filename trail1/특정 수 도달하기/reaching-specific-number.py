arr = list(map(int, input().split()))


total =  0
for i in range(10):
    if arr[i] >= 250:
        idx = i
        break
        for j in range(i):
            total += arr[j]
    else:
        total += arr[i]
        idx = 10



print(total, f"{total/idx:.1f}")
    