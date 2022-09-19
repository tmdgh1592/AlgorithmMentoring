import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())
booked = [False] * 101
cnt = 0

for x in arr:
    if booked[x]:
        cnt+=1
    else:
        booked[x] = True

print(cnt)