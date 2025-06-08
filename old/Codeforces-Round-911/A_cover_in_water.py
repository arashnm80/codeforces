t = int(input())

for case in range(t):
    n = int(input())
    s = list(input())
    can_move = False
    for i in range(1, n - 1):
        if s[i] == s[i-1] == s[i+1] == ".":
            can_move = True
            break
    
    if can_move:
        print(2)
    else:
        print(s.count("."))