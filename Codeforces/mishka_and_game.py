n = int(input())
m = 0
c = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        m += 1
    elif y > x:
        c += 1


if m == c:
    print("Friendship is magic!^^")
elif m > c:
    print("Mishka")
else:
    print("Chris")

