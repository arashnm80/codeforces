t = int(input())

def solve_test_case():
    n = int(input())
    p = list(range(n))
    
    for j in range(n):
        p[j] += 1

    p.pop(0)
    p.append(1)

    print(" ".join(map(str, p)))


for i in range(t):
    solve_test_case()