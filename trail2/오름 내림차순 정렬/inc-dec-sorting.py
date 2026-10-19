'''
n개의 정수가 주어졌을 때, 처음에는 오름차순으로 정렬하여 출력하고, 그 다음에는 내림차순으로 정렬하여 출력하는 프로그램을 작성해보세요.
'''

n = int(input())
nums = list(map(int, input().split()))

print(*sorted(nums))
print(*sorted(nums)[::-1])
