import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

s = 0

for _ in range(int(input())):
    arr = input().rstrip().split()

    if arr[0] == 'add':
        s |= (1 << (int(arr[1]) - 1))
    elif arr[0] == 'remove':
        s &= ~(1 << (int(arr[1])) - 1)
    elif arr[0] == 'check':
        print((s >> (int(arr[1]) - 1)) & 1)
    elif arr[0] == 'toggle':
        s ^= (1 << (int(arr[1]) - 1))
    elif arr[0] == 'all':
        s = ~0
    else:
        s = 0
