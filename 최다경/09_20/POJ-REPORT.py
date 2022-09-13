from collections import defaultdict

report_dic = defaultdict(set)
res = defaultdict(int)
def solution(id_list, report, k):
    report = list(set(report))
    for id in id_list:
        report_dic[id]
        res[id]
    for data in report:
        p1, p2 = data.split()
        report_dic[p1].add(p2)
        res[p2] += 1

    answer = []
    for id in id_list:
        cnt = 0
        for rep in report_dic[id]:
            if res[rep] >= k:
                cnt += 1
        answer.append(cnt)

    return answer


