'''
N 개의 원소와 Q 개의 질의가 주어집니다.

하나의 질의는 다음 세 종류 중 하나입니다:

"1 a"
a번째 원소를 출력합니다.

"2 b"
N 개의 원소 중에 값이 b인 원소를 찾아, 그 원소가 몇 번째 원소인지 출력합니다.
그러한 원소가 여러 개라면, 그 중에서 index가 제일 작은 원소의 것을 출력합니다.
그러한 원소가 없다면, 0을 출력합니다.

"3 s e"
s번째 원소부터 e번째 원소까지 각 원소의 값을 공백으로 구분하여 차례대로 출력합니다.
각 질의를 차례대로 수행하는 프로그램을 작성해보세요.
'''

n, q = map(int, input().split())  # n - 원소 개수, q - 질의 개수
num = list(map(int, input().split()))  # 정수 배열

query = [list(input().split()) for _ in range(q)]  # 질의 배열

for i in range(q):
    if query[i][0] == '1':  # 1번 질의일 때
            print((num[int(query[i][1])-1]))  # a번째 원소 출력합니다

    if query[i][0] == '2':  # 2번 질의일 때
        for j in range(n):
            if num[j] == int(query[i][1]): # b인 원소를 찾아 idx 출력
                print(j+1)
                break
        else:
            print(0)  # 모두 순회했는데 없으면 0

    if query[i][0] == '3':  # 3번 질의일 때
        for j in range(int(query[i][1])-1, int(query[i][2])):
            print(num[j], end= " ")
        print()
