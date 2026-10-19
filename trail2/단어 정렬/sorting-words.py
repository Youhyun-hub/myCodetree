n = int(input())
word = [input() for _ in range(n)]

for word in sorted(word):
    print(word)