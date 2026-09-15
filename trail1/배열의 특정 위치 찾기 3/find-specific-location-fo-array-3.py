arr = list(map(int, input().split()))

total = 0
for i in range(len(arr)):
    if arr[i] == 0:
        if i <= 3:
            total = sum(arr[:i])
            break
        else:
            total = sum(arr[i-3:i])
            break
    
print(total)