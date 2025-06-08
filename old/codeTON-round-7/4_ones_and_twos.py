t = int(input())

for case in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = (arr[i] == 2) # 1 is False, 2 is True
    for query in range(q):
        func =  list(map(int, input().split()))
        op = func[0]
        if op == 1:
            check_sum = func[1]
            ###### check
            two_count = arr.count(True)
            one_count = n - two_count
            max_sum = two_count * 2 + one_count

            if check_sum > max_sum:
                print("NO")
                continue

            min_count = check_sum // 2
            if min_count > n:
                print("NO")
                continue

            found = False
            for start in range(n):
                for size in range(min_count, n - start + 1):
                    sub_arr = arr[start:start+size]
                    sub_arr_two_cont = sub_arr.count(True)
                    sub_arr_one_count = size - sub_arr_two_cont
                    sub_arr_sum = sub_arr_two_cont * 2 + sub_arr_one_count
                    if sub_arr_sum == check_sum:
                        found = True
                        break
                if found:
                    break
            
            if found:
                print("YES")
            else:
                print("NO")
            ###### check
        else:
            index_to_change = func[1] - 1
            new_value = (func[2] == 2)
            arr[index_to_change] = new_value