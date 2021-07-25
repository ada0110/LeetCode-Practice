n = int(input())

arr = list(map(int,input().split()))

sum_ = sum(arr)//(n//2)

for i in range(len(arr)):
    for j in range(1, len(arr)):
        if arr[i] + arr[j] == sum_ and i != j:
            print(i+1, j+1)
            arr[i] = 0
            arr[j] = 0

            

