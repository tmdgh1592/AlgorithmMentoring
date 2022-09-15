import code
import functools
from re import X
import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

number = list(input().rstrip().split())

reverse = { '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'9', '7':'7', '8':'8', '9':'6'}

# print(number)


def cmp(a, b): #길이로 정렬
    str1 = a + b
    str2 = b + a
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1


def rev(num):
    rst = ""
    for i in num[::-1]:
        rst += reverse[i]
    return rst

for i in range(len(number)):
    number[i] = rev(number[i])

number.sort(key=lambda x : (len(x), int(x)))
# print(number)
number.append(number[-1])
# print(number)
number.sort(key=functools.cmp_to_key(cmp))

#밑의 코드는 시간초과
# print(number)
# for i in range(len(number)):
#     number[i] = rev(number[i])
# # number.reverse()
# result = ''.join(number)

# print(int(result))
print(''.join(map(rev, number)))
