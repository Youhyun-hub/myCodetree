nums = list(map(int, input().split()))

odds = 0
evens = 0
for i in range(len(nums)):
    if i % 2 == 0:
        odds += nums[i]
    else:
        evens += nums[i]

print(abs(odds - evens))