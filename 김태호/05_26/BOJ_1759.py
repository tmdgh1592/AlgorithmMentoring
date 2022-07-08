#-*- coding:utf-8 -*-
from itertools import combinations
import sys
from collections import Counter

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


def is_possible(lst):
    _VOWEL = ['a', 'e', 'i', 'o', 'u']
    counter = Counter(lst)
    
    num_v = 0
    
    for v in _VOWEL:
        num_v += counter[v]
    print(lst, num_v)
    return (num_v >= 1) and ((len(lst) - num_v) >= 2)

l, c = MIS()
letter = sorted(list(input().rstrip().split()))

for combi in combinations(letter, l):
    if is_possible(combi):
        pass
        # print(*combi)

