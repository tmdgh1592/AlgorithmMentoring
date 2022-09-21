#-*- coding:utf-8 -*-
import sys
from collections import Counter
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

data = [input().rstrip() for _ in range(int(input()))]
std = Counter(data[0])
res = 0

for i in range(1, len(data)):
    tmp = Counter(data[i])
    
    if std == tmp:
        res += 1
    else:
        a = std - tmp
        b = tmp - std
        if (not a and len(b) == 1 and b.most_common()[0][1] == 1) or (not b and len(a) == 1 and a.most_common()[0][1] == 1) or (len(a) == 1 and len(b) == 1 and a.most_common()[0][1] == 1 and b.most_common()[0][1] == 1):
            res += 1
print(res)