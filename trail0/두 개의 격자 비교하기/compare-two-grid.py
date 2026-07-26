n, m = map(int, input().split())

a_matrix = []
for _ in range(n):
    arr1 = list(map(int, input().split()))
    a_matrix.append(arr1)
# print(a_matrix)

b_matrix = []
for _ in range(n):
    arr2 = list(map(int, input().split()))
    b_matrix.append(arr2)
# print(b_matrix)

result = []
for i in range(n):
    for j in range(m):
        if a_matrix[i][j] == b_matrix[i][j]:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()