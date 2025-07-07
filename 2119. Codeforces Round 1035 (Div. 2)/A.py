t = int(input())

def handle_test_case():
    a, b, x, y = map(int, input().split())
    if a == 1 and b == 2:
        return x
    if a == b:
        return 0
    if a > b:
        if a == b + 1 and a % 2 == 1: 
            return y
        else:
            return -1
        
    if x < y:
        return (b - a) * x
    else:
        less_half = (b - a) // 2
        more_half = (b - a) - less_half
        if a % 2 == 1:
            return less_half * y + more_half * x
        else:
            return more_half * y + less_half * x

for _ in range(t):
    ans = handle_test_case()
    print(ans)