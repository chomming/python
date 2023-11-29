a, b, c = map(int, input('').split())

if a == b:
    if a == c:
        print(10000+(a*1000))
    else:
        print(1000+(a*100))
else: # a != b
    if a == c: # a != b, a == c
        print(1000+a*100)
    elif b == c: # a != b, b == c
        print(1000+b*100)
    else:
        if (a > b) and (a > c):
            print(a*100)
        elif (b > a) and (b > c):
            print(b*100)
        elif (c > a) and (c > b):
            print(c*100)
