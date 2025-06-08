t = int(input())

for case in range(t):
    n = int(input())
    s = list(input())
    # method 1: not optimized
    # unused = set(range(n))
    # # used = set()
    # # counter = 0
    # while True:
    #     continue_loop = False
    #     for i in sorted(unused):
    #         if i < n - 1:
    #             if s[i] == 'A' and s[i + 1] == 'B':
    #                 s[i], s[i + 1] = s[i + 1], s[i]
    #                 continue_loop = True
    #                 # used.add(i)
    #                 unused.remove(i)
    #                 # counter += 1
    #     if not continue_loop:
    #         break
    # print(n - len(unused))

    # method 2: perfect optimized
    if "A" not in s or "B" not in s:
        print(0)
    else:
        first_A = s.index("A")
        reversed_s = s[::-1]  # Reverse the list
        last_B = len(s) - reversed_s.index("B") - 1
        if first_A > last_B:
            print(0)
        else:
            print(last_B - first_A)