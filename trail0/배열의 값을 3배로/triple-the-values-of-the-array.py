matrix = []
for _ in range(3):
    arr = list(map(int, input().split()))
    new_row = []
    for i in arr:
        new_row.append(i * 3)
    matrix.append(new_row)

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end = " ")
    print()

# # 3줄의 입력을 받아 각각 3배를 한 뒤 바로 출력
# for _ in range(3):
#     # 1. 입력받은 수들을 각각 3배하여 리스트 생성 (리스트 컴프리핸션)
#     row = [x * 3 for x in map(int, input().split())]
    
#     # 2. 리스트 요소를 공백으로 구분하여 한 줄 출력 (* 언패킹)
#     print(*row)