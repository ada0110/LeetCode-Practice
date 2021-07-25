#  -1 if we can't obtain 1
#  else print min no. of moves
t = int(input())

for i in range(t):
    n = int(input())
    c = 0

    while (n % 2 == 0):
        n = n//2
        c += 1
    while(n % 3 == 0):
        n = n//3
        c += 2
    while(n % 5 == 0):
        n = n//5
        c += 3

    if n == 1:
        print(c)
    else:
        print(-1)



