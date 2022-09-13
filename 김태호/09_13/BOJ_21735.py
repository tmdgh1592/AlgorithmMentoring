#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
snow = list(MIS())

def dfs(cur_pos, total, time):
    if time == m or cur_pos == n - 1:
        return total
    ret, left, right = -float('inf'), -float('inf'), -float('inf')
    if cur_pos + 1 < n:
        left = dfs(cur_pos + 1, snow[cur_pos + 1] + total, time + 1)
    if cur_pos + 2 < n:
        right = dfs(cur_pos + 2, snow[cur_pos + 2] + (total // 2), time + 1)
    ret = max(left, right)
    return ret
print(dfs(-1, 1, 0))
