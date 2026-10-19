'''
소문자 알파벳으로만 이루어져 있는 단어가 n개 주어졌을 때, 사전순으로 앞선 단어가 더 먼저 나오도록 정렬하여 출력하는 프로그램을 작성해보세요.
'''

n = int(input())
word = [input() for _ in range(n)]

for word in sorted(word):
    print(word)