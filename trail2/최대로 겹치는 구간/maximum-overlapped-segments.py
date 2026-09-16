n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
arr = [0] * 201 # -100~100 (0포함)
for a, b in segments:
    for i in range(a, b):
        arr[i+100] += 1

print(max(arr))