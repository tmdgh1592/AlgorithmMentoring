#-*- coding:utf-8 -*-
import sys
from itertools import combinations
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


while (data := list(MIS())) and data[0] != 0:
    for combi in combinations(data[1:], 6):
        print(*list(combi))
    print()