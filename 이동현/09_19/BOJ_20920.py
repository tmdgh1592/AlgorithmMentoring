import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
word_list = defaultdict(int)
n, m = MIS()
for _ in range(n):
    word = input().rstrip()
    len_word = len(word)
    if len_word < m: continue
    # print("word 추가:", word)
    word_list[word] += 1

# print(word_list)
word_list = sorted(word_list.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i in word_list:
    print(i[0])