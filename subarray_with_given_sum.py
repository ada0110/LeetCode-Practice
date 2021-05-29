def sumSubArr(arr, k, sum_):
    n = len(arr)
    if (n <= k):
        print('Invalid Operation')
        return -1
    
    win_sum = sum(arr[i] for i in range(k))
    if win_sum == sum_:
        print(f"given sum found at 0 and 1 position")
    # print('win_sum at 0 and 1 pos: ', win_sum)
    for i in range(n-k):
        win_sum = win_sum - arr[i] + arr[i+2]
        # print('win_sum: ', win_sum)
        if win_sum == sum_:
            print(f"{sum_} sum found between index {i+1} and {i+2}")

    return 0 



arr = [12, 8, 2, 6, 9, 5, 7]
k = 2
sum_ = 14
sumSubArr(arr, k, sum_)

