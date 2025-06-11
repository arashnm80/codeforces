import math

t = int(input())

for i in range(t):
    n = int(input())

    root = int(math.sqrt(n))
    if root * root == n:
        print(0, root)
    else:
        print(-1)