def maxSum(arr, k):
    n = len (arr)

    if (n <= k): # array size is less than window size
        print("Invalid Operation")
        return -1 

    win_sum = sum (arr[i] for i in range(k))
    max_sum = win_sum
    # print(max_sum)

    for i in range (n-k):
        win_sum = win_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, win_sum)
        
    return max_sum
    



arr = [80, -50, 90, 100]
k = 2 # k is window size,  so ans should be 190
result = maxSum(arr, k)
print(f"maxisum sum of {k} consecutive numbers is {result}")

