a_matrix = []
b_matrix = []

for _ in range(3):
    a = list(map(int, input().split()))
    a_matrix.append(a)
# print(a_matrix)

input()

for _ in range(3):
    b = list(map(int, input().split()))
    b_matrix.append(b)
# print(b_matrix)

for i in range(3):
    for j in range(3):
        result = a_matrix[i][j] * b_matrix[i][j]
        print(result, end = " ")
    print()


# a = [x for x in map(int, input().split())]
# input()
# b = [y for y in map(int, input().split())]

# for x in a:
#     for y in b:
#         result = a * b
# print(result)