n, m = map(int, input().split())

# Please write your code here.
def max_gong(N, M):
    if M == 0:
        return N
    return max_gong(M, N % M)           

print(max_gong(n, m))