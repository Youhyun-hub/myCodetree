a, b, c = map(int, input().split()) # a - 날짜, b - 시, c - 분

# 24시간(하루) = 1,440분

if a <= 11 and b < 11:
    diff = -1
elif a >= 11 and b >= 11:  # 11일보다 크고 11시 11분 이후
    if c - 11 < 0:
        diff = 60 + c - 11 + ((b - 11 - 1) * 60) + ((a - 11) * 1440)
    else:
        diff = c - 11 + ((b - 11) * 60) + ((a - 11) * 1440)

print(diff)