t = int(input())

for case in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sa = sorted(a)
    sb = sorted(b)
    beauty = 0
    max_beauty = 0
    ia = 0
    ib = 0
    
    p1a = sa[n - x, n]
    p2a = sa[0: n - x]

    p1b = sb[0: n - x]
    p2b = sb[n - x, n]
    
    while ia < n:
        if sa[ia] > sb[ib]:
            max_beauty += 1
        
        ia += 1

    
    print(counter)