'''
N개의 정수가 주어졌을 때,
같은 정수가 연속하여 나오는 횟수 중 최댓값을 구하는 프로그램을 작성해보세요.
'''

n = int(input())
arr = [int(input()) for _ in range(n)]

max_v = 0

for i in range(n):
    cnt = 0

    for j in range(i, n):
        if arr[i] == arr[j]:
            cnt += 1
        else:
            break

    if max_v < cnt:
        max_v = cnt

print(max_v)

'''
[코드트리 풀이]
# 변수를 선언하고 입력을 받습니다.
n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

# 같은 정수가 연속하여 나오는 횟수를 구해보며,
# 그중 최댓값을 갱신합니다.
ans, cnt = 0, 0
for i in range(n):
    # Case 1
    if i >= 1 and arr[i] == arr[i - 1]:
        cnt += 1
    # Case 2
    else:
        cnt = 1

    ans = max(ans, cnt)

# 결과를 출력합니다.
print(ans)


'''