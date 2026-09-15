h, w = map(int, input().split())

b = round(w // (h / 100)** 2)

if b >= 25:
    print(f"{b}", "Obesity", sep="\n")
else:
    print(f"{b}")