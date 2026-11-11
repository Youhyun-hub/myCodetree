'''
N개의 정수가 주어졌을 때, 순서대로 정수를 읽다가 홀수 번째의 원소가 주어질 때마다 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성해보세요.
여기서 중앙값이란, 어떤 주어진 값들을 오름차순으로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
'''

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if i % 2 == 0:  # 홀수 번째 원소
        mid = sorted(arr[:i+1])
        print(mid[len(mid)//2], end=" ")