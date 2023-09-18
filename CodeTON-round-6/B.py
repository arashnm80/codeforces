def xor_of_numbers(numbers):
    result = 0
    for num in numbers:
        result ^= num
    return result

def or_of_numbers(numbers):
    result = 0
    for num in numbers:
        result |= num
    return result

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    or_of_b = or_of_numbers(b)

    min_xor = max_xor = xor_of_numbers(a)
    for i in b:
        min_temp = min_xor ^ i
        if min_temp < min_xor:
            min_xor = min_temp
        
        max_temp = max_xor ^ i
        if max_temp > max_xor:
            max_xor = max_temp
    print("Hi",min_xor, max_xor)