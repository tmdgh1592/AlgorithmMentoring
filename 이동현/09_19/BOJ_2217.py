import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
rope = list()

for _ in range(n):
    rope.append(int(input()))
rope = sorted(rope, reverse=True)

max_weight = rope[0]

for i in range(1, n + 1):
    temp = rope[i - 1] * i
    if max_weight < temp:
        max_weight = temp
print(max_weight)