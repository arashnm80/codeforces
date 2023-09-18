t = int(input())

def string_in_base_k(number, base_k):
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        remainder = number % base_k
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        number = number // base_k
    return result

def number_from_base_k(s, base_k):
    if not s:
        return 0
    decimal_number = 0
    power = 0
    for char in s[::-1]:
        if '0' <= char <= '9':
            decimal_number += int(char) * (base_k ** power)
        elif 'A' <= char <= 'Z':
            decimal_number += (ord(char) - ord('A') + 10) * (base_k ** power)
        else:
            raise ValueError("Invalid character in the input string")
        power += 1

    return decimal_number

def create_arr(n, k):
    arr = []
    for i in range(1, n + 1):
        i_in_base_k = string_in_base_k(i, k)
        arr.append(i_in_base_k)
    arr.sort()
    return arr

for i in range(t):
    n, k = map(int, input().split())
    arr = create_arr(n, k)
    result = 0
    print(arr)
    # for i, value in enumerate(arr):
    #     if (i + 1) == number_from_base_k(value, k):
    #         result += 1
    # print(result)