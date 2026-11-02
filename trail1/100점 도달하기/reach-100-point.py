score = int(input())


for i in range(100-score+1):
    if score+i >= 90:
        print("A", end=" ")
    elif score+i >= 80:
        print("B", end=" ")
    elif score+i >= 70:
        print("C", end=" ")
    elif score+i >= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")