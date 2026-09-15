arr = list(map(int, input().split()))

s = 0
v = []
a = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        s += arr[i]

    elif (i + 1) % 3 == 0:
        v.append(i)
        for j in v:
            a += arr[j]
            a = a / len(v)

print(s, a)    