#시간초과
import code
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
nums = list(MIS())
m = int(input())
#홀수일때
#[(s-1): (s-1) + center]
#[(e-1): (s-1) + center: -1]
#짝수일때
#[(s-1): (s-1) + center]
#[e - 1 : (s-1) + center -  1: -1]

def pel(s, e):
    if s == e:
        return 1
    length = e - s + 1
    center = length // 2
    if center != 0:
        if nums[(s-1): (s-1) + center] == nums[(e - 1): (s - 1) + center: -1]:
            return 1
        else:
            return 0
    else:
        if nums [(s-1): (s-1) + center] == nums[e - 1 : (s-1) + center -  1: -1]:
            return 1
        else:
            return 0
# print()

for i in range(m):
    s, e = MIS()
    # print("asdasd")
    print(pel(s, e))

