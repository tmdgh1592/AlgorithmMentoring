#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def init_are_friends():
    ret = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(0, m * 2, 2):
        ret[relationship[i]][relationship[i + 1]] = ret[relationship[i + 1]][relationship[i]] = True
    return ret

def count_pair(taken):
    first_not_taken = -1
    
    for i in range(n):
        if taken[i]: continue;
        first_not_taken = i
        break
    
    if first_not_taken == -1: return 1;
    ret = 0
    
    for pair_with in range(first_not_taken + 1, n):
        if taken[pair_with] or not are_friends[first_not_taken][pair_with]: continue;
        taken[first_not_taken] = taken[pair_with] = True
        ret += count_pair(taken)
        taken[first_not_taken] = taken[pair_with] = False
    return ret

# declare global variables
n, m = -1, -1
relationship = list()

# main
for _ in range(int(input())):
    n, m = MIS()
    relationship = list(MIS())
    
    are_friends = init_are_friends()
    res = count_pair([False for _ in range(n)])
    print(res)