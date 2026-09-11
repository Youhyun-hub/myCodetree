a, b = map(int, input().split())

def is_on(n):
    cnt = 0
    if n % 2 != 0 and (n % 10) != 5 and (n % 3 != 0 or n % 9 == 0):
        return True
    else:
        return False
def cnt_on(A, B):
    cnt = 0
    for i in range(A, B+1):
        if is_on(i):
            cnt += 1
    return cnt

print(cnt_on(a, b)) 