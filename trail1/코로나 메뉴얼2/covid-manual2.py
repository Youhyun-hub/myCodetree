a = 0 
b = 0
c = 0
d = 0  # 증상별 분류


for _ in range(3):
    cold, temp = input().split()


    if cold == "Y":  # 유증상
        if int(temp) >= 37:  # 체온 이상
            a += 1
        else:  # 체온 정상
            c += 1
    else:  # 무증상
        if int(temp) >= 37:  # 체온 이상
            b += 1
        else:  # 체온 정상
            d += 1

print(a, b, c, d, end=" ")
if a >= 2:
    print("E")
