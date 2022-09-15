import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
nun = list(MIS())
max_size = 0
nundungee = list()

def calc_size(index):
    sum = 0
    for i in index:
        sum += nun[i]
    return sum

def per():
    if len(nundungee) == m:
        temp = calc_size(nundungee)
        if max_size < temp:
            max_size = temp
    for i in range(n):
        nundungee.append[i]