N = int(input())

grade = list(map(float, input().split()))

total = 0
for i in range(N):
    total += grade[i]
    avg = total / N

if avg >= 4.0:
    print(f"{avg:.1f}", "Perfect", sep="\n")
elif avg >= 3.0:
    print(f"{avg:.1f}", "Good", sep="\n")
else:
    print(f"{avg:.1f}", "Poor", sep="\n")