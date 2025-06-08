t = int(input())

for case in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    while True:
        continue_loop = False
        for i in range(1, n - 1):
            if num[i - 1] < num[i] and num[i] > num[i + 1]:
                x = num[i]
                y = num[i + 1]

                num[i] = y
                num[i + 1] = x

                continue_loop = True
        if not continue_loop:
            break
    
    if (num == sorted(num)):
        print("YES")
    else:
        print("NO")