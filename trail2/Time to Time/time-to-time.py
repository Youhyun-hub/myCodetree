'''
2011년 11월 11일 A시 B분에서 시작하여 같은 날 C시 D분이 될 때까지 몇 분이 걸리는지를 계산하는 프로그램을 작성해보세요.
'''

a, b, c, d = map(int, input().split())

if d- b < 0:
    diff = 60 + d - b + ((c - a - 1) * 60)
else:
    diff = d - b + ((c - a) * 60)

print(diff)