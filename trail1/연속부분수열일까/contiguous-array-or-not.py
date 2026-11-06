'''
N1개의 원소로 이루어져 있는 수열 A의 정보와,
N2개의 원소로 이루어져 있는 수열 B의 정보가 주어졌을 때 수열 B가 수열 A의 연속부분수열인지를 판단하는 프로그램을 작성해보세요.
'''

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# b_list 길이만큼의 filter를 만들어서 비교함
ans = "No"
for i in range(a):
    if a_list[i:i+b] == b_list:
        ans = "Yes"

print(ans)