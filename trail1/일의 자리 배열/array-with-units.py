a, b = map(int, input().split())

output = [a, b, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, 10):
    output[i] = (output[i-1] + output[i-2]) % 10
print(*output)