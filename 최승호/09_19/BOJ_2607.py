#-*- coding:utf-8 -*-
from collections import Counter
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
first = input().rstrip()
words = [input().rstrip() for _ in range(n-1)]

total = 0
aLen = len(first)

for word in words:
    bLen = len(word)
    if abs(aLen - bLen) >= 2:
        continue

    aChecked = [False] * aLen
    bChecked = [False] * bLen

    for i, aCh in enumerate(first):
        for j, bCh in enumerate(word):
            if not bChecked[j] and aCh == bCh:
                aChecked[i] = True
                bChecked[j] = True
                break

    aCount = aChecked.count(False)
    bCount = bChecked.count(False)

    if aCount <= 1 and bCount <= 1 and abs(aCount - bCount) <= 1:
        total += 1

print(total)