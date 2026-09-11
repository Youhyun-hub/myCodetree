a, b = map(int, input().split())

def mul_three(A, B):
    cnt = 0
    for i in range(A, B+1):
        if (i//10) == 3 or (i//10) == 6 or (i//10) == 9 or (i%10) == 3 or (i%10) == 6 or (i%10) == 9 or i % 3 == 0:
            cnt += 1
    return cnt

print(mul_three(a, b))