#-*- coding:utf-8 -*-
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


MAX_IDX = 9

dy = [1, -1, 0, 0, 0]
dx = [0, 0, 1, -1, 0]

def in_range(y, x):
    return (y >= 0 and y < MAX_IDX + 1) and (x >= 0 and x < MAX_IDX + 1)

def toggle(y, x, lst):
    for dir in range(len(dy)):
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if not in_range(ny, nx): continue;
        lst[ny][nx] ^= 1

def any_switch_on(lst):
    for i in range(MAX_IDX + 1):
        if lst[9][i]:
            return True
    return False
    # for i in range(MAX_IDX + 1):
    #     for j in range(MAX_IDX + 1):
    #         if lst[i][j]:
    #             return True
    # return False

def toggle_remaining(lst):
    ret = 0
    for i in range(1, MAX_IDX + 1):
        for j in range(0, MAX_IDX + 1):
            if not lst[i - 1][j]: continue;
            toggle(i, j, lst)
            ret += 1
    return ret

def my_copy(lst):
    return [lst[i][:] for i in range(MAX_IDX + 1)]


def decide_first_row(x, lst, cnt):
    if x == MAX_IDX + 1:
        tmp = my_copy(lst)
        res = toggle_remaining(tmp)
        return res + cnt if not any_switch_on(tmp) else float('inf')
    
    ret = float('inf')
    
    ret = min(decide_first_row(x + 1, lst, cnt), ret)
    toggle(0, x, lst)
    ret = min(decide_first_row(x + 1, lst, cnt + 1), ret)
    toggle(0, x, lst)
    return ret


bulb = [list(map(lambda c : 1 if c == 'O' else 0, input().rstrip())) for _ in range(10)]
res = decide_first_row(0, bulb, 0)
print(res if res != float('inf') else -1)