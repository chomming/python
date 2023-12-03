N = int(input())
T = list(map(int, input().split()))
max = T[0]
min = T[0]

for i in range(0, len(T)):
    if max < T[i]:
        max = T[i]
    elif min > T[i]:
        min = T[i]

print(min, max)
