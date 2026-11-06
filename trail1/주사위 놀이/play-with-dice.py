'''
주사위를 10번 던진다고 합니다.
던질 때마다 나온 숫자가 주어지면 각 숫자가 몇 번씩 나왔는지 출력하는 프로그램을 작성해보세요.
'''

arr = map(int, input().split())
cnt = [0] * 6  # 카운트 배열

for i in arr:
    cnt[i-1] += 1

for i in range(6):
    print(f"{i+1} - {cnt[i]}")
    