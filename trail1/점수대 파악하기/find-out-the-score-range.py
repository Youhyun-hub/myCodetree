'''
100명 이하인 학생들의 점수가 주어지다가 0이 주어지면 그때까지 주어진 점수를 10점 단위로 구분하여 점수대별 학생 수를 출력하는 프로그램을 작성해보세요.
'''


arr = list(map(int, input().split()))
cnt = [0] * 11

for i in range(len(arr)):
    if arr[i] == 0:
        break
    cnt[arr[i] // 10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt[i]}")