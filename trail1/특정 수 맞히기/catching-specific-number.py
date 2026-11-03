while True:
    n = int(input())
    if n < 25:
        print("Higher")
    elif n > 25:
        print("Lower")
    else:  # 25일 떄
        print("Good")
        break