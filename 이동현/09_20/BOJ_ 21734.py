import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

word = list(input())


def sum_digit(n):
    sum  = 0
    while n > 0:
        sum += n % 10
        n  //= 10
    sum += n
    return sum

for i in word:
    cnt = sum_digit(ord(i))
    print(i * cnt)