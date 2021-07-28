'''
Input
t – the number of numbers in list, then t lines follow [t <= 10^6].
Each line contains one integer: N [0 <= N <= 10^6]

Output
Output given numbers in non decreasing order.
'''

t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))
# print(arr)
# ans = sorted(arr)
# for elem in ans:
#     print(elem)
print(arr)

# sorting using count sort 
cnt_arr = [0] * len(arr)
# for elem in arr:
#     cnt_arr[elem] += 1
# print(cnt_arr)

