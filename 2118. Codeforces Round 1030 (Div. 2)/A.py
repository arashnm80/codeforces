t = int(input())

def handle_test_case():
    n, k = map(int, input().split())
    ones = k
    zeros = n - k

    ans = (ones > 0) * "1" + \
          max(0, (zeros - 1)) * "0" + \
          max(0, (ones - 1)) * "1" + \
          (zeros > 0) * "0"
        
    return ans

for i in range(t):
    ans = handle_test_case()
    print(ans)