import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
students = list()
for i in range(n):
    students.append(input().rstrip().split())

students.sort(key =lambda x: (-int(x[1]), x[2], -int(x[3]), x[0]))

for i in range(n):
    print(students[i][0])