import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(input().rstrip().split())

table = {
    '6':'9',
    '9':'6'
}

my_str = ''

for x in arr:
    if x in table:
        my_str += table[x]
    else:
        my_str += x

print(my_str)

