#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
FILTER = lambda k: mdict[k]

mdict = defaultdict(int)

for _ in range(int(input())):
    name, state = input().rstrip().split()
    mdict[name] = (state == "enter")

print(*sorted(filter(FILTER, mdict), reverse=True), sep='\n')