n = int(input())

cnt = 0
for i in range(1, n+1):
    for _ in range(i):
        cnt += 1
        print(cnt, end = " ")
    print()


# for i in range(1, 2):  # 1, i+1
#     print(i)

# for i in range(2, 4):  # i+1, i+2
#     print(i, end = " ")
# print()

# for i in range(4, 7):  # i+2, i+3  # 4
#     print(i, end = " ")
# print()

# for i in range(7, 11):
#     print(i, end = " ")
# print()

# for i in range(11, 16):
#     print(i, end = " ")
# print()

# for i in range(16, 22):
#     print(i, end = " ")

# for i in range(22, 29):  # 7
#     print(i, end = " ")