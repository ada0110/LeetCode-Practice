debug = False

# n = int(input("enter number of lanterns:"))
# l = int(input("enter length of street:"))
n = int(input())
l = int(input())
arr = []
# for i in range(n):
#     elem = int(input())
#     arr.append(elem)

arr = [int(elem) for elem in input().split()]

# arr = list(map(int, input().split()))
arr.sort()

# distance between 0 and starting lantern
x = arr[0] - 0

# distance between last lantern and lenght of street which is endpoint
y = l - arr[-1]

if debug: print(f"x(0-a1): {x} y(l-an): {y}")

# checking the maximum distance between the lanterns
max_dist = 0
for i in range(1, len(arr)):
    dist = arr[i] - arr[i-1]
    max_dist = max(dist, max_dist)
if debug: print(max_dist)

if debug: print("max distance between lanterns:", max_dist)

# max_dist/2 --> area which can be lit by one lantern
ans = max(max_dist/2, max(x,y))

print("ans:", ans)