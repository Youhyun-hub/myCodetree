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