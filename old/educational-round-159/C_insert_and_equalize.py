import math

def lcm(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return abs(a * b) // math.gcd(a, b)

def smallest_common_multiple(numbers):
    if len(numbers) < 2:
        return None  # No common multiple for a single number

    common_mult = numbers[0]
    for num in numbers[1:]:
        common_mult = lcm(common_mult, num)

    return common_mult

def gcd_of_list(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers for GCD calculation.")

    result = numbers[0]
    for num in numbers[1:]:
        if result == 0 or num == 0:
            result = max(num, result)
        else:
            result = math.gcd(result, num)

    return result

def check(n, s):
    if n == 1:
        return 1
    
    shift = min(s)
    # normalize
    if shift != 0:
        s = [x - shift for x in s]

    scm = smallest_common_multiple(s)
    gcd = gcd_of_list(s)

    ans = 0
    
    for num in s:
        ans += (scm - num) // gcd
    
    if scm == max(s):
        ans += n
    
    return n
    

t = int(input())
ans = []
for case in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    # print(check(n, s))
    ans.append(check(n,s))

print(ans)