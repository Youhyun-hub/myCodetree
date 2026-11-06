a, b = map(int, input().split())
ans = [a, b]

while len(ans) < 10:  # 10번째 항까지만
    ans.append(2 * ans[-2] + ans[-1])

print(*ans)