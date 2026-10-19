'''
N개의 수가 주어졌을 때, 오름차순으로 정렬했을 때 K번째 수를 출력하는 프로그램을 작성해보세요.
'''

n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
print(sorted(nums)[k-1])