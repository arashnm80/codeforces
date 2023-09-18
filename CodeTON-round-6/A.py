t = int(input())

def sum_of_0_to_y(y):
    if y == 0:
        return 0
    else:
        return y + sum_of_0_to_y(y - 1)

def func(n, k, x):
    if n < k:
        return -1
    elif x < k - 1:
        return -1
    else:
        rest = n - k
        y_sum = sum_of_0_to_y(k - 1)
        if x == k:
            last_item = x - 1
        else:
            last_item = x
        rest_sum = rest * last_item
        sum = y_sum + rest_sum
        return sum
    
for i in range(t):
    n, k, x = map(int,input().split())
    print(func(n,k,x))
    