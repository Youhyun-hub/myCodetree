'''
2N개의 정수가 주어졌을 때, 겹치지 않으면서 2개의 원소가 하나의 그룹을 이루도록 하여 총 N개의 그룹을 만드려고 합니다.
적절하게 그룹을 만들어 각 그룹에 있는 원소의 합 중 최댓값이 최소가 되도록 하는 프로그램을 작성해보세요.
'''

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# 가장 큰 값과 가장 작은 값의 합 조합 중에 최대값 고르기 = 최대값이 최소
s = []   # 합의 조합
for i in range(n):
    s.append(nums[i] + nums[2*n-i-1])

print(max(s))
    
