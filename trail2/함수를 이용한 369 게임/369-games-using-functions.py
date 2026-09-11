a, b = map(int, input().split())

def mul_three(A, B):
    cnt = 0
    for i in range(A, B+1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            cnt += 1
        elif i % 3 == 0:
            cnt += 1
    return cnt

print(mul_three(a, b))