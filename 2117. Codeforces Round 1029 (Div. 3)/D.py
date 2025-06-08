t = int(input())
 
def solve_test_case():
    n = int(input())
    nums = list(map(int, input().split()))

    answer = True

    # reverse if necessary
    if nums[1] < nums[0]:
        nums.reverse()

    step = nums[1] - nums[0]

    if step > min(nums):
        return False
    
    for i in range(1, n):
        if (nums[i] - nums[i-1]) != step:
            answer = False
            break
        
 
for i in range(t):
    answer = solve_test_case()

    if answer:
        print("yes")
    else:
        print("no")