# O(n^2) brute force approach
def duplicate_elem1(arr):
    ans = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                ans.append(arr[i])
    
    return sorted(ans)


# O(n) using dictionaries
def duplicate_elem2(arr):
    d = {}
    ans = []
    for elem in arr:
        if elem in d: #O(n)
            d[elem] += 1
        else:
            d[elem] = 1
    
    for elem in d:
        if d[elem] > 1: # O(n)
            ans.append(elem)
        
    return ans





ans = duplicate_elem2([1,4,8,5,3,5,3])
print("ans:", ans)
