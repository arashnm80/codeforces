t = int(input())

def solve_test_case():
    n = int(input())
    arr = list(map(int, input().split()))

    count = 1
    check = set()
    biggest_set = set()
    for i in range(n):
        check.add(arr.pop(0))

        # the very first item
        if not biggest_set:
            biggest_set = check.copy()
            check.clear()
            continue

        if biggest_set.issubset(check):
            count += 1
            biggest_set = check.copy()
            check.clear()

    print(count)


for i in range(t):
    solve_test_case()