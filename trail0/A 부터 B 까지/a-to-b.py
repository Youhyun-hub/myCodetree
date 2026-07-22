a, b = map(int, input().split())

result = [a] 

while True:
    if a % 2 == 1:
        a *= 2
    else:
        a += 3
        
    if a > b:
        break
        
    result.append(a)

print(*result)
