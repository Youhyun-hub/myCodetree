n = int(input())

for i in range(1, n+1):
    for j in range(i+(i-1)):
        print("*", end="")
    print()

# for i in range(3):
#     print("*", end="")
# print()

# for i in range(5):
#     print("*", end="")
# print()