#-*- coding:utf-8 -*-
from collections import Counter
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [input().rstrip() for _ in range(n)]
first = Counter(arr[0])

cnt = 0

for i in range(1, len(arr)):
    word = Counter(arr[i])

    if first == word:
        cnt += 1
    else:
        #단어 하나 뺀 경우
        plus = word - first
        minus = first - word
        if not plus and (len(minus) == 1 and minus.most_common()[0][1] == 1):
            cnt += 1
        #단어 하나 추가한 경우
        if not minus and len(plus) == 1 and plus.most_common()[0][1] == 1:
            cnt += 1
        # 한글자씩 차이나는 경우
        if len(minus) == 1 and len(plus) == 1 and plus.most_common()[0][1] == 1 and minus.most_common()[0][1] == 1:
            cnt += 1
print(cnt)



