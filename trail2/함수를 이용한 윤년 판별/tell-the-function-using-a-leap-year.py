y = int(input())

def lun_year(n):
    if n % 4 == 0:
        return "true"
    else:
        return "false"

print(lun_year(y))