h, w = map(int, input().split())

b = int(w // (h/100) ** 2)

if b >= 25:
    print(b, "Obesity", sep="\n")
else:
    print(b)