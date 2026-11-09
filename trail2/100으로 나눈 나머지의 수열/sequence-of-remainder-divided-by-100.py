N = int(input())

def f(N):
    if N == 0:
        return 2
    
    if N == 1:
        return 4

    return (f(N-1) * f(N-2)) % 100  # 세번째 이후
        

print(f(N-1))  # 1번째부터 시작