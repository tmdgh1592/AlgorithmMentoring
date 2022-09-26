import code
import sys
from collections import Counter


input = sys.stdin.readline
MIS = lambda: map(input().rstrip().split())

n = int(input())
f_word = input().rstrip()
words = [input().rstrip() for _ in range(n - 1)]
fc = Counter(f_word)#비교 대상 단어 카운터

cnt = 0#없는 단어 카운트
cnt2 = 0#존재하는 단어 카운트
res = 0#답

for word in words:#list에서 단어 하나씩 뽑아서 비교
    if abs(len(f_word) - len(word)) >= 2: continue
    wc = Counter(word)
    cnt = 0
    cnt2 = 0
    check2 = [False] * len(word)
    for alpha in wc:#단어에 있는 글자 1개
        if alpha[0] not in fc:#비교 대상 단어에 없는 글자일 경우
                cnt += wc[alpha[0]]
                print(cnt, alpha)
        for letter in fc: #비교 대상 단어의 글자 1개
            if alpha[0] == letter[0]:#존재하는 글자일 경우
                cnt2 += abs(fc[letter] - wc[alpha]) 
                print(cnt2, alpha, letter)
    if len(f_word) == len(word) and cnt <= 1 and cnt != 0: res += 1
    elif cnt + cnt2 <= 1: res += 1
    print(cnt, cnt2)

print(res)

#abbc
#abcc