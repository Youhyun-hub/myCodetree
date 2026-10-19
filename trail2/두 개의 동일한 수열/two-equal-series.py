'''
n개의 원소로 이루어진 수열 A와 n개의 원소로 이루어진 수열 B가 주어졌을 때, 두 수열이 순서에 관계없이 서로 같은 원소들로 이루어져 있는지를 판단하는 프로그램을 작성해보세요.

예를 들어 수열 A=[1,2,3], 수열 B=[3,1,2]라면 순서만 다르고 같은 원소로 이루어져 있지만, 수열 A=[1,2,5], 수열 B=[3,1,2]라면 같은 원소로 이루어져 있지 않습니다.
'''

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    if sorted(A)[i] != sorted(B)[i]:
        ans = 'No'
        break
    else:
        ans = 'Yes'

print(ans)