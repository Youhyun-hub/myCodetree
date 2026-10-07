def avg_score(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    avg = round(total / len(arr), 1)
    
    return avg


arr = list(map(float, input().split()))
print(avg_score(arr))