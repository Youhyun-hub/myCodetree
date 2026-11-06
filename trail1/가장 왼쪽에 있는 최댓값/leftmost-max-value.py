'''
N개의 정수가 주어졌을 때, 주어진 정수들 중 최댓값의 위치를 출력합니다. 만약 최댓값이 여러 개라면, 가장 왼쪽에 있는 최댓값의 위치를 출력합니다.

그 이후에는 위에서 구한 최댓값의 위치보다 더 왼쪽에 있는 정수들 중 최댓값을 구해 그 위치를 출력합니다. 이 경우에도 최댓값이 여러 개라면, 가장 왼쪽에 있는 최댓값의 위치를 출력합니다.

위의 과정을 끊임없이 반복하며, 최종적으로 첫 번째 원소가 뽑히게 되면 이 과정을 종료합니다. 이러한 과정을 거쳐 구해진 최댓값의 위치들을 출력하는 프로그램을 작성해보세요.
'''

n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_idx = 0
while True:
    for i in range(n):
        if a[i] == max(a):
            max_idx = i
            a = a[:max_idx]
            break
    print(max_idx+1, end=" ")
    if max_idx == 0:
        break
 

