n, m = map(int, input().split())

# Please write your code here.
def one_matrix(i, j):
    for _ in range(i):
        for _ in range(j):
            print("1", end="")
        print()
one_matrix(n, m)