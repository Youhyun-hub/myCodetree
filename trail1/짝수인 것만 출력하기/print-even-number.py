n = int(input())
nums = list(map(int, input().split()))

evens = []
for i in range(n):
    if nums[i] % 2 == 0:
        evens.append(nums[i])

print(*evens)
        