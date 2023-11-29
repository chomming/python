X = int(input()) # 총 금액
N = int(input()) # 물건 종류의 수
total = 0

for i in range(0, N):
    a, b = map(int, input().split())
    total += a*b

if X == total:
    print('Yes')
else:
    print('No')
