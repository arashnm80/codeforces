import math

def check(n,p,l,t):
    if n == 1:
        return 0
    
    task_days = math.ceil(n / 7)

    single_task_day = task_days % 2
    double_task_days = (task_days - single_task_day) // 2
    normal_days = n - single_task_day - double_task_days

    double_task_days_max = double_task_days * (l + (2 * t))
    single_task_day_max = single_task_day * (l + t)
    normal_days_max = normal_days * l
    if double_task_days_max >= p:
        n -= math.ceil(p / (l + (2 * t)))
        return n
    
    n -= double_task_days
    p -= double_task_days_max

    if single_task_day_max >= p:
        n -= math.ceil(p / (l + t))
        return n
    
    n -= single_task_day
    p -= single_task_day_max

    if normal_days_max >= p:
        n -= math.ceil(p / l)
        return n

    return -1



testcases = int(input())
ans = []

for testcase in range(testcases):
    n, p, l, t = map(int, input().split())
    print(check(n,p,l,t))
#     ans.append(check(n,p,l,t))

# print("\n".join(map()))