h, m = map(int, input('').split())
add = int(input(''))
madd = m+add # minute

if madd < 60:
    print(h, madd)
else:
    hadd = madd//60 # hour

    if madd % 60 == 0:
        if h+hadd > 23:
            print((h+hadd)-24, 0)
        else:
            print(h+hadd, 0)
    else:
        if h+hadd > 23:
            print((h+hadd)-24, madd-(60*hadd))
        else:
            print(h+hadd, madd-(60*hadd))
