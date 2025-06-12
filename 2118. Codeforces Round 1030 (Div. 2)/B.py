t = int(input())

for i in range(t):
    n = int(input())

    print(2 * n - 1)
    for i in range(1, n+1):
        if i == 1:
            print(f"1 1 {n}")
        else:
            print(f"{i} 1 {n-i+1}")
            print(f"{i} {n-i+2} {n}")

    # # demonstration that how it will look
    # line = [str(i+1) for i in range(n)]
    # for i in range(n, 0, -1):
    #     if i == n:
    #         print(" ".join(line[::-1]))
    #     else:
    #         part_1 = line[:i]
    #         part_2 = line[-(n-i):]
    #         ans = " ".join(part_1[::-1]) + " " + " ".join(part_2[::-1])
    #         print(ans)