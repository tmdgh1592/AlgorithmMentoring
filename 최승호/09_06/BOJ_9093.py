import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

T = int(input())

for _ in range(T):
    arr = input().split()

    for word in arr:
        print(word[::-1], end=' ')
    print()
    