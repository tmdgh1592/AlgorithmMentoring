now = 100
ch = int(input())
lenOfCh = len(str(ch))
chList = []
for i in str(ch):
    chList.append(int(i))
broken = int(input())
working = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if broken != 0 :
    num = list(map(int,input().split()))
    working = list(set(working) - set(num))
working.sort()
sol = []
sol2 = []
index = 0

def remote(ch, lenOfCh, index, status):
    if len(working) == 0:
        return None
    if lenOfCh == 0 :
        sol2.append(int(''.join(str(i) for i in sol)))
        return None
    if index == 0 or (len(sol) != 0 and sol[index - 1] in chList):
        if chList[index] in working:
            sol.append(chList[index])
            remote(ch, lenOfCh - 1, index + 1, status)
        else:
            if status == 1:
                for i in range(len(working)):
                    if chList[index] < working[i]:
                        sol.append(working[i])
                        remote(ch, lenOfCh - 1, index + 1, status)
                        break
            else:
                for i in reversed(range(len(working))):
                    if chList[index] > working[i]:
                        sol.append(working[i])
                        remote(ch, lenOfCh - 1, index + 1, status)
                        break
    else:
        if status == 1:
            sol.append(working[0])
            remote(ch, lenOfCh - 1, index + 1, status)
        else:
            sol.append(working[-1])
            remote(ch, lenOfCh - 1, index + 1, status)
def activate(ch, now):
    min = 10000000
    if ch == now:
        return 0
    for i in range(len(sol2)):
        if abs(ch - sol2[i]) < min:
            min = sol2[i]
        if abs(ch - now) < abs(ch - min) :
            return abs(now - ch)
        else:
            return len(str(min)) + abs(min - ch)
    
if len(working) == 0:
    print(abs(ch - now))
else:
    remote(ch, lenOfCh, index, 1)
    sol.clear()
    remote(ch, lenOfCh, index , -1)
    print(activate(ch, now))