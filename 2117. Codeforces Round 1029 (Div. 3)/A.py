t = int(input())

def solve_test_case():
    n, x = map(int, input().split())
    doors = list(map(int, input().split()))

    first = doors.index(1) # first closed door
    last = len(doors) - 1 - doors[::-1].index(1)  # last closed door

    if last - first + 1 <= x:
        print("yes")
    else:
        print("no")


for i in range(t):
    solve_test_case()