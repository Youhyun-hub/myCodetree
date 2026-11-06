'''
세자리 미만의 정수가 주어지다가 0이 주어지면 그 0을 제외하고 그 때까지 입력된 정수의 숫자들의 십의 자리 숫자가 각각 몇 개인지 작은 수부터 출력하는 프로그램을 작성해보세요.
단, 0이 첫 번째 부터 주어지지않는다고 가정해도 좋습니다.
'''

arr = list(map(int, input().split()))
cnt = [0] * 10

for i in range(len(arr)):
    if arr[i] == 0:
        break
    cnt[arr[i] // 10] += 1

for i in range(1, 10):
    print(f"{i} - {cnt[i]}")