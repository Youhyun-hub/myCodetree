binary = list(map(int, input()))
num = 0  # 십진수 결과

for i in range(len(binary)):
    num = num * 2 + binary[i]

'''
11101

i = 0: 0 * 2 + 1 = 1
i = 1: 1 * 2 + 1 = 3
i = 2: 3 * 2 + 1 = 7
i = 3: 7 * 2 + 0 = 14
i = 4: 14 * 2 + 1 = 29
'''

print(num)