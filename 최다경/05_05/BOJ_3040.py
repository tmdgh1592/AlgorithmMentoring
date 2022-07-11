
dwarf = []
arr = []
here = -1

for i in range(9):
    dwarf.append(int(input()))
def f(arr, here):
    if len(arr) == 7:
        if sum(arr) == 100:
            print(*arr, sep = '\n')
        return None

    for i in range(here + 1, 9):
            arr.append(dwarf[i])
            here += 1
            f(arr, here)
            arr.pop()
            
f(arr, here)
