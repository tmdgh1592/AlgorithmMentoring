import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
jongee = list()

for _ in range(n):
    jongee.append(list(MIS()))

white = 0
blue = 0

def check(width, ypos, xpos):
    global white, blue
    start = jongee[ypos][xpos]
    for i in range(ypos, ypos + width):
        for j in range(xpos, xpos + width):
            if start != jongee[i][j]:
                new_width = width // 2
                check(new_width, ypos, xpos)
                check(new_width, ypos, xpos + new_width)
                check(new_width, ypos + new_width, xpos)
                check(new_width, ypos + new_width, xpos + new_width)
                return None
    if start == 0:
        white += 1
    else:
        blue += 1
check(n, 0, 0)
print(white)
print(blue)