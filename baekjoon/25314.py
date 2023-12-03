N = int(input())
total = 0

for i in range (0, N):
    if i % 4 ==0:
        total += 1

print("long "*total+"int")
