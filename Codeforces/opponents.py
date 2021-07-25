# n opponents
# d days
# 0 - jth character absent on ith day

n, d = map(int, input().split())
curr_cnt = 0
max_cnt = 0

for i in range(d):
    day = input()
    if '0' in day:
        curr_cnt += 1
    else:
        # before resetting the curr_cnt we update max_cnt
        max_cnt = max(curr_cnt, max_cnt)
        curr_cnt = 0
        
print(max(max_cnt, curr_cnt))

# n d
# 4 5
# 1101 --> max_cnt = 0, curr_cnt = 1 
# 1111 --> max_cnt = 1, curr_cnt = 0
# 0110 --> max_cnt = 1, curr_cnt = 1 
# 1011 --> max_cnt = 1, curr_cnt = 2 
# 0111 --> max_cnt = 1, curr_cnt = 3



