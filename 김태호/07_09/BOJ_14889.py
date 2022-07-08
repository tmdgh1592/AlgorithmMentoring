#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def calc(lst):
    ret = 0
    
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j: continue;
            ret += stats[lst[i]][lst[j]]
    return ret

def bf(cur):
    if len(team_a) > n // 2 or len(team_b) > n // 2: return float('inf');
    if len(team_a) == n // 2 and len(team_b) == n // 2:
        return abs(calc(team_a) - calc(team_b))
    
    ret = float('inf')
    
    team_a.append(cur)
    ret = min(bf(cur + 1), ret)
    team_a.pop()
    
    team_b.append(cur)
    ret = min(bf(cur + 1), ret)
    team_b.pop()
    
    return ret

# declare global variables
n = int(input())
stats = [list(MIS()) for _ in range(n)]
team_a = list()
team_b = list()


print(bf(0))