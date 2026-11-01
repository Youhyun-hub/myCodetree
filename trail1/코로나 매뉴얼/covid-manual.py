'''
감기 증상이 있으면 Y, 없으면 N으로 나타내기로 하고, 증상 여부와 체온에 따라 진료소를 다음과 같이 구분하려고 합니다.

증상이 있고, 체온이 37℃ 이상일 때 A
증상이 없고, 체온이 37℃ 이상일 때 B
증상이 있고, 체온이 37℃ 미만일 때 C
증상이 없고, 체온이 37℃ 미만일 때 D
한 번에 3명씩 검사하는데 A로 가는 사람이 2명 이상 나올 때는 위급상황으로 분류합니다. 위급상황인지를 판단하는 프로그램을 작성해보세요.
'''
ans = []  # A 개수
for i in range(3):
    cold, temp = input().split()
    temp = int(temp)

    if cold == 'Y':
        if temp >= 37:
            ans.append('A')
        else:
            continue
    else:  # 증상 없음
        continue
    
if len(ans) >= 2:
    print('E')
else:
    print('N')
    # cold.append(int(a))
    # temp.append(b)
    # cold1, temp1 = input().split()
    # cold2, temp2 = input().split()
    # cold3, temp3 = input().split()


