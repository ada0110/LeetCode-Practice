# n: number of rows and columns in the table.
t = int(input())

for i in range(t):
    n = int(input())
    l = []
    for j in range(n):
        s = input()
        l.append(list(s))
    print("list of str:", l)
    
    stars = []
    for elem in l:
        print("elem:", elem)
        for l in range(len(elem)):
            if elem[l] == '*':
                stars.append(l)
  
        print("stars pos:", stars)    
            # for val in stars:
            #     elem[val] = '*'




# for i in range(t):
#     n = int(input())
#     for j in range(n):
#         s = input()
#         for j, char in enumerate(s):
#             if s[j] == '*':
#                 print(j)



#     # print(l)

       
       

    
