from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
tree = defaultdict(list)
# for i in range(n):
#     p, l, r = input().rstrip().split()
#     if l != '.':
#         tree[tree.index(p) + 1] = l
#     else: 
#         tree[tree.index(p) + 1] = '.'
#     if r != '.':
#         tree[tree.index(p) + 2] = r
#     else: 
#         tree[tree.index(p) + 2] = '.'

for _ in range(n):
    p, l, r = input().rstrip().split()
    if l != '.':
        tree[p].append(l)
    else:
        tree[p].append(0)
    if r != '.':
        tree[p].append(r)
    else:
        tree[p].append(0)

def pre(pos):
    if pos == 0: return
    print(pos, end = '')
    pre(tree[pos][0])
    pre(tree[pos][1])

def ino(pos):
    if pos == 0: return
    ino(tree[pos][0])
    print(pos, end = '')
    ino(tree[pos][1])

def post(pos):
    if pos == 0: return
    post(tree[pos][0])
    post(tree[pos][1])
    print(pos, end = '')

pre('A')
print()
ino('A')
print()
post('A')