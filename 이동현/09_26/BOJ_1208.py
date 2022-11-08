import sys
input = sys.stdin.readline
from collections import Counter, defaultdict
MIS = lambda: map(int, input().rstrip().split())

n, s = MIS()
original = list(MIS())

len_original = len(original)

original_l = original[:len_original//2]
original_r = original[len_original//2:]

len_l = len(original_l)
len_r = len(original_r)

res_l = defaultdict(int)
sum = 0
cnt = 0
#비트 마스크를 이용해 수열의 합을 구하는 과정
for i in range(1, (1 << len_l)):
    sum = 0
    for j in range(len_l): 
        if i & (1 << j):
            sum += original_l[j]
    res_l[sum] += 1

cnt += res_l[s]

sum = 0
for i in range(1, (1 << len_r)):
    sum = 0
    for j in range(len_r):
        if i & (1 << j):
            sum += original_r[j]
    if sum == s: cnt += 1
    if res_l[s - sum] > 0:
        cnt += res_l[s - sum]
        
print(cnt)