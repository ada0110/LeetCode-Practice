t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}

    for i, elem in enumerate(arr):
        if elem in d:
            d[elem].append(i)
        else:
            d[elem] = [i]
  
    for key in d:
        if len(d[key]) == 1:
            print(d[key][0] + 1)
            break




