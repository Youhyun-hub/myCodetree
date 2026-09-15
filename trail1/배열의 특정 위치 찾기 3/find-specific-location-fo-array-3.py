arr = list(map(int, input().split()))

total = 0
for i in range(3, len(arr)):
    if arr[i] == 0:
        total = sum(arr[i-3:i])
        break
    
print(total)