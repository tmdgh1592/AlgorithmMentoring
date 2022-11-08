# -*- coding:utf-8 -*-
from collections import Counter
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def MIS(): return map(int, input().rstrip().split())

n, m = MIS()

arr = list(filter(lambda word: len(word) >= m, [input().rstrip() for _ in range(n)]))
counter = Counter(arr)

result = list(set(arr))
result.sort(key=lambda word: (-counter[word], -len(word), word))

print(*result, sep='\n')