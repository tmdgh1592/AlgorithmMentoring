from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
exp = list(input())

nums, ops = deque(), deque()
num = ''
hasC = False


def calc(op, n1, n2):
    if op == 'S':
        return n1 - n2
    elif op == 'M':
        return n1 * n2
    elif op == 'U':
        result = abs(n1) // abs(n2)
        if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
            result *= -1
        return result
    elif op == 'P':
        return n1 + n2



for x in exp:
    if x in ['S', 'M', 'U', 'P', 'C']:
        if x == 'C':
            hasC = True

        ops.append(x)
        if num != '':
            nums.append(int(num))
            num = ''
    else:
        num += x



result = nums.popleft()

if not hasC:
    print('NO OUTPUT')
else:
    for op in ops:
        if op == 'C':
            print(result, end=' ')
        else:
            if len(nums) > 0:
                result = calc(op, result, nums.popleft())
        
