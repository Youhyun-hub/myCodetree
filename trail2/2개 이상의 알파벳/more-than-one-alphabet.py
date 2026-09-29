def diff_chars(txt):
    pick = txt[0]
    cnt = 1  # 서로 다른 알파벳 수
    res = "No"
    for i in range(1, len(A)):
        if pick != A[i]:
            cnt += 1
            res = "Yes"
            break
    return res

A = input()
print(diff_chars(A))