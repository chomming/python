N = int(input())
total = 0
T = list(map(int, input().split()))

v = int(input())

for i in range(0, N):
    if T[i] == v:
        total += 1

print(total)
