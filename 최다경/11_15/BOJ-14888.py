import sys
from itertools import permutations
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = list(MIS())
oper = list(MIS())
arr = []
for i in range(len(oper)):
    if oper[i]:
        if i == 0:
            for i in range(oper[i]):
                arr.append('+')

        elif i == 1:
            for i in range(oper[i]):
                arr.append('-')

        elif i == 2:
            for i in range(oper[i]):
                arr.append('*')

        elif i == 3:
            for i in range(oper[i]):
                arr.append('/')




opers = list(permutations(arr, n - 1))

def calc(symbol, n1, n2):
    if symbol == '+':
        return n1 + n2
    elif symbol == '-':
        return n1 - n2
    elif symbol == '*':
        return n1 * n2
    else: return int(n1 / n2) 

if (n == 2):
    tmp = calc(arr[0], data[0], data[1])
    print(tmp)
    print(tmp)
    exit(0)

res = -float('inf')
res2 = float('inf')
cnt = 0
su = 0

for i in opers:
    flag = True
    cnt = 0
    su = 0
    tmp2 = 0
    for j in i:
        if cnt == 0:
            tmp = calc(j, data[0], data[cnt + 1])
            cnt += 1
            #print('if tmp', tmp)
        else:
            #print('else tmp2, data', tmp, data[cnt + 1], calc(j, tmp, data[cnt + 1]))
            tmp2 = calc(j, tmp, data[cnt + 1])
            #print('else tmp2', tmp2)
            tmp = tmp2
            cnt += 1
    res = max(res, tmp2)
    res2 = min(res2, tmp2)
print(res)
print(res2)
  