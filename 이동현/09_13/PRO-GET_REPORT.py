from collections import defaultdict
from operator import index
import sys

input = sys.stdin.readline
id_list = ["muzi", "frodo", "apeach", "neo"]	
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_list = {id:set() for id in id_list}
    # cnt = defaultdict(int)

    for report_case in set(report):
        name = report_case.split()
        report_list[name[1]].add(name[0])
        # cnt[name[0]] += 1

    print(report_list)
    
    for reported, users in report_list.items():
        if len(users) >= k:
            for user in users:
                answer[id_list.index(user)] += 1

    return answer
    
solution(id_list, report, k)