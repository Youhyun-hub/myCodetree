n = int(input())

# Please write your code here.
def get_num_square(num):
    num_list = [1] * (num**2)
    for i in range(1, num*num):
        num_list[i] += num_list[i-1]
        if num_list[i-1] == 9:
            num_list[i] = 1
    
    num_square = [[0]*num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            num_square[i][j] = num_list[i*num+j]
    
    # 출력
    for i in range(num):
        print(' '.join(map(str, num_square[i])))

get_num_square(n)


            