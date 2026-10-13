'''
주어진 입력 문자열에서 목적 문자열이 처음 등장하는 시작 인덱스를 구하는 코드를 작성해보세요.
인덱스는 0부터 시작한다고 가정합니다.
단, 일치 여부를 판단하는 일은 함수로 분리해 주세요.
입력 문자열의 시작 위치 하나를 인자로 받아 그 위치에서 목적 문자열이 시작하는지를 참 또는 거짓으로 반환하는 함수를 만들고, 앞쪽 위치부터 차례로 그 함수를 호출해 답을 찾습니다. 두 문자열은 전역 변수에 두면 함수 인자로 따로 넘기지 않아도 됩니다.
'''

text = input()
pattern = input()

def is_start(start):
    return text[start:start+len(pattern)] == pattern

def find_pattern():
    ans = -1

    for i in range(len(text)):
        if is_start(i):
            ans = i
            break

    return ans

print(find_pattern())