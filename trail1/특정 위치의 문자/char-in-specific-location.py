text = ['L', 'E', 'B', 'R', 'O', 'S']
char = input()

for i in range(6):
    if text[i] == char:
        print(i)
        break
else:
    print("None")