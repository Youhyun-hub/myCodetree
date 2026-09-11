n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_part(n, m, A, B):
    for i in range(n):
        if A[i:i+m] == B:
            return "Yes"
    return "No"

print(is_part(n1, n2, a, b))
