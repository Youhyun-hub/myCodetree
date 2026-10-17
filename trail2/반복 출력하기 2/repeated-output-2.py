'''
정수 N이 주어지면 재귀함수를 이용해서 문자열 "HelloWorld"를 N번 출력하는 프로그램을 작성해보세요.
'''

n = int(input())

def print_helloworld(n):
    if n == 0:
        return  # 종료 조건
    print_helloworld(n-1)
    print("HelloWorld")

print_helloworld(n)