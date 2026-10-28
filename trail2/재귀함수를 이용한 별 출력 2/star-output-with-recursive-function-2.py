'''
정수 n을 입력받아 재귀함수를 이용해 다음 모양대로 별을 출력하는 프로그램을 작성해보세요.
첫 번째 줄부터 차례로 별을 n개, n−1개, …, 1개 출력한 뒤, 이어서 다시 1개, 2개, …, n개 출력합니다.
즉 별의 개수가 n개에서 1개까지 줄어들었다가 다시 n개까지 늘어나며, 모두 2n개의 줄을 출력하게 됩니다.
'''

n = int(input())

def counting_star(n):
    if n == 0:
        return
    
    print("* " * n)
    counting_star(n-1)
    print("* " * n)

counting_star(n)