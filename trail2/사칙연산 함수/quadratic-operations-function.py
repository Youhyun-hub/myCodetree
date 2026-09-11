a, o, c = input().split()
a = int(a)
c = int(c)

def get_cal(A, O, C):
    if O not in '+-/*':
        return False
    else:
        if O == "+":
            result = A + C
        elif O == "-":
            result = A - C
        elif O == "/":
            result = A // C
        else:
            result = A * C
    return f"{a} {o} {c} = {result}"

print(get_cal(a, o, c))