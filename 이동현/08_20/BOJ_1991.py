import sys
from collections import defaultdict

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())

d = defaultdict(list)
for _ in range(n):
    parent, left, right = input().split()
    d[parent].append(left)
    d[parent].append(right)

def pre_order(node):
        print(node, end = '')
        if d[node][0] != '.':
            pre_order(d[node][0])
        if d[node][1] != '.':
            pre_order(d[node][1])

def in_order(node):
    if node != ['.', '.']:
        if d[node][0] != '.':
            in_order(d[node][0])
        print(node, end = '')
        if d[node][1] != '.':
            in_order(d[node][1])


def post_order(node):
    if node != ['.', '.']:
        if d[node][0] != '.':
            post_order(d[node][0])
        if d[node][1] != '.':
            post_order(d[node][1])
        print(node, end = '')
pre_order('A')
print()
in_order('A')
print()
post_order('A')
