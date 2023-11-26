t = int(input())

def simplify(abc):
    if abc == [1, 1, 1] or abc == [0, 0, 0]:
        return abc
    
    if abc.count(0) == 2 and abc.count(1) == 1:
        return abc
    
    if abc.count(0) == 1 and abc.count(1) == 2:
        for i in range(3):
            if abc[i] == 0:
                abc[i] = 1
            else:
                abc[i] = 0
        return abc
    
    if abc.count(0) == 2:
        for i in range(3):
            if abc[i] != 0:
                abc[i] = 1
                return abc
            
    for i in range(3):
        if abc[i] > 1:
            abc[i] = abc[i] % 2
            return simplify(abc)
        
    if abc.count(1) == 1:
        return abc
    
    if abc.count(1) == 2:
        for i in range(3):
            if abc[i] == 0:
                abc[i] = 1
            else:
                abc[i] = 0
        return abc

    return "wrong"



for case in range(t):
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        ans = [0, 0, 0]
    elif a == b == c == 1:
        ans = [1, 1, 1]
    else:
        ans = simplify([a, b, c])

    print(" ".join(map(str, ans)))