def swap_characters(input_string, i, j):
    # Convert the string to a list to make it mutable
    string_list = list(input_string)

    # Swap the characters at indices i and j
    string_list[i], string_list[j] = string_list[j], string_list[i]

    # Convert the list back to a string
    result_string = ''.join(string_list)

    return result_string

t = int(input())

for case in range(t):
    n = int(input())
    s = list(input())
    used = set()
    counter = 0
    while True:
        continue_loop = False
        for i in range(0, n - 1):
            if (i not in used) and s[i] == 'A' and s[i + 1] == 'B':
                s[i], s[i + 1] = s[i + 1], s[i]
                continue_loop = True
                used.add(i)
                counter += 1
        if not continue_loop:
            break
    
    print(counter)