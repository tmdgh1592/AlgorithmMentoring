import sys
import itertools

dwarf : list[int] = []
realdwarf : list[int] = []

for i in range(9):
    dwarf.append(int(input()))

#version1
def isCorrect(realdwarf,here):
    if len(realdwarf) == 7:
        if sum(realdwarf) == 100:
            print(*realdwarf, sep="\n")
            sys.exit(0)
        return None

    for there in range(here+1,9):
        realdwarf.append(dwarf[there])
        isCorrect(realdwarf,there)
        realdwarf.pop()

isCorrect(realdwarf, -1)