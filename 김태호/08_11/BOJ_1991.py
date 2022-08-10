#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e6))
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def pre_order(here):
    if here == -1: return 
    print(chr(here + ord('A')) , end='')
    pre_order(g[here][0])
    pre_order(g[here][1])
    return

def in_order(here):
    if here == -1: return
    in_order(g[here][0])
    print(chr(here + ord('A')) , end='')
    in_order(g[here][1])
    return

def post_order(here):
    if here == -1: return
    post_order(g[here][0])
    post_order(g[here][1])
    print(chr(here + ord('A')) , end='')
    return

n = int(input())
g = defaultdict(list)
empty_node = ord('.') - ord('A')
for _ in range(n):
    parent, left, right = map(lambda x: ord(x) - ord('A'), input().rstrip().split())
    if left != empty_node:
        g[parent].append(left)
    else:
        g[parent].append(-1)

    if right != empty_node:
        g[parent].append(right)
    else:
        g[parent].append(-1)

pre_order(0)
print()
in_order(0)
print()
post_order(0)