M, D = map(int, input().split())

def is_yes(m, d):
    # 월 비교 (m)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_d = 31
    elif m in [4, 6, 9, 11]:
        max_d = 30
    elif m == 2:
        max_d = 28
    else:
        return "No"
    # 일 비교 (d)
    if d <= max_d:
        return "Yes"
    else:
        return "No"
    

print(is_yes(M, D))