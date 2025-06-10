# my answer was taking too much time after test 7 but it was good

t = int(input())

def handle_test_case():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # separate groups in zigzag
    for i in range(n):
        if i % 2 == 1:
            a[i], b[i] = b[i], a[i]
    
    # step backward from the end
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if a[i] == b[j] or a[j] == b[i]:
                return (i + 1)
            elif (j - i > 1) and (a[i] == a[j] or b[i] == b[j]):
                return (i + 1)

    return 0

for i in range(t):
    answer = handle_test_case()
    print(answer)