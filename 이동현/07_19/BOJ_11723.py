import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
s =0 

for _ in range(n):
    data = input().rstrip().split()
    if data[0] == 'add':
        s |= (1 << (int(data[1]) - 1))
    elif data[0] == 'remove':
        s &= ~(1 << (int(data[1]) - 1))
    elif data[0] == 'check':
        print((s >> (int(data[1]) - 1)) & 1)
    elif data[0] == 'toggle':
        s ^= (1 << (int(data[1]) - 1))
    elif data[0] == 'all':
        s = ~0
    else:
        s = 0