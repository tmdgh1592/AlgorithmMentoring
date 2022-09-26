import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

word = input().rstrip()

for char in word:
    print(char * sum(list(map(int, list(str(ord(char)))))))