Y, M, D = map(int, input().split())

def valid_date(y, m, d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_d = 31
    elif m in [4, 6, 9, 11]:
        max_d = 30
    elif m == 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            max_d = 29
        else:
            max_d = 28
    if max_d >= d:
        return True
    else:
        return False

def get_season(y, m, d):
    if valid_date(y, m, d):
        if 3<=m<=5:
            return "Spring"
        elif 6<=m<=8:
            return "Summer"
        elif 9<=m<=11:
            return "Fall"
        elif m in [12, 1, 2]:
            return "Winter"
    else:
        return -1

print(get_season(Y, M, D))