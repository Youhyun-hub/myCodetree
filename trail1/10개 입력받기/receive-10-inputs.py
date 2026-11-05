'''
정수 10개를 입력받아서 그 합과 평균을 출력하는데, 0이 입력되면 10개 입력이 끝나지 않았더라도 그때까지 입력된 합과 평균을 출력하는 프로그램을 작성해보세요.
0이 입력된 경우 0을 제외한 합과 평균을 구합니다. 단, 첫 입력으로는 0이 들어오지않는다고 생각해도 좋습니다.
'''

num = list(map(int, input().split()))

sum_v = 0
cnt = 0
for i in num:
    sum_v += i
    cnt += 1

    if i == 0:
        cnt -= 1
        break

print(sum_v, f"{sum_v/cnt:.1f}")
