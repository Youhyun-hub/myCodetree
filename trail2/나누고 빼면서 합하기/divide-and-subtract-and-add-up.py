'''
N개의 원소로 이루어진 수열 A가 주어지고, 정수 M이 주어집니다.
처음 주어진 M에서 시작하여 M이 1이 될 때까지, M이 홀수면 1을 빼고 짝수면 2로 나누는 것을 반복합니다.
이 과정에서 거쳐 간 모든 M에 대하여 A의 M번째 원소를 더한 값을 출력하는 프로그램을 작성해보세요.
처음 주어진 M과 마지막 값인 1에 대한 원소도 모두 더합니다.
따라서 처음부터 M이 1이면 더 이상 반복하지 않고 A의 첫 번째 원소만 더한 값이 답이 됩니다.

단, 함수를 이용하여 문제를 해결해주세요.
'''

n, m = map(int, input().split()) # n - 원소 수, m - 변화 시작 수
A = list(map(int, input().split()))

# Please write your code here.
def get_one(m):
    num = [m]

    while m > 1:
        if m % 2 != 0:  # 홀수면
            m -= 1
        else:  # 짝수면
            m //= 2
        num.append(m)  # 4, 2, 1
    
    return num

def get_num(num):
    total = 0
    
    for x in num:  # 4, 2, 1
        total += A[x-1]

    return total


num = get_one(m)
print(get_num(num))
        
