#-*- coding:utf-8 -*-
import sys
from itertools import combinations

sys.setrecursionlimit(1 << 12)

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
MIRS = lambda: map(int, sys.stdin.readlines())


dwarf = [int(input().rstrip()) for _ in range(9)]
MAX_DWARF = 7
MAX_IDX = 9
TARGET_SUM = 100

def solve_ver_1():
    def recursion(lst, here):
        if len(lst) == MAX_DWARF and sum(lst) == TARGET_SUM:
            print(*lst, sep='\n')
            sys.exit(0)
        
        for there in range(here + 1, MAX_IDX):
            lst.append(dwarf[there])
            recursion(lst, there)
            lst.pop()

    recursion(list(), -1)


def solve_ver_2():
    def recursion(lst, here, cur_sum):
        if len(lst) == MAX_DWARF and cur_sum == TARGET_SUM:
            print(*lst, sep='\n')
            sys.exit(0)
        
        for there in range(here + 1, MAX_IDX):
            lst.append(dwarf[there])
            recursion(lst, there, dwarf[there] + cur_sum)
            lst.pop()

    recursion(list(), -1, 0)

def solve_ver_3():
    for combi in combinations(dwarf, 7):
        if sum(combi) == TARGET_SUM:
            print(*list(combi), sep='\n')
            break



