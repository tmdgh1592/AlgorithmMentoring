arr = [int(input()) for _ in range(9)]
lst = list()

def func(lst,cur_idx):

    if(len(lst)>7 or cur_idx == len(arr)):
        return None
        
    if(sum(lst) == 100 and len(lst)==7):
        print(*lst, sep='\n')
        return None
    
    for there in range(cur_idx+1,9):
        lst.append(arr[there])
        func(lst,there)
        lst.pop()



func(lst,-1)
