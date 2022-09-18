import sys
from collections import Counter
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())

standard = list(input().rstrip())
len_standard = len(standard)

word_list = list()
for i in range(n -1):
    temp = input().rstrip()
    len_temp = len(temp)
    if len_standard -1 <= len_temp and len_temp <= len_standard + 1:
        word_list.append(list(temp))
    else: continue

cnt = 0
cnt_standard = Counter(standard)

for word in word_list:
    cnt_word = Counter(word)
    rst = max(sum((cnt_standard - cnt_word).values()), sum((cnt_word - cnt_standard).values()))
    if rst <= 1:
        cnt += 1
print(cnt)