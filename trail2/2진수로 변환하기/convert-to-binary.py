# 십진수 N이 주어지면 0과 1로만 이루어진 2진수로 그 수를 변환하여 출력하는 프로그램을 작성해보세요.

n = int(input())
digits = []

while True:   # 종료 조건 전까지 (n > 0)
    if n < 2:
        digits.append(n)
        break
    
    digits.append(n % 2)  # 현재 숫자의 나머지 저장
    n //= 2

for digit in digits[::-1]:
    print(digit, end="")