'''
정수 2개를 입력받아 두 값중 최댓값을 출력하는 프로그램을 작성해보세요.
'''

a, b = map(int, input().split())

max_v = print(a if a > b else b)