'''
1번째 줄부터 N번째 줄까지, i번째 줄에 별 문자 *를 정확히 i개씩 출력하는 프로그램을 작성해보세요.
단, 재귀함수를 이용해 출력해주세요.
'''

n = int(input())

def print_star(n):
    if n == 0:
        return
    
    print_star(n-1)
    print("*" * n, end = "")
    print()
    

print_star(n)