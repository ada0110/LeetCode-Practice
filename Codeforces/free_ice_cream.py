# x ice cream packs
# n is queue length 
n, x = map(int, input().split())
# print(n, x)
distress = 0
for i in range(n):
    l = input().split()
    # print(l)
    if l[0] == '+':
        x += int(l[1])
    else:
        if(x - int(l[1]) < 0):
            distress += 1
        else:
            x -= int(l[1])

        

print(x, distress)
    

