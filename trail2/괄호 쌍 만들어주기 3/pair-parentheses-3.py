'''
문자′(′,′)′로만 이루어진 문자열 A가 주어지면, 여는 괄호와 닫는 괄호로 쌍을 이룰 수 있는 서로 다른 가짓수를 구하는 프로그램을 작성해보세요.
단, 여는 괄호가 닫는 괄호보다 먼저 나와야 합니다.

문자열 A의 길이를 ∣A∣, i번째 문자를 Ai라고 하겠습니다.
즉, 1≤i<j≤∣A∣를 만족하는 두 위치 i, j를 골라 Ai가 ′
 (′이고 Aj가 ′)′인 쌍 (i,j)의 개수를 세야 합니다.
각 쌍은 서로 독립적으로 셉니다. 따라서 같은 위치에 있는 괄호가 서로 다른 여러 쌍에 중복해서 쓰일 수 있습니다.
'''

A = input()
open = []
close = []

for i in range(len(A)):
    if A[i] == '(':
        open.append(i+1)
    else:
        close.append(i+1)

ans = []
for i in open:
    for j in close:
        if i < j:
            ans.append((i, j))

print(len(ans))