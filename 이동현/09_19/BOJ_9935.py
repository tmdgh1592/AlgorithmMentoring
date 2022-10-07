#시간초과
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

word = input().rstrip()
bomb = input().rstrip()
len_bomb = len(bomb)

#구글에서 찾은 인덱스 찾기 함수
def find_index(data, target):
    res = []
    lis = data
    while True:
        try:
            res.append(lis.index(target) + (res[-1] + 1 if len(res) != 0 else 0)) 
            lis = data[res[-1] + 1:]
        except:
            break
    return res

res = find_index(word,bomb)

#문자열 슬라이싱으로 문자열 폭발
# def explosion(index,len_bomb, word):
#     if index == 0:
#         new_word = word[len_bomb:]
#     else:
#         new_word = word[:index] + word[index + len_bomb:]
#     return new_word

# while res:
#     index = res.pop()
#     word = explosion(index, len_bomb, word)
#     if not res:
#         res = find_index(word,bomb)

def explosion(index,len_bomb, word):
    while index:
        cur = index.pop()
        if cur == 0:
            new_word = word[len_bomb:]
        else:
            new_word = word[:cur] + word[cur + len_bomb:]
        return new_word

while res:
    index = res
    word = explosion(index, len_bomb, word)
    if not res:
        res = find_index(word,bomb)


if not word:
    print("FRULA")
    exit()

print(word)