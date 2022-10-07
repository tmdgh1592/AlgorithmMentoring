import sys
from collections import Counter

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
words = []

for _ in range(n):
    word = input().rstrip()
    if len(word) < m: continue
    words.append(word)

c = Counter(words)
c = sorted(c.items() , key = lambda x: (-x[1], -len(x[0]), x[0]))

for word in c:
    print(word[0])



