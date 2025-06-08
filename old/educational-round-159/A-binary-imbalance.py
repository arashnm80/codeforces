t = int(input())

for testcase in range(t):
    n = int(input())
    s = input()
    if s.count("0") > 0:
        print("YES")
    else:
        print("NO")