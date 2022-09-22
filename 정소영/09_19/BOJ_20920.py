#-*- coding:utf-8 -*-
from collections import Counter, defaultdict

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n , m = MIS()
words = list()
for i in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    words.append(word)

words = Counter(words)
words = sorted(words.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(words)):
    print(*words[i][0], sep='')

