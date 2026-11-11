'''
단어가 N개 주어졌을 때, 문자열 T로 시작하는 단어들 중 사전순으로 정렬했을 때의 K번째 문자열을 출력하는 프로그램을 작성해보세요.
'''

n, k, t = input().split()  # n - 단어 개수, k - 문자열 번호, t - 시작 단어
n, k = int(n), int(k)
str = [input() for _ in range(n)]
str.sort()  # 사전 순 정렬

ans = []  # 조건 만족 리스트
for i in range(n):
    if t in str[i]:
        ans.append(str[i])

print(ans[2])