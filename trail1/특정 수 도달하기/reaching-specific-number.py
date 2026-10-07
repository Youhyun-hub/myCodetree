arr = list(map(int, input().split()))
tmp = sorted(arr)

for i in range(10):
    if arr[i] >= 250:
        idx = i
        break
        
total =  0
for j in range(i):
    total += arr[j]

print(total, f"{total/idx:.1f}")
    