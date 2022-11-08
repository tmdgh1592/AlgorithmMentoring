import sys
from collections import defaultdict
import math
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
dp = [0, 1]
def is_square(number):
    temp = math.sqrt(number)
    if temp == int(temp): return int(temp)
    return 0

sq = 1


for i in range(2, n + 1):
    min_val = int(1e9)
    temp = is_square(i)
    if temp:
        sq = temp
        dp.append(1)
    
    else:
        for j in range(1, sq + 1):
            min_val = min(min_val, dp[i - (j*j)] + 1)
        dp.append(min_val)
print(dp[n])