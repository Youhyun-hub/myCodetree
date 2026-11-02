'''
자연수 N을 입력받아 1부터 N까지 369 게임을 진행했을 때의 결과를 출력하는 프로그램을 작성해보세요. 369 게임에서는 수가 3의 배수이거나 수를 구성하는 숫자에 3, 6, 9 중 하나라도 들어가있는 경우에는 0을 출력하고,
그렇지 않다면 해당 수를 그대로 출력합니다.
'''

N = int(input())
arr = [str(i) for i in range(1, N+1)]

for x in arr:
    if (x.count('3') >= 1 or x.count('6') >= 1 or x.count('9') >= 1) or int(x) % 3 == 0:
        print(0, end=" ")
    else:
        print(x, end=" ")