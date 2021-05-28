def binarySearch(arr, target):
    l = 0
    r = len(arr)-1
    
    while(l<=r):
        mid = (l+r)//2 #finding the middle index 
        
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            l = mid + 1
        else:
            r = mid - 1

    return -1 



arr = [5, 8, 11, 15, 19, 25]
# target = 19

target = int (input('enter number you want to search: '))
result = binarySearch(arr, target)

if result != -1:
    print(f"Element is present at index {result}.")
else:
    print(f"The element does not exit in array.")
